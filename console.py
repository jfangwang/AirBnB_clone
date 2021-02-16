#!/usr/bin/python3
"""Console"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.base_model import BaseModel
import cowsay
import os

class_dict = {"BaseModel": BaseModel,
              "State": State,
              "City": City,
              "Amenity": Amenity,
              "Place": Place,
              "Review": Review,
              "User": User
              }


class HBNBCommand(cmd.Cmd):
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

# ----------------------CREATE---------------------------------------
    def do_create(self, arg):
        """create an instance"""
        if (len(arg) == 0):
            print("** class name missing **")
        elif arg in class_dict:
            instance = class_dict[arg]()
            instance.save()
            print(instance.id)
        else:
            print("** class doesn't exist **")

# ----------------------SHOW---------------------------------------
    def do_show(self, arg):
        """Show contents of a class based on class and id"""
        word_list = arg.split()
        if (len(word_list) == 0):
            print("** class name missing **")
        elif (len(word_list) == 1):
            print("** instance id missing **")
        elif word_list[0] in class_dict:
            search = "{}.{}".format(word_list[0], word_list[1])
            objdict = storage.all()
            if search in objdict.keys():
                print(objdict[search])
            else:
                print("** no instance found **")

# ----------------------ALL---------------------------------------
    def do_all(self, arg):
        """Shows the contents of all instances"""
        word_list = arg.split()
        output_list = []
        if (len(word_list) == 0):
            for a in storage.all():
                output_list.append(str(storage.all()[a]))
            print(output_list)
        elif (len(word_list) == 1 and word_list[0] in class_dict):
            for a in storage.all():
                word = a.split(".")
                if word[0] == word_list[0]:
                    output_list.append(str(storage.all()[a]))
            print(output_list)
        else:
            print("** class doesn't exist **")

# ----------------------DESTROY---------------------------------------
    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        word_list = arg.split()
        if (len(word_list) == 0):
            print("** class name missing **")
        elif (len(word_list) == 1):
            if word_list[0] in class_dict:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        elif word_list[0] in class_dict:
            search = "{}.{}".format(word_list[0], word_list[1])
            objdict = storage.all()
            if search in objdict.keys():
                del objdict[search]
            else:
                print("** no instance found **")

    def do_type(self, arg):
        """testing the type"""
        if len(arg) == 0:
            print("no arg")
        elif arg.isdigit():
            print("{}, type: digit".format(arg))
        else:
            print("{}, type: {}".format(arg, type(args)))

# ----------------------UPDATE---------------------------------------
    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        untouchable = ["id", "created_at", "updated_at"]
        word_list = arg.split()
        if (len(word_list) == 0):
            print("** class name missing **")
        elif (len(word_list) == 1):
            if word_list[0] in class_dict:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        elif len(word_list) == 2:
            search = "{}.{}".format(word_list[0], word_list[1])
            flag = 0
            for a in storage.all().keys():
                if search == a:
                    print("** attribute name missing **")
                    flag = 1
            if flag == 0:
                print("** no instance found **")
        elif len(word_list) == 3:
            print("** value missing **")
        elif word_list[0] in class_dict:
            search = "{}.{}".format(word_list[0], word_list[1])
            for key, val in storage.all().items():
                if word_list[2] not in untouchable:
                    setattr(val, word_list[2], word_list[3])
                    val.save()
                else:
                    print("you cannot change attribute '{}'".format(word_list[2]))

# ----------------------FUN_ADD_ONS---------------------------------------
    def do_clear(self, arg):
        """clear line"""
        def clear(): os.system('clear')
        clear()

    def help_cowsay(self):
        """cowsay help"""
        print("""USAGE: cowsay [cow_name] PHRASE""")
        print("cow_name options\nbeavis\ncheese\ndaemon\ncow(default)")
        print("dragon\nghostbusters\nkitty\nmeow\nmilk\npig\nstegosaurus\n")
        print("stimpy\nturkey\nturtle\ntux\n")

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
