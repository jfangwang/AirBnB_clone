#!/usr/bin/python3
from cmd import Cmd
import cowsay

class HBNBCommand(Cmd):
    """HBNBC"""
    prompt = '(hbnb) '
    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        return True

    def emptyline(self):
        pass

    def do_cowsay(self, arg):
        """implementing cowsay test"""
        cowsay.cow(arg)

    def do_create(self, arg):
        """Creates a new instance"""
        if str(arg) is "base":
            print("it works")
        elif not arg:
            print("** class name missing **")
        else:
            print("** class doesn't exist **")
        
if __name__ == '__main__':
    HBNBCommand().cmdloop()
