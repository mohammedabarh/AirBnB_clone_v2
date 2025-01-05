#!/usr/bin/python3
"""Test console commands."""
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):
    """Test cases for HBNBCommand."""

    @patch('sys.stdout', new_callable=StringIO)
    def test_quit(self, mock_stdout):
        """Test the quit command."""
        cmd = HBNBCommand()
        cmd.do_quit("")
        self.assertEqual(mock_stdout.getvalue(), "")

    # More tests for other commands...

if __name__ == "__main__":
    unittest.main()
