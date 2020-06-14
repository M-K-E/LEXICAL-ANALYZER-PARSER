import re

# define constants
delimiters = ' ', '{', '}', '[', ']', '(', ')'
delimiter_exp = '|'.join(map(re.escape, delimiters))

operators = ['+', '-', '*', '/', '>', '<', '=']
keywords = ['if', 'else', 'do', 'while', 'break', 'continue', 'switch', 'case',
            'short', 'int', 'long', 'double', 'float', 'char', 'return', 'void', 'NULL', 'struct']


def isInteger(s):  # check if string is integer
    try:
        int(s)
        return True
    except ValueError:
        return False


def isFloat(s):  # check if string is float
    try:
        float(s)
        return True
    except ValueError:
        return False


print("***CENG2002 LEXICAL PARSER HOMEWORK FOR FINAL EXAM***")
with open('stringtoparse.txt', 'r') as inputFile:  # open file
    while True:  # loop file until last line
        text = inputFile.readline().strip('\n')  # readline
        if (text == ''):  # check end of file
            break
        line = re.split(delimiter_exp, text)  # split by delimiters

        print("***The String Is:")
        print(text+"\n")
        print("***TOKENIZED VERSION IS***")
        # check each token for validity
        for token in line:
            if token in operators:
                print("'%s' IS AN OPERATOR" % (token))
            elif token in keywords:
                print("'%s' IS A KEYWORD" % (token))
            elif isInteger(token):
                print("'%s' IS AN INTEGER" % (token))
            elif isFloat(token):
                print("'%s' IS A REAL NUMBER" % (token))
            elif token[0].isdigit():
                print("'%s' IS NOT A VALID IDENTIFIER" % (token))
            else:
                print("'%s' IS A VALID IDENTIFIER" % (token))
