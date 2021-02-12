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
        """end of file"""
        return True

    def emptyline(self):
        """empty line"""
        pass

    def help_cowsay(self):
        """cowsay help"""
        print("""USAGE: cowsay [cow_name] PHRASE""")
        print("cow_name options:\nbeavis\ncheese\ndaemon\ncow (default)\ndragon\nghostbusters\nkitty\nmeow\nmilk\npig\nstegosaurus\nstimpy\nturkey\nturtle\ntux\n")
    
    def do_cowsay(self, arg):
        """cowsay"""
        word_list = []
        word = ""
        for char in arg:
            if char == " ":
                word_list.append(word)
                word = ""
            else:
                word += char
        word_list.append(word)
        og_arg = arg
        arg = ""
        for index in range(0, len(word_list)):
            if (index != 0):
                arg += word_list[index]
            if (index < len(word_list) - 1):
                arg += " "
        if (word_list[0] == "beavis"):
            cowsay.beavis(arg)
        elif (word_list[0] == "cheese"):
            cowsay.cheese(arg)
        elif (word_list[0] == "daemon"):
            cowsay.daemon(arg)
        elif (word_list[0] == "cow"):
            cowsay.cow(arg)
        elif (word_list[0] == "dragon"):
            cowsay.dragon(arg)
        elif (word_list[0] == "ghostbusters"):
            cowsay.ghostbusters(arg)
        elif (word_list[0] == "kitty"):
            cowsay.kitty(arg)
        elif (word_list[0] == "meow"):
            cowsay.meow(arg)
        elif (word_list[0] == "milk"):
            cowsay.milk(arg)
        elif (word_list[0] == "pig"):
            cowsay.pig(arg)
        elif (word_list[0] == "stegosaurus"):
            cowsay.stegosaurus(arg)
        elif (word_list[0] == "stimpy"):
            cowsay.stimpy(arg)
        elif (word_list[0] == "turkey"):
            cowsay.turkey(arg)
        elif (word_list[0] == "turtle"):
            cowsay.turtle(arg)
        elif (word_list[0] == "tux"):
            cowsay.tux(arg)
        else:
            cowsay.cow(og_arg)

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
