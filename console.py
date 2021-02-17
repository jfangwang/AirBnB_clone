#!/usr/bin/python3
"""
Console:
This file contains every function the console needs and runs based off running
functions from BaseModel.
"""
import cmd    # Required to run the console
import cowsay  # Cowsay for python
import os     # ability to use OS dependent functionality
import shlex  # used for split(), removed quotes if input had quotes
import re     # Regular Expressions, used for search substrings with wildcards
import json   # Used it load arg into dict.
import ast    # Used to convert string representation to dict obj
from models import storage              # Every else is from models
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.base_model import BaseModel

# Dictionary to store available and known classes
class_dict = {"BaseModel": BaseModel,
              "State": State,
              "City": City,
              "Amenity": Amenity,
              "Place": Place,
              "Review": Review,
              "User": User
              }
# Dictionary storing all commands, used for default()
func_dict = {"create()": "create", "show()": "show", "destroy()": "destroy",
             "all()": "all", "update()": "update", "cowsay()": "cowsay",
             "count()": "count"
             }


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand:
    HBNBCommand is a class that relies on the cmd module imported above and
    uses this to create an instance of a running command-line-interpreter.
    The (cmd.Cmd) part is what creates this instance. At the bottom, you'll
    see the HBNBCommand.cmdloop(). This keeps issuing a prompt and waits for
    an input to be enters in the console.

    Custom Methods: Any method that begins with "do_" is a custom method and
    shows up as a command in the console. The doc string under a custom method
    is used as the description when entering "help". Any method that begins
    with "help_" corresponds to its "do_" method and is called when entering
    "help command". Most of the time, it is used to print more info about a
    command.

    CMD Methods: For this file, it is any method that does not start with
    "do_", assume it is a built-in method provided by the cmd module.

    CMD Variables: Built-in instance variable that contain backend information
    about the command line such as displaying a custom prompt.

    All public instance methods:
    do_quit(): Ends the program with a return statement ending the cmdloop()

    do_EOF(): Also ends the program like do_quit()

    emptyline(): Built-in method and is called when an empty line is entered.
    Pass is implemented making sure nothing happens when nothing is entered.

    do_create() [class]: Creates an instances of whatever class the user
    provides. Instance is saved to file storage and prints the id on the next
    line.

    do_show() [class] [id]: Prints the string representation of a class given
    class and id.

    do_all() [class (optional)]: Prints all instances in string representation
    if not given a class. If class is provided, it only shows the instances
    of the given class.

    do_destroy() [class] [id]: Deletes an instance if given class and id.

    do_update() [class] [id] [attr_name] [attr_value]: Updates an instance if
    given class, attr_name, attr_value. If instance does not have given
    attr_name, it will add it as a new attr to the instance.

    default(): Built-in method, gets called if command is not found. It then
    checks if input is formatted as 'class.method()'. If not, it prints a
    standard error message like normal.

    count() [class]: Prints the number of instances of a given class.

    do_clear(): Clears the terminal with the os module.

    help_cowsay(): Provided a help page to cowsay.

    do_cowsay() [class (optional)]: Implement cowsay with cowsay module.

    CMD variables:
    prompt: What to display as the prompt
    """

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """USAGE: quit, exits the console"""
        return True

    def do_EOF(self, arg):
        """USAGE: EOF, exits the console"""
        return True

    def emptyline(self):
        """Does nothing if nothing is entered"""
        pass

# ----------------------CREATE---------------------------------------
    def do_create(self, arg):
        """USAGE: create [class], creates an instance of given class"""
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
        """USAGE: show [class] [id], shows instances in str representation"""
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
        """USAGE: all [class (optional)], shows all instances"""
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
        """USAGE: destroy [class] [id], deletes an instance given class id"""
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
        """USAGE: update [class] [id] [attr_name] [attr_value]"""
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
        """Helper function to run class.method()"""
        word_list = line.split(".")
        id_wrong = True
        id_num = str()
        attr_list = []
        atrr_name = str()
        attr_value = str()
        dict_obj = None
        if len(word_list) == 2:
            if re.search('show(.+)', word_list[1]):
                id_num = word_list[1][slice(5, -1, 1)]
                word_list[1] = word_list[1][slice(0, 5)] + ")"
            if re.search('destroy(.+)', word_list[1]):
                id_num = word_list[1][slice(8, -1, 1)]
                word_list[1] = word_list[1][slice(0, 8)] + ")"
            if re.search('update(.+)', word_list[1]):
                attr_list = word_list[1][slice(7, -1, 1)]
                attr_list = attr_list.split(",", 1)
                if len(attr_list) >= 1:
                    id_num = attr_list[0]
                if len(attr_list) >= 2:
                    attr_list[1] = attr_list[1].strip()
                    try:
                        # dict_obj = json.loads(attr_list[1])
                        dict_obj = ast.literal_eval(str(attr_list[1]))
                    except:
                        pass
                    if type(dict_obj) != dict:
                        atrr_name = attr_list[1]
                    else:
                        for key in storage.all():
                            temp = key.split(".")
                            if id_num == temp[1]:
                                id_wrong = False
                                for k in dict_obj:
                                    self.onecmd("update {} {} {} {}".
                                                format(word_list[0], id_num,
                                                       k, dict_obj[k]))
                        if id_wrong:
                            print("** no instance found **")
                        return
                if len(attr_list) >= 3:
                    attr_value = attr_list[2]
                word_list[1] = word_list[1][slice(0, 7)] + ")"
            if (word_list[0] in class_dict and word_list[1] in func_dict and
                    len(attr_list) > 0):
                self.onecmd(func_dict[word_list[1]] + " " + word_list[0] +
                            " " + id_num + " " + atrr_name + " " + attr_value)
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
        """USAGE: count [class], counts num of instances of given class"""
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

# ----------------------CLEAR---------------------------------------
    def do_clear(self, arg):
        """USAGE: clear, clears the console"""
        def clear(): os.system('clear')
        clear()

# ----------------------HELP_COWSAY---------------------------------------
    def help_cowsay(self):
        """cowsay help"""
        print("""\nUSAGE: cowsay [cow_name] PHRASE""")
        print("COW_NAME OPTIONS\nbeavis\ncheese\ndaemon\ncow(default)")
        print("dragon\nghostbusters\nkitty\nmeow\nmilk\npig\nstegosaurus")
        print("stimpy\nturkey\nturtle\ntux\n")

# ----------------------COWSAY---------------------------------------
    def do_cowsay(self, arg):
        """USAGE: cowsay [cow_name (optional)], type 'help cowsay' for more"""
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

# ----------------------MAIN---------------------------------------
"""
Python executes all of the code found in a file. This includes importing
modules. This makes sure all the code found in all the imported modules
does not get executed until it gets called properly by a function. The
HBNBCommand().cmdloop() inits and starts the console.
"""
if __name__ == '__main__':
    HBNBCommand().cmdloop()
