from configparser import ConfigParser
import string

# Global Initialization
configparser = ConfigParser(comment_prefixes=())
configparser.read('config.ini')

Operators = configparser['Tokens']['Operators'].split()
Separators = configparser['Tokens']['Separators'].split()
ReservedWords = configparser['Tokens']['Reserved Words'].split()

operator_chars = ''.join(Operators)
identifier_start_chars = string.ascii_letters + '_'
identifier_after_chars = string.ascii_letters + '_' + string.digits