import unittest
from PascalParser.Tokens import *

class TestTokens(unittest.TestCase):
    def test_Token(self):
        self.assertRaises(Exception, lambda: Token(''))

    def test_StringLiteral(self):
        StringLiteral('')

    def test_NumericLiteral(Token):
        NumericLiteral('')

    def test_Identifier(Token):
        Identifier('')

    def test_Keyword(Token):
        Keyword('')

    def test_Operator(Token):
        Operator('')

    def test_Separator(Token):
        Separator('')

    def test_Comment(Token):
        Comment('')

    def test_Whitespace(Token):
        Whitespace('')