import unittest
from PascalParser.LineColumnMap import *

class TestSeparatorHandler(unittest.TestCase):
    def test_empty(self):
        lcmap = LineColumnMap('')
        self.assertEqual(lcmap.get_column(0), 1)

    def test_first_line(self):
        lcmap = LineColumnMap('Hello' + os.linesep + 'World')
        self.assertEqual(lcmap.get_line(6), 1)

    def test_second_line(self):
        lcmap = LineColumnMap('Hello' + os.linesep + 'World')
        self.assertEqual(lcmap.get_line(7), 2)

    def test_first_line_column(self):
        lcmap = LineColumnMap('Hello' + os.linesep + 'World')
        self.assertEqual(lcmap.get_column(3 + len(os.linesep)), 4 + len(os.linesep))

    def test_second_line_column(self):
        lcmap = LineColumnMap('Hello' + os.linesep + 'World')
        self.assertEqual(lcmap.get_column(5 + len(os.linesep)), 1)