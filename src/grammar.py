import io

class MyStringIO(io.StringIO):
    def peek(self, size=1):
        current_position = self.tell()
        data = self.read(size)
        self.seek(current_position)
        return data

class Grammar:
    def __init__(self):
        self.productions = {}
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
                        self.tokens.append(["h3", value]) # value = ###
                    else :
                        self.tokens.append(["h2", value]) # value = ##
                else :
                    self.tokens.append(["h1", value]) # value = #
            # string
            elif char == "'":
                self.tokens.append(["textmark", char]) # value = '
                while self.file.peek(1) != "'":
                    value += self.file.read(1)
                self.tokens.append(["string", value]) # value = 'data'
                self.tokens.append(["textmark", "'"]) # value = '
            # bold and italics
            elif char == "*":
                value += char
                if self.file.peek(1) == "*":
                    value += self.file.read(1)
                    self.tokens.append(["boldmark", value]) # value = **
                else :
                    self.tokens.append(["italicmark", value]) # value = *
            # newline
            elif char == '\n':
                value += char
                if self.file.peek(1) == '\n':
                    value += self.file.read(1)
                    self.tokens.append(["blocksep", value])
                else:
                    self.tokens.append(["newline", value])
                while self.file.peek(1) == '\n':
                    self.file.read(1)
            # comment
            elif (char == "/" and self.file.peek(1) == "*"):
                while self.file.peek(2) != "*/":
                    self.file.read(1)
                self.file.read(2)
                while self.file.peek(1) == '\n':
                    self.file.read(1)
            # ordered list mark
            elif char == "+":
                self.tokens.append(["olistmark", char])
            # unordered list mark
            elif char == "-":
                self.tokens.append(["ulistmark", char])
            elif char == "!":
                self.tokens.append(["imagemark", char])
            elif char == "[":
                self.tokens.append(["openbracket", char])
            elif char == "]":
                self.tokens.append(["closebracket", char])
            elif char == "(":
                self.tokens.append(["openparenth", char])
                # TODO: Add support for recognized links or routes
            elif char == ")":
                self.tokens.append(["closeparenth", char])

        self.tokens.append(["eof", ""])
        return self.tokens    
    
    def parser(self):
        pass