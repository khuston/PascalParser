import unittest
from PascalParser.Lexer import Lexer, WhitespaceIgnoringLexerDecorator
from PascalParser import get_lexer

class TestGetLexer(unittest.TestCase):
    def test_default(self):
        lexer = get_lexer()
        self.assertIsInstance(lexer, Lexer)

    def test_ignore_whitespace(self):
        lexer = get_lexer({'ignore_whitespace': True})
        self.assertIsInstance(lexer, WhitespaceIgnoringLexerDecorator)