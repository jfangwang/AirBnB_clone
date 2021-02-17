#!/usr/bin/python3
"""Console Unit Test"""
import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


cmd = HBNBCommand()


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
        self.assertEqual('(hbnb) ', cmd.prompt)

    def test_emptyLine(self):
        """test empty line"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertEqual(None, cmd.onecmd(""))


if __name__ == '__main__':
    unittest.main()
