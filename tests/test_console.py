#!/usr/bin/python3
"""Test Console"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage


class TestConsole(unittest.TestCase):
    """Test cases for HBNB console"""

    def setUp(self):
        """Set up test cases"""
        self.console = HBNBCommand()

    def test_quit(self):
        """Test quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("quit"))

    def test_EOF(self):
        """Test EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("EOF"))

    def test_create(self):
        """Test create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create State name=\"California\"")
            output = f.getvalue().strip()
            self.assertTrue(len(output) > 0)

    def test_show(self):
        """Test show command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show State")
            output = f.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_destroy(self):
        """Test destroy command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy State")
            output = f.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_all(self):
        """Test all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all")
            output = f.getvalue().strip()
            self.assertTrue(isinstance(eval(output), list))


if __name__ == '__main__':
    unittest.main()
