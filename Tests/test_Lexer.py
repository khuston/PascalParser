import unittest
from PascalParser.Lexer import Lexer, WhitespaceIgnoringLexerDecorator
import PascalParser.Tokens as Tokens


class TestTokens(unittest.TestCase):
    def test_empty(self):
        lex = Lexer()
        for token in lex.tokenize(''):
            self.fail('Should find no tokens')

    def test_whitespace(self):
        lex = Lexer()
        tokens = []
        for token in lex.tokenize(' '):
            tokens.append(token)
        self.assertEqual(len(tokens), 1)
        self.assertIsInstance(token, Tokens.Whitespace)

    def test_whitespace(self):
        lex = Lexer()
        tokens = []
        for token in lex.tokenize(' '):
            tokens.append(token)
        self.assertEqual(len(tokens), 1)
        self.assertIsInstance(token, Tokens.Whitespace)

    def test_whitespace_ignoring(self):
        lex = WhitespaceIgnoringLexerDecorator(Lexer())
        tokens = []
        for token in lex.tokenize(' '):
            self.fail('Should find no tokens')

    def test_class(self):
        text = """
TDlgTaskParam = class(TSNModalBaseDlg)
  Panel1: TPanel;
end;"""
        expected_token_sequence = (Tokens.Identifier, Tokens.Operator, Tokens.Keyword, Tokens.Separator, Tokens.Identifier, Tokens.Separator,
                                   Tokens.Identifier, Tokens.Separator, Tokens.Identifier, Tokens.Separator, Tokens.Keyword, Tokens.Separator)

        lex = WhitespaceIgnoringLexerDecorator(Lexer())
        tokens = []
        for i, token in enumerate(lex.tokenize(text)):
            expected_token = expected_token_sequence[i]
            self.assertIsInstance(token, expected_token)
