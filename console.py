#!/usr/bin/python3
from cmd import Cmd
from models.base_model import BaseModel
import cowsay
import os

class HBNBCommand(Cmd):
    """HBNBC"""
    prompt = '(hbnb) '
    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """end of file"""
        return True

    def emptyline(self):
        """empty line"""
        pass

    def do_create(self, args):
        """create an instance"""
        if (args == "BaseModel"):
            instance = BaseModel()
            instance.save()
            print(instance.id)
        elif (len(args) == 0):
            print("** class name missing **")
        else:
            print("** class doesn't exist **")
    
    def do_show(self, args):
        """create an instanc"""
        if (args == "BaseModel"):
            instance = BaseModel()
            print(instance.id)
        elif (len(args) == 0):
            print("** class name missing **")
        else:
            print("** class doesn't exist **")
            
            

    def do_clear(self, args):
        """clear line"""
        clear = lambda: os.system('clear') #on Linux System
        clear()

    def help_cowsay(self):
        """cowsay help"""
        print("""USAGE: cowsay [cow_name] PHRASE""")
        print("cow_name options:\nbeavis\ncheese\ndaemon\ncow (default)\ndragon\nghostbusters\nkitty\nmeow\nmilk\npig\nstegosaurus\nstimpy\nturkey\nturtle\ntux\n")
    
    def do_cowsay(self, args):
        """cowsay"""
        word_list = []
        word = ""
        for char in args:
            if char == " ":
                word_list.append(word)
                word = ""
            else:
                word += char
        word_list.append(word)
        og_args = args
        args = ""
        for index in range(0, len(word_list)):
            if (index != 0):
                args += word_list[index]
            if (index < len(word_list) - 1):
                args += " "
        if (word_list[0] == "beavis"):
            cowsay.beavis(args)
        elif (word_list[0] == "cheese"):
            cowsay.cheese(args)
        elif (word_list[0] == "daemon"):
            cowsay.daemon(args)
        elif (word_list[0] == "cow"):
            cowsay.cow(args)
        elif (word_list[0] == "dragon"):
            cowsay.dragon(args)
        elif (word_list[0] == "ghostbusters"):
            cowsay.ghostbusters(args)
        elif (word_list[0] == "kitty"):
            cowsay.kitty(args)
        elif (word_list[0] == "meow"):
            cowsay.meow(args)
        elif (word_list[0] == "milk"):
            cowsay.milk(args)
        elif (word_list[0] == "pig"):
            cowsay.pig(args)
        elif (word_list[0] == "stegosaurus"):
            cowsay.stegosaurus(args)
        elif (word_list[0] == "stimpy"):
            cowsay.stimpy(args)
        elif (word_list[0] == "turkey"):
            cowsay.turkey(args)
        elif (word_list[0] == "turtle"):
            cowsay.turtle(args)
        elif (word_list[0] == "tux"):
            cowsay.tux(args)
        else:
            cowsay.cow(og_args)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
