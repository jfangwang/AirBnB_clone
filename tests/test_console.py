#!/usr/bin/python3
"""Console Unit Test"""
import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


class dummyTest(unittest.TestCase):
    """Dummy Test Cases for testing purposes, not real tests"""
    def test_cmdPrompt(self):
        """idk"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")


class command_prompt(unittest.TestCase):
    """The Real Test Begins Here"""
    def test_prompt(self):
        """test prompt"""
        self.assertEqual('(hbnb) ', HBNBCommand().prompt)

    def test_emptyLine(self):
        """test empty line"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertEqual(None, HBNBCommand().onecmd(""))

    def test_quit(self):
        """test quit"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertEqual(True, HBNBCommand().onecmd("quit"))

    def test_help(self):
        """test help"""
        answer = ("Documented commands (type help <topic>):\n"
                  "========================================\n"
                  "EOF  all  clear  count  create  destroy  help  "
                  "quit  show  update")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertEqual(answer, f.getvalue().strip())

    def test_help_quit(self):
        """test help quit"""
        answer = "Quit command to exit the program"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertEqual(answer, f.getvalue().strip())

    def test_help_create(self):
        """test help create"""
        answer = "USAGE: create [class], creates an instance of given class"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            self.assertEqual(answer, f.getvalue().strip())

    def test_create(self):
        """test create"""
        answer = "** class name missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(answer, f.getvalue().strip())

    def test_create_fake_class(self):
        """test create fakeClass"""
        answer = "** class doesn't exist **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create fakeClass")
            self.assertEqual(answer, f.getvalue().strip())

    def test_show(self):
        """test show"""
        answer = "** class name missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual(answer, f.getvalue().strip())

    def test_show_fake_class(self):
        """test show fakeClass"""
        answer = "** class doesn't exist **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show fakeClass")
            self.assertEqual(answer, f.getvalue().strip())

    def test_show_class_fakeid(self):
        """test show class fakeid"""
        answer = "** no instance found **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 1234")
            self.assertEqual(answer, f.getvalue().strip())

    def test_show_class(self):
        """test show class"""
        answer = "** instance id missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            self.assertEqual(answer, f.getvalue().strip())

    def test_all_fake_class(self):
        """test all fakeClass"""
        answer = "** class doesn't exist **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all fakeClass")
            self.assertEqual(answer, f.getvalue().strip())

    def test_destroy(self):
        """test destroy"""
        answer = "** class name missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(answer, f.getvalue().strip())

    def test_destroy_fake_class(self):
        """test destroy fakeClass"""
        answer = "** class doesn't exist **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy fakeClass")
            self.assertEqual(answer, f.getvalue().strip())

    def test_destroy_no_id(self):
        """test destroy no id"""
        answer = "** instance id missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            self.assertEqual(answer, f.getvalue().strip())

    def test_destroy_wrong_id(self):
        """test destroy wrong_id"""
        answer = "** no instance found **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 1234")
            self.assertEqual(answer, f.getvalue().strip())

    def test_update(self):
        """test update"""
        answer = "** class name missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            self.assertEqual(answer, f.getvalue().strip())

    def test_update_fake_class(self):
        """test update fakeClass"""
        answer = "** class doesn't exist **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update fakeClass")
            self.assertEqual(answer, f.getvalue().strip())

    def test_update_no_id(self):
        """test update no id"""
        answer = "** instance id missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
            self.assertEqual(answer, f.getvalue().strip())

    def test_update_wrong_id(self):
        """test update wrong_id"""
        answer = "** attribute name missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel 1234")
            self.assertEqual(answer, f.getvalue().strip())


if __name__ == '__main__':
    unittest.main()
