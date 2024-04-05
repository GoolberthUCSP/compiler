import io
import re

class MyStringIO(io.StringIO):
    def peek(self, size=1):
        current_position = self.tell()
        data = self.read(size)
        self.seek(current_position)
        return data

def Scanner(file : MyStringIO):
    tokens = []
    while file.peek(1):
        value = ""
        char = file.read(1)
        # H1, H2, H3
        if char == "#":
            value += char
            if file.peek(1) == "#":
                value += file.read(1)
                if file.peek(1) == "#":
                    value += file.read(1)
                    tokens.append(["H3", value]) # value = ###
                else :
                    tokens.append(["H2", value]) # value = ##
            else :
                tokens.append(["H1", value]) # value = #
        # string
        elif char == "'":
            while file.peek(1) != "'":
                value += file.read(1)
            file.read(1) # Consumes the last '
            tokens.append(["STR", value]) # value = 'data'
        # bold and italics
        elif char == "*":
            value += char
            if file.peek(1) == "*":
                value += file.read(1)
                tokens.append(["BOLDMARK", value]) # value = **
            else :
                tokens.append(["ITALICMARK", value]) # value = *
        # newline
        elif char == '\n':
            value += char
            tokens.append(["NEWLINE", value]) # value = \n
        
        char = file.read(1)
        value += char

    tokens.append(["EOF", ""])
    return tokens        