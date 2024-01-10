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
        'BaseModel': 'models.base_model'
    }

    def do_create(self, line):
        """The ``create`` command creates new instances and
        save them to a JSON file"""
        if len(line.split()) <= 0 or not line.split()[0]:
            print("** class name missing **")
        elif line.split()[0] not in self.__modelsMapper:
            print("** class doesn't exist **")
        else:
            class_name = line.split()[0]
            module = import_module(self.__modelsMapper.get(class_name))
            model = getattr(module, class_name)()
            model.save()

            _all = storage.all()
            [print(obj_id.split('.')[1]) for obj_id in _all.keys()
             if _all.get(obj_id).get('id') == model.id]

    def do_show(self, line):
        """The ``show`` command displays an object to the user based
        on its Identifier"""
        if len(line.split()) <= 0 or not line.split()[0]:
            print("** class name missing **")
        elif line.split()[0] not in self.__modelsMapper:
            print("** class doesn't exist **")
        else:
            try:
                class_name = line.split()[0]
                _id = line.split()[1]
                _all = storage.all()
                for obj_id in _all.keys():
                    if (_all.get(obj_id).get('__class__') == class_name
                            and _all.get(obj_id).get('id') == _id):
                        module = import_module(self.__modelsMapper.get(class_name))
                        model = getattr(module, class_name)(_all.get(obj_id))
                        print(model)
                        return

                print("** no instance found **")
            except IndexError:
                print("** instance id missing **")

    def do_destroy(self, line):
        """The ``destroy`` command deletes an object based on the
        Identifier given by the user"""
        if len(line.split()) <= 0 or not line.split()[0]:
            print("** class name missing **")
        elif line.split()[0] not in self.__modelsMapper:
            print("** class doesn't exist **")
        else:
            try:
                class_name = line.split()[0]
                _id = line.split()[1]
                _all = storage.all()
                for obj_id in _all.keys():
                    if (_all.get(obj_id).get('__class__') == class_name
                            and _all.get(obj_id).get('id') == _id):
                        _all.pop(obj_id)
                        return

                print("** no instance found **")
            except IndexError:
                print("** instance id missing **")

    def do_all(self, line):
        """The ``all`` command prints all string representations of
        all the instances based or not on the class name"""
        if line and line.split()[0] not in self.__modelsMapper:
            print("** class doesn't exist **")
        else:
            _all = storage.all()
            print(_all)

    def do_update(self, line):
        pass

    def emptyline(self):
        """Override the default mode to don't execute blank lines"""
        pass

    def do_EOF(self, line):
        """This EOF command exit the command line processor\n"""
        return True

    def do_quit(self, line):
        """The ``quit`` command exit the command line processor\n"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
