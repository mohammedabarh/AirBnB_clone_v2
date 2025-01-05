#!/usr/bin/python3
"""Console for AirBnB clone."""
import cmd
from models import storage

class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """End Of File command to exit the program."""
        return True

    def do_create(self, arg):
        """Creates a new instance of a class."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        try:
            cls = eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return
        obj = cls()
        for param in args[1:]:
            key, value = param.split("=")
            value = value.strip('"').replace("_", " ")
            setattr(obj, key, value)
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        pass

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        pass

    def do_all(self, arg):
        """Prints all string representations of all instances."""
        pass

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
