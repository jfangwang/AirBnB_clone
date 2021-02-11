#!/usr/bin/python3
from cmd import Cmd

class HBNBCommand(Cmd):
    """HBNBC"""
    prompt = '(hbnb) '
    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        return True

    def emptyline(self):
        pass
if __name__ == '__main__':
    HBNBCommand().cmdloop()
