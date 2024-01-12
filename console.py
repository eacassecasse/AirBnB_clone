#!usr/bin/python3
import cmd
from importlib import import_module
from models import storage

"""Defines a simple command line interpreter"""


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

    def do_create(self, line):
        """The ``create`` command creates new instances and
        save them to a JSON file"""
        if len(line.split()) <= 0 or not line.split()[0]:
            print("** class name missing **")
        elif line.split()[0] not in HBNBCommand.__modelsMapper:
            print("** class doesn't exist **")
        else:
            class_name = line.split()[0]
            module = import_module(HBNBCommand.__modelsMapper.get(class_name))
            model = getattr(module, class_name)()
            model.save()

            _all = storage.all()
            [print(obj_id.split('.')[1]) for obj_id in _all.keys()
             if _all.get(obj_id).id == model.id]

    def do_show(self, line):
        """The ``show`` command displays an object to the user based
        on its Identifier"""
        if len(line.split()) <= 0 or not line.split()[0]:
            print("** class name missing **")
        elif line.split()[0] not in HBNBCommand.__modelsMapper:
            print("** class doesn't exist **")
        else:
            try:
                class_name = line.split()[0]
                _id = line.split()[1]
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
        if len(line.split()) <= 0 or not line.split()[0]:
            print("** class name missing **")
        elif line.split()[0] not in HBNBCommand.__modelsMapper:
            print("** class doesn't exist **")
        else:
            try:
                class_name = line.split()[0]
                _id = line.split()[1]
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
        if line and line.split()[0] not in HBNBCommand.__modelsMapper:
            print("** class doesn't exist **")
        else:
            _all = storage.all()
            if line:
                results = [str(_obj) for _obj in _all.values()
                           if _obj.__class__.__name__ == line]
            else:
                results = [str(_obj) for _obj in _all.values()]

            print(results)

    def do_update(self, line):
        """The ``update`` command modifies an object's attribute
        based on the Identifier and other arguments given by the user"""
        _args = line.split()

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
                print("** value missing **")
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
