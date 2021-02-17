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
import shlex
import sys
import re

class_dict = {"BaseModel": BaseModel,
              "State": State,
              "City": City,
              "Amenity": Amenity,
              "Place": Place,
              "Review": Review,
              "User": User
              }
func_dict = {"create()": "create", "show()": "show", "destroy()": "destroy",
             "all()": "all", "update()": "update", "cowsay()": "cowsay",
             "count()": "count"
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
        elif word_list[0] not in class_dict:
            print("** class doesn't exist **")
        elif (len(word_list) == 1):
            print("** instance id missing **")
        else:
            search = "{}.{}".format(word_list[0], word_list[1])
            objdict = storage.all()
            if search in objdict.keys():
                print(objdict[search])
            else:
                print("** no instance found **")

# ----------------------ALL---------------------------------------
    def do_all(self, arg):
        """Shows the contents of all instances"""
        cmd_arg = self.lastcmd
        word_list = arg.split()
        output_list = []
        if (len(word_list) == 0):
            for a in storage.all():
                output_list.append(str(storage.all()[a]))
            print(output_list)
        elif word_list[0] in class_dict:
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
        elif word_list[0] not in class_dict:
            print("** class doesn't exist **")
        elif len(word_list) == 1:
            print("** instance id missing **")
        else:
            search = "{}.{}".format(word_list[0], word_list[1])
            objdict = storage.all()
            if search in objdict.keys():
                del objdict[search]
                storage.save()
            else:
                print("** no instance found **")

# ----------------------UPDATE---------------------------------------
    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        untouchable = ["id", "created_at", "updated_at"]
        word_list = shlex.split(arg)
        instance_exist = 0
        if len(word_list) == 0:
            print("** class name missing **")
        elif word_list[0] not in class_dict:
            print("** class doesn't exist **")
        elif len(word_list) == 1:
            print("** instance id missing **")
        elif len(word_list) == 2:
            print("** attribute name missing **")
        elif len(word_list) == 3:
            print("** value missing **")
        else:
            search = "{}.{}".format(word_list[0], word_list[1])
            for key, val in storage.all().items():
                if key == search:
                    setattr(val, word_list[2], str(word_list[3]))
                    val.save()
                    instance_exist = 1
            if instance_exist == 0:
                print("** no instance found **")

# ----------------------DEFAULT---------------------------------------
    def default(self, line):
        """Helper function to run <class>.method()"""
        word_list = line.split(".")
        id_num = str()
        attr_list = []
        atrr_name = str()
        attr_value = str()
        if len(word_list) == 2:
            if re.search('show(.+)', word_list[1]):
                id_num = word_list[1][slice(5, -1, 1)]
                word_list[1] = word_list[1][slice(0, 5)] + ")"
            if re.search('destroy(.+)', word_list[1]):
                id_num = word_list[1][slice(8, -1, 1)]
                word_list[1] = word_list[1][slice(0, 8)] + ")"
            if re.search('update(.+)', word_list[1]):
                attr_list = word_list[1][slice(7, -1, 1)]
                attr_list = attr_list.split(",")
                if len(attr_list) >= 1:
                    id_num = attr_list[0]
                if len(attr_list) >= 2:
                    atrr_name = attr_list[1]
                if len(attr_list) >= 3:
                    attr_value = attr_list[2]
                word_list[1] = word_list[1][slice(0, 7)] + ")"
            if (word_list[0] in class_dict and word_list[1] in func_dict and
                    len(attr_list) > 0):
                self.onecmd(func_dict[word_list[1]] + " " + word_list[0] + " " + id_num + " " + atrr_name + " " + attr_value)
            elif (word_list[0] in class_dict and
                    word_list[1] in func_dict and id_num is None):
                self.onecmd(func_dict[word_list[1]] + " " + word_list[0])
            elif word_list[0] in class_dict and word_list[1] in func_dict:
                self.onecmd(func_dict[word_list[1]] + " " + word_list[0] +
                            " " + id_num)
            else:
                print("*** Unknown syntax: {}".format(line))
        else:
            print("*** Unknown syntax: {}".format(line))
        return

# ----------------------COUNT---------------------------------------
    def do_count(self, arg):
        """Helper function to run <class>.method()"""
        arg = arg.split()
        count = 0
        if len(arg) == 0:
            print("Missing Class Name")
        else:
            for key in storage.all():
                if storage.all()[key].__class__.__name__ == arg[0]:
                    count += 1
            if count > 0:
                print(count)
            else:
                print("class does not exist")

# ----------------------USER---------------------------------------
    def do_postcmd(self, stop, line):
        """Helper function to run <class>.method()"""
        word_list = line.split(".")
        if len(word_list) == 2:
            if word_list[0] in class_dict:
                self.onecmd(word_list[1])

# ----------------------TEST---------------------------------------
    def do_test(self, arg):
        """test"""
        print("User")
        print("ARG: {}".format(arg))
        for key in storage.all():
            print("OBJECT: {}".format(storage.all()[key]))
            print("DIR: {}".format(storage.all()[key].__dir__()))
            print("HASH: {}".format(storage.all()[key].__hash__()))
            print("CLASS: {}".format(storage.all()[key].__class__.__name__))

# ----------------------FUN_ADD_ONS---------------------------------------
    def do_clear(self, arg):
        """clear line"""
        def clear(): os.system('clear')
        clear()

    def help_cowsay(self):
        """cowsay help"""
        print("""\nUSAGE: cowsay [cow_name] PHRASE""")
        print("COW_NAME OPTIONS\nbeavis\ncheese\ndaemon\ncow(default)")
        print("dragon\nghostbusters\nkitty\nmeow\nmilk\npig\nstegosaurus")
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
