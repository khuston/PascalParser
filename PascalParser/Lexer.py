import PascalParser.TokenHandlers as TokenHandlers
import PascalParser.Tokens as Tokens


class Lexer():
    def __init__(self, token_handlers=TokenHandlers.default_handler_sequence):
        self.__token_handlers = list(token_handlers)
        self.__token_handlers.append(TokenHandlers.default_handler)

    def tokenize(self, text):
        self.position = 0
        while self.position < len(text):
            yield self._get_next_token(text)

    def _get_next_token(self, text):
        for token_handler in self.__token_handlers:
            new_position = token_handler(self.position, text)
            if new_position > self.position:
                token = TokenHandlers.TokenFactory(text[self.position:new_position], token_handler)
                self.position = new_position
                return token

class WhitespaceIgnoringLexerDecorator():
    def __init__(self, lexer):
        self.__inner_lexer = lexer

    def tokenize(self, text):
        for token in self.__inner_lexer.tokenize(text):
            if type(token) != Tokens.Whitespace:
                yield token

        

"""


    ifdef_depth = 0;
    in_comment = False;
    in_string_literal = False;
    comment_start_character = '';
    token = '';

    for lLine in aLines:
        if (in_comment) and (comment_start_character == '/'):
            in_comment = False;
        while lLine:
            lCharacter, lLine = lLine[:1], lLine[1:];
            if (not in_comment) and (not in_string_literal):
                if (lCharacter in ('{', '/', '(')):
                    if (lCharacter == '{'):
                        if token:
                            yield token.lower();
                        token = '';
                        in_comment = True;
                        comment_start_character = lCharacter;
                        if (lLine[0] == '$'):
                            if (lLine[1:6].lower() == 'ifdef') or (lLine[1:7].lower() == 'ifndef'):
                                ifdef_depth += 1;
                            elif (ifdef_depth > 0) and (lLine[1:6].lower() == 'endif'):
                                ifdef_depth -= 1;
                        continue;
                    elif ((lCharacter == '/' and lLine[0] == '/')
                     or (lCharacter == '(' and lLine[0] == '*')):
                        if token:
                            yield token.lower();
                        token = '';
                        in_comment = True;
                        comment_start_character = lCharacter;
                        lLine = lLine[1:];
                        continue;
                if (not aTokenizeIFDEFs) and (ifdef_depth > 0):
                    continue;
                if lCharacter == "'":
                    in_string_literal = True;
                    continue;
                if lCharacter in Separators:
                    if token:
                        yield token.lower();
                    yield lCharacter;
                    token = '';
                    continue;
                lOperator, lLine = SplitOperator(lCharacter+lLine);	
                if lOperator:
                    if token:
                        yield token.lower();
                    yield lOperator;
                    token = '';
                    continue;
                if (lCharacter in Whitespace):
                    if token:
                        yield token.lower();
                    token = '';
                    continue;
                token += lCharacter;
            elif in_comment:
                if (comment_start_character == '{' and lCharacter == '}'):
                    in_comment = False;
                    continue;
                elif (comment_start_character == '(' and lCharacter == '*' and lLine[0] == ')'):
                    lLine = lLine[1:];
                    in_comment = False;
                    continue;
                #elif (lCommentStartCharacter == '/' and lCharacter == '\n'):
                #	lInComment = False;
                #	continue;
            elif in_string_literal:
                if lCharacter == "'":
                    if lLine[0] == "'": # escaped single quote
                        lLine = lLine[1:];
                        continue;
                    else:
                        in_string_literal = False;
                        continue;
"""