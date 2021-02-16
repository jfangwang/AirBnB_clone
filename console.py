#!/usr/bin/python3
from cmd import Cmd
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

# ----------------------CREATE---------------------------------------
    def do_create(self, args):
        """create an instance"""
        if args in class_dict:
            instance = class_dict[args]()
            instance.save()
            print(instance.id)
        elif (len(args) == 0):
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

# ----------------------SHOW---------------------------------------
    def do_show(self, args):
        """Show contents of a class based on class and id"""
        word_list = args.split()
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
    def do_all(self, args):
        """Shows the contents of all instances"""
        word_list = args.split()
        if (len(word_list) == 0):
            for a in storage.all():
                print(storage.all()[a])
        elif (len(word_list) == 1 and word_list[0] in class_dict):
            for a in storage.all():
                print(storage.all()[a])
        else:
            print("** class doesn't exist **")

# ----------------------DESTROY---------------------------------------
    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        word_list = args.split()
        if (len(word_list) == 0):
            print("** class name missing **")
        elif (len(word_list) == 1):
            print("** instance id missing **")
        elif word_list[0] in class_dict:
            search = "{}.{}".format(word_list[0], word_list[1])
            objdict = storage.all()
            if search in objdict.keys():
                del objdict[search]
            else:
                print("** no instance found **")

# ----------------------UPDATE---------------------------------------
    def do_update(self, args):
        """Updates an instance based on the class name and id"""
        untouchable = ["id", "created_at", "updated_at"]
        word_list = args.split()
        if (len(word_list) == 0):
            print("** class name missing **")
        elif (len(word_list) == 1):
            print("** instance id missing **")
        elif len(word_list) == 2:
            print("** attribute name missing **")
        elif len(word_list) == 3:
            print("** value missing **")
        elif word_list[0] in class_dict:
            search = "{}.{}".format(word_list[0], word_list[1])
            objdict = storage.all()
            if search in objdict.keys():
                instance_dict = objdict[search]
                if word_list[2] in instance_dict.keys() and word_list[2]:
                    if word_list[2] not in untouchable:
                        instance_dict[word_list[2]] = word_list[3]
                        storage.save()
                    else:
                        print("Cannot change value {}".format(word_list[2]))
                else:
                    instance_dict[word_list[2]] = word_list[3]
                    storage.save()
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

# ----------------------FUN_ADD_ONS---------------------------------------
    def do_clear(self, args):
        """clear line"""
        def clear(): os.system('clear')
        clear()

    def help_cowsay(self):
        """cowsay help"""
        print("""USAGE: cowsay [cow_name] PHRASE""")
        print("cow_name options\nbeavis\ncheese\ndaemon\ncow(default)")
        print("dragon\nghostbusters\nkitty\nmeow\nmilk\npig\nstegosaurus\n")
        print("stimpy\nturkey\nturtle\ntux\n")

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
