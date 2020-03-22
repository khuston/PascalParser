import unittest
from PascalParser.TokenHandlers import *
from PascalParser.ParseTypes import *
import os

class TestConditionalDefineHandler(unittest.TestCase):
    def test_empty(self):
        position = conditional_define_handler(0, '')
        self.assertEqual(position, 0)

    def test_comment(self):
        position = conditional_define_handler(0, '{}')
        self.assertEqual(position, 0)

    def test_empty_cd(self):
        position = conditional_define_handler(0, '{$}')
        self.assertEqual(position, 3)

    def test_whitespace_cd(self):
        position = conditional_define_handler(0, '{$  }')
        self.assertEqual(position, 5)

    def test_ifdef(self):
        position = conditional_define_handler(0, '{$ifdef}')
        self.assertEqual(position, 8)

class TestCommentHandler(unittest.TestCase):
    def test_empty(self):
        position = comment_handler(0, '')
        self.assertEqual(position, 0)

    def test_sslash(self):
        position = comment_handler(0, '//')
        self.assertEqual(position, 2)

    def test_sslash_linebreak(self):
        position = comment_handler(0, '//  '+os.linesep)
        self.assertEqual(position, 4)

    def test_empty_block(self):
        position = comment_handler(0, '(**)')
        self.assertEqual(position, 4)

    def test_unclosed_block1(self):
        position = comment_handler(0, '(**')
        self.assertEqual(position, 3)

    def test_unclosed_block2(self):
        position = comment_handler(0, '(*')
        self.assertEqual(position, 2)

    def test_not_comment(self):
        position = comment_handler(0, '(')
        self.assertEqual(position, 0)

    def test_block_with_linebreaks(self):
        position = comment_handler(0, '(*' + os.linesep + '*)')
        self.assertEqual(position, 4 + len(os.linesep))

class TestStringLiteralHandler(unittest.TestCase):
    def test_empty(self):
        position = string_literal_handler(0, '')
        self.assertEqual(position, 0)

    def test_empty_string(self):
        position = string_literal_handler(0, "''")
        self.assertEqual(position, 2)

    def test_whitespace_string(self):
        position = string_literal_handler(0, "'  '")
        self.assertEqual(position, 4)

class TestSeparatorHandler(unittest.TestCase):
    def test_empty(self):
        position = separator_handler(0, '')
        self.assertEqual(position, 0)

    def test_parenthesis_open(self):
        position = separator_handler(0, '(')
        self.assertEqual(position, 1)

    def test_parenthesis_close(self):
        position = separator_handler(0, ')')
        self.assertEqual(position, 1)

    def test_parentheses(self):
        position = separator_handler(0, '()')
        self.assertEqual(position, 1)

    def test_square_open(self):
        position = separator_handler(0, '[')
        self.assertEqual(position, 1)

    def test_square_close(self):
        position = separator_handler(0, ']')
        self.assertEqual(position, 1)

    def test_comma(self):
        position = separator_handler(0, ',  ')
        self.assertEqual(position, 1)

    def test_semicolon(self):
        position = separator_handler(0, ';  ')
        self.assertEqual(position, 1)

    def test_ignore_whitespace(self):
        position = separator_handler(0, ' .')
        self.assertEqual(position, 0)

class TestWhitespaceHandler(unittest.TestCase):
    def test_empty(self):
        position = whitespace_handler(0, '')
        self.assertEqual(position, 0)

    def test_single_space(self):
        position = whitespace_handler(0, ' ')
        self.assertEqual(position, 1)

    def test_linebreak1(self):
        position = whitespace_handler(0, '\n')
        self.assertEqual(position, 1)

    def test_linebreak2(self):
        position = whitespace_handler(0, '\r')
        self.assertEqual(position, 1)

    def test_linebreak3(self):
        position = whitespace_handler(0, '\n\r')
        self.assertEqual(position, 2)

    def test_linebreak4(self):
        position = whitespace_handler(0, '\r\n')
        self.assertEqual(position, 2)

    def test_tab1(self):
        position = whitespace_handler(0, '\t')
        self.assertEqual(position, 1)

    def test_tab2(self):
        position = whitespace_handler(0, '\x0b')
        self.assertEqual(position, 1)

    def test_tab3(self):
        position = whitespace_handler(0, '\x0c')
        self.assertEqual(position, 1)

    def test_nonspace_at_start(self):
        position = whitespace_handler(0, 'a  ')
        self.assertEqual(position, 0)

    def test_nonspace_at_end(self):
        position = whitespace_handler(0, '  a')
        self.assertEqual(position, 2)

class TestOperatorHandler(unittest.TestCase):
    def test_empty(self):
        position = operator_handler(0, '')
        self.assertEqual(position, 0)

    def test_operators(self):
        operators = ":= = + - ^ @ * / ="
        for operator in operators.split():
            position = operator_handler(0, operator)
            self.assertEqual(position, len(operator), 'Mismatch in position after '+operator)

class TestKeywordHandler(unittest.TestCase):
    def test_empty(self):
        position = keyword_handler(0, '')
        self.assertEqual(position, 0)

    def test_keywords(self):
        keywords = """and end interface record var array except is repeat while as
        exports label resourcestring WITH asm file library set xor begin finalization
        mod shl case finally nil shr CLASS for not string const function object then
        cOnStRuCtOr gOTO of threadvar destructor if or to dispinterface implementation
        packed try div in procedure type do INHERITED program unit downto initialization
        property until else inline raise uses"""
        for keyword in keywords.split():
            position = keyword_handler(0, keyword)
            self.assertEqual(position, len(keyword), 'Mismatch in position after '+keyword)

class TestIdentifierHandler(unittest.TestCase):
    def test_empty(self):
        position = identifier_handler(0, '')
        self.assertEqual(position, 0)

    def test_alphaword(self):
        position = identifier_handler(0, 'flamingo')
        self.assertEqual(position, 8)

    def test_alphanumericword(self):
        position = identifier_handler(0, 'flamingo2')
        self.assertEqual(position, 9)

    def test_underscore(self):
        position = identifier_handler(0, '_')
        self.assertEqual(position, 1)

    def test_startdigit(self):
        position = identifier_handler(0, '2flamingo2')
        self.assertEqual(position, 0)

class TestDefaultHandler(unittest.TestCase):
    def test_empty(self):
        self.assertRaises(ParseException, lambda: default_handler(0, ''))

    def test_message(self):
        try:
            default_handler(10, 'Hello' + os.linesep + 'World and Hello World' )
            self.fail('Did not raise Exception')
        except ParseException as exception:
            self.assertEqual(str(exception), 'Unhandled at line 2 column 4: ld and Hel')