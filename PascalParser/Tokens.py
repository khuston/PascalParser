import PascalParser.Config as Config

class Token:
    def __init__(self, text):
        self.text = text
        if type(self) == Token:
            raise Exception('Token is an abstract class that should not be instantiated.')

class ConditionalDefine(Token):
    pass

class Comment(Token):
    pass

class StringLiteral(Token):
    pass

class NumericLiteral(Token):
    pass

class Identifier(Token):
    pass

class Keyword(Token):
    pass

class Operator(Token):
    pass

class Separator(Token):
    pass

class Whitespace(Token):
    pass

class Keyword(Token):
    pass

def SameSymbol(symbol1, symbol2):
    return symbol1.lower() == symbol2.lower()

def IsKeyword(symbol):
    for keyword in Config.ReservedWords:
        if SameSymbol(symbol, keyword):
            return True
    return False

def IsOperator(symbol):
    for operator in Config.Operators:
        if SameSymbol(symbol, operator):
            return True
    return False