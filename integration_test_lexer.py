from PascalParser import Lexer
import PascalParser.Config as Config
from PascalParser.TextFile import ReadTextFile, IsPascalFile
import os

def test_files():
    lexer = Lexer()
    pascal_filepaths = []
    for path in Config.PathsToTest:
        if os.path.isdir(path):
            for root, dir, filenames in os.walk(path):
                for filename in filenames:
                    filepath = os.path.join(root, filename)
                    if IsPascalFile(filepath):
                        pascal_filepaths.append(filepath)
        else:
            pascal_filepaths.append(path)

    for filepath in pascal_filepaths:
        text = ReadTextFile(filepath)
        lexer.tokenize(text)


test_files()