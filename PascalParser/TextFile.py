import os

def ReadTextFile(filepath):
    try:
        with open(filepath, encoding='utf-8-sig') as f:
            return f.read()
    except UnicodeDecodeError:
        with open(filepath, encoding='mbcs') as f:
            return f.read()

def IsPascalFile(filename):
    filenameroot, extension = os.path.splitext(filename)
    return extension.strip('.').lower() == 'pas'
