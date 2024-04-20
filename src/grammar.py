import io
from src import rules

class MyStringIO(io.StringIO):
    def peek(self, size=1):
        current_position = self.tell()
        data = self.read(size)
        self.seek(current_position)
        return data

class Grammar:
    def __init__(self):
        self.productions = rules.productions
        self.tokens = []
        self.errors = []
        self.file = MyStringIO
    
    def validate(self, input : MyStringIO):
        self.file = input
        self.tokens = self.scanner()

    def scanner(self):
        while self.file.peek(1):
            value = ""
            char = self.file.read(1)
            # H1, H2, H3
            if char == "#":
                value += char
                if self.file.peek(1) == "#":
                    value += self.file.read(1)
                    if self.file.peek(1) == "#":
                        value += self.file.read(1)
                        self.tokens.append(["H3", value])  # value = ###
                    else:
                        self.tokens.append(["H2", value])  # value = ##
                else:
                    self.tokens.append(["H1", value])  # value = #
            # string
            elif char == "'":
                self.tokens.append(["TEXTMARK", char])  # value = '
                while self.file.peek(1) != "'":
                    value += self.file.read(1)
                self.tokens.append(["STRING", value])  # value = 'data'
                self.tokens.append(["TEXTMARK", "'"])  # value = '
            # bold and italics
            elif char == "*":
                value += char
                if self.file.peek(1) == "*":
                    value += self.file.read(1)
                    self.tokens.append(["BOLDMARK", value])  # value = **
                else:
                    self.tokens.append(["ITALICMARK", value])  # value = *
            # newline
            elif char == '\n':
                value += char
                if self.file.peek(1) == '\n':
                    value += self.file.read(1)
                    self.tokens.append(["BLOCKSEP", value])  # value = \n\n
                else:
                    self.tokens.append(["NEWLINE", value])  # value = \n
                while self.file.peek(1) == '\n':
                    self.file.read(1)  # skip empty lines
            # comment
            elif (char == "/" and self.file.peek(1) == "*"):
                while self.file.peek(2) != "*/":
                    self.file.read(1)
                self.file.read(2)  # skip comment
                while self.file.peek(1) == '\n':
                    self.file.read(1)
            # ordered list mark
            elif char == "+":
                self.tokens.append(["OLISTMARK", char])
            # unordered list mark
            elif char == "-":
                self.tokens.append(["ULISTMARK", char])
            elif char == "!":
                self.tokens.append(["IMAGEMARK", char])
            elif char == "[":
                self.tokens.append(["OPENBRACKET", char])
            elif char == "]":
                self.tokens.append(["CLOSEBRACKET", char])
            elif char == "(":
                self.tokens.append(["OPENPARENTH", char])
                # TODO: Add support for recognized links or routes
            elif char == ")":
                self.tokens.append(["CLOSEPARENTH", char])
    
        self.tokens.append(["EOF", "$"])
        return self.tokens   
    
    def parser(self):
        pass