#!/usr/bin/python3
from cmd import Cmd

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

    def do_create(self):
        """Creates a new instance"""
        
        
if __name__ == '__main__':
    HBNBCommand().cmdloop()
