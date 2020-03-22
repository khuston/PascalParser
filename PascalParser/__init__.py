from PascalParser.Lexer import Lexer, WhitespaceIgnoringLexerDecorator

def apply_filters(lexer, settings):
    if 'ignore_whitespace' in settings and settings['ignore_whitespace']:
        lexer = WhitespaceIgnoringLexerDecorator(lexer)

    return lexer

def get_lexer(settings={}):
    lexer = Lexer()
    lexer = apply_filters(lexer, settings)
    return lexer