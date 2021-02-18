# AirBnB clone

## Description

__The Console__ - This is the first part of full web application with the goal of cloning AirBnB. Building the console is setting the foundation of this application by having the ability to create and store objects in a "file storage" using json. We also have created some unit tests to validate our code and keeping it bug free as possible.

## How the Command Interpreter Works

__How to Start it__ - Our command interpreter is lableled console.py and is the entry point of this program. The file is an executable and you need to be in the root directoy. To start it, type ```./console.py```. 

## How to Use it

List of Commands and their description:

* __create__ [class]: Creates an instances of whatever class the user provides. Instance is saved to file storage and prints the id on the nextline.
* __show__ [class] [id]: Prints the string representation of a class given class and id.
* __all__ [class (optional)]: Prints all instances in string representation if not given a class. If class is provided, it only shows the instances of the given class.
* __destroy__ [class] [id]: Deletes an instance if given class and id.
* __update__ [class] [id] [attr_name] [attr_value]: Updates an instance if given class, attr_name, attr_value. If instance does not have given attr_name, it will add it as a new attr to the instance.
* __count__ [class]: Prints the number of instances of a given class.
__clear__: Clears the terminal with the os module.

List of Available Classes:

* __BaseModel__
* __State__
* __City__
* __Amenity__
* __Place__
* __Review__
* __User__


## Examples of Usage

To create a BaseModel class:
```create BaseModel```
* Output: ```f564785d-1307-499f-81e6-cce695c23248```

## Authors

**[Manny Figueroa](2216@holbertonschool.com)** and **[Jonathan Wang](2226@holbertonschool.com)**
