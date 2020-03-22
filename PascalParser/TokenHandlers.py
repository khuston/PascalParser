import PascalParser.Config as Config
from PascalParser.ParseTypes import *
from PascalParser.Tokens import *
import string
import os
from PascalParser.LineColumnMap import LineColumnMap


def conditional_define_handler(position, text):
    if (position < len(text) - 1):
        if text[position] == '{' and text[position + 1] == '$':
            position = position + 2
            while (position < len(text)):
                if (text[position] == '}'):
                    return position + 1
                position += 1
    return position


def comment_handler(position, text):
    if (position < len(text) - 1):
        if text[position] == '/' and text[position + 1] == '/':
            position = position + 2
            while (position < len(text)) and not (text[position] in os.linesep):
                position += 1
        elif text[position] == '(' and text[position + 1] == '*':
            position = position + 2
            while (position < len(text)):
                if (text[position] == '*') and (position < len(text) - 1) and (text[position + 1] == ')'):
                    return position + 2
                position += 1
    return position


def string_literal_handler(position, text):
    if (position < len(text) - 1):
        if text[position] == "'":
            position += 1
            while (position < len(text)):
                if text[position] == "'":
                    return position + 1
                position += 1
    return position


def separator_handler(position, text):
    if (position < len(text)) and (text[position] in Config.Separators):
        position += 1
    return position


def whitespace_handler(position, text):
    while (position < len(text)) and (text[position] in string.whitespace):
        position += 1
    return position


def operator_handler(position, text):
    trial_position = position
    while (trial_position < len(text)) and (text[trial_position] in Config.operator_chars):
        trial_position += 1
    if IsOperator(text[position:trial_position]):
        return trial_position
    return position


def keyword_handler(position, text):
    trial_position = position
    while (trial_position < len(text)) and (text[trial_position] in Config.identifier_after_chars):
        trial_position += 1
    if IsKeyword(text[position:trial_position]):
        return trial_position
    return position


def identifier_handler(position, text):
    if (position < len(text)) and (text[position] in Config.identifier_start_chars):
        while (position < len(text)) and (text[position] in Config.identifier_after_chars):
            position += 1
    return position


def default_handler(position, text):
    line_column_map = LineColumnMap(text)
    raise ParseException('Unhandled at line {} column {}: {}'.format(line_column_map.get_line(
        position), line_column_map.get_column(position), text[position:position+10]))


default_handler_sequence = (conditional_define_handler, comment_handler, string_literal_handler,
                            separator_handler, whitespace_handler, operator_handler, keyword_handler, identifier_handler)

token_class_map = {conditional_define_handler: ConditionalDefine, comment_handler: Comment, string_literal_handler: StringLiteral,
                   separator_handler: Separator, whitespace_handler: Whitespace, operator_handler: Operator, keyword_handler: Keyword, identifier_handler: Identifier}


def TokenFactory(text, handler):
    token_class = token_class_map[handler]
    return token_class(text)
