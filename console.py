#!usr/bin/python3
import cmd
import re
from shlex import split
from importlib import import_module
from models import storage

"""Defines a simple command line interpreter"""


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """
    This is the command line interpreter for the AirBnB Clone Project.
    It will help us to manipulate data without having a visual interface.

    It has 3 main purposes:
    - to create data model
    - to manage (create, update, destroy, etc) objects
    - to store and persist objects to a file (in our case, JSON file)

    This interpreter will be used to validate the storage engine too.
    """

    prompt = '(hbnb) '
    __modelsMapper = {
        'BaseModel': 'models.base_model',
        'Amenity': 'models.amenity',
        'City': 'models.city',
        'Place': 'models.place',
        'Review': 'models.review',
        'State': 'models.state',
        'User': 'models.user'
    }

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_create(self, line):
        """The ``create`` command creates new instances and
        save them to a JSON file"""
        argl = parse(line)
        if len(argl) <= 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__modelsMapper:
            print("** class doesn't exist **")
        else:
            class_name = argl[0]
            module = import_module(HBNBCommand.__modelsMapper.get(class_name))
            model = getattr(module, class_name)()
            model.save()

            _all = storage.all()
            [print(obj_id.split('.')[1]) for obj_id in _all.keys()
             if _all.get(obj_id).id == model.id]

    def do_show(self, line):
        """The ``show`` command displays an object to the user based
        on its Identifier"""
        argl = parse(line)
        if len(argl) <= 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__modelsMapper:
            print("** class doesn't exist **")
        else:
            try:
                class_name = argl[0]
                _id = argl[1]
                _all = storage.all()
                for obj_id in _all.keys():
                    _class = _all.get(obj_id).__class__.__name__
                    if (_class == class_name
                            and _all.get(obj_id).id == _id):
                        print(_all.get(obj_id))
                        return

                print("** no instance found **")
            except IndexError:
                print("** instance id missing **")

    def do_destroy(self, line):
        """The ``destroy`` command deletes an object based on the
        Identifier given by the user"""
        argl = parse(line)
        if len(argl) <= 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__modelsMapper:
            print("** class doesn't exist **")
        else:
            try:
                class_name = argl[0]
                _id = argl[1]
                _all = storage.all()
                for obj_id in _all.keys():
                    _class = _all.get(obj_id).__class__.__name__
                    if (_class == class_name
                            and _all.get(obj_id).id == _id):
                        del _all[obj_id]
                        storage.save()
                        return

                print("** no instance found **")
            except IndexError:
                print("** instance id missing **")

    def do_all(self, line):
        """The ``all`` command prints all string representations of
        all the instances based or not on the class name"""
        argl = parse(line)

        if len(argl) > 0 and argl[0] not in HBNBCommand.__modelsMapper:
            print("** class doesn't exist **")
        else:
            _all = storage.all()
            if len(argl) > 0:
                results = [str(_obj) for _obj in _all.values()
                           if _obj.__class__.__name__ == argl[0]]
            else:
                results = [str(_obj) for _obj in _all.values()]

            print(results)

    def do_update(self, line):
        """The ``update`` command modifies an object's attribute
        based on the Identifier and other arguments given by the user"""
        _args = parse(line)

        match len(_args):
            case 0:
                print("** class name missing **")
            case 1:
                print("** class doesn't exist **") \
                    if _args[0] not in HBNBCommand.__modelsMapper \
                    else print("** instance id missing **")
            case 2:
                print("** attribute name missing **")
            case 3:
                try:
                    _isDict = type(eval(_args[2])) != dict

                    _all = storage.all()
                    _obj = _all.get('{}.{}'.format(_args[0], _args[1]))
                    if _obj is None:
                        print("** no instance found **")
                        return

                    for key, val in eval(_args[2]).items():
                        if (key in _obj.__class__.__dict__.keys() and
                                type(_obj.__class__.__dict__[key]) in [str, int, float]):
                            _type = type(_obj.__class__.__dict__[key])
                            _obj.__dict__[key] = _type(val)
                        else:
                            _obj.__dict__[key] = val
                except NameError:
                    print("** value missing **")
                    return False
            case 4:
                _all = storage.all()
                _obj = _all.get('{}.{}'.format(_args[0], _args[1]))
                if _obj is None:
                    print("** no instance found **")
                    return
                if _args[2] in _obj.__class__.__dict__.keys():
                    value_type = type(_obj.__class__.__dict__.get(_args[2]))
                    _obj.__dict__.update({_args[2]: value_type(_args[3])})
                else:
                    _obj.__dict__.update({_args[2]: _args[3]})

                storage.save()

    def do_count(self, line):
        """The ``count`` counts the amount of instances of some abject
                exists"""
        _args = parse(line)
        count = 0
        for _obj in storage.all().values():
            if _args[0] == _obj.__class__.__name__:
                count += 1

        print(count)

    def emptyline(self):
        """Override the default mode to don't execute blank lines"""
        pass

    def do_EOF(self, line):
        """This EOF command exit the command line processor\n"""
        print("")
        return True

    def do_quit(self, line):
        """The ``quit`` command exit the command line processor\n"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
