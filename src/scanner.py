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
                    tokens.append(["h3", value]) # value = ###
                else :
                    tokens.append(["h2", value]) # value = ##
            else :
                tokens.append(["h1", value]) # value = #
        # string
        elif char == "'":
            while file.peek(1) != "'":
                value += file.read(1)
            file.read(1) # Consumes the last '
            tokens.append(["string", value]) # value = 'data'
        # bold and italics
        elif char == "*":
            value += char
            if file.peek(1) == "*":
                value += file.read(1)
                tokens.append(["boldmark", value]) # value = **
            else :
                tokens.append(["italicmark", value]) # value = *
        # newline
        elif char == '\n':
            tokens.append(["newline", char])

    tokens.append(["eof", ""])
    return tokens        