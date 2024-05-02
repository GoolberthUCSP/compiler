import io
from src.rules import productions
from src.alphabet import *

class MyStringIO(io.StringIO):
    def peek(self, size=1):
        current_position = self.tell()
        data = self.read(size)
        self.seek(current_position)
        return data

class Grammar:
    def __init__(self):
        self.productions = productions
        self.num_productions = []
        self.parsing_table = dict(dict())
        self.tokens = []
        self.errors = []
        self.strings = []
        self.file = None
        self.enum_productions()
        self.fill_parsing_table()

    def validate(self, input : MyStringIO):
        self.file = input
        self.tokens = self.scanner()
        #print(self.tokens)
        done = self.parser()
        if not done:
            print("Errors:")
            for error in self.errors:
                print("\t", error)
        else:
            print("Success!")
        

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
            elif char in alphabet:
                while char in alphabet:
                    if char == "\\":
                        if self.file.peek(1) in special_chars: # We not need to escape the special chars in the grammar
                            value += self.file.read(1)
                        elif self.file.peek(1) in latex_escaped: # For latex format we need to escape the special chars
                            value += char
                            value += self.file.read(1)
                        else:
                            self.errors.append("Error in point " + str(self.file.tell()) + ": Invalid escape sequence")
                    else:
                        value += char
                    char = self.file.read(1)
                self.file.seek(self.file.tell() - 1) # return to last char
                # self.tokens.append(["STRING", value])
                self.strings.append(value)
                self.tokens.append(["STRING", "alphanum"])
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
                self.file.read(2)  # skip comment closer = */
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
            elif char == "&":
                self.tokens.append(["TABLEHEADSEP", char])
            elif char == "|":
                self.tokens.append(["TABLEBODYSEP", char])
            else:
                self.errors.append("Error in point " + str(self.file.tell()) + ": Invalid char")
        self.tokens.append(["EOF", "$"])
        return self.tokens   
    
    def parser(self):
        stack = []
        stack.append("DOCUMENT")
        queue = self.tokens[:]
        word = queue.pop(0) # word = [token, value] e.g. ["H1", "#"]
        while True:
            # Top of Stack = stack[-1]
            if stack[-1] == word[1] == "$":
                return True # success
            elif stack[-1] not in self.productions.keys(): # stack[-1] = terminal
                if stack[-1] != word[1]:
                    self.errors.append(f"Expected {word[0]}, got {stack[-1]}")
                    return False # error
                else:
                    stack.pop()
                    word = queue.pop(0)
            else: # stack[-1] == non-terminal
                if word[1] in self.parsing_table[stack[-1]].keys():
                    production = self.num_productions[self.parsing_table[stack[-1]][word[1]]][1]
                    stack.pop()
                    if not isinstance(production, list):
                        production = [production]
                    if production == ["epsilon"]:
                        continue
                    for prod in reversed(production): # reversed because we append to stack
                        stack.append(prod)
                else:
                    self.errors.append(f"Production not found: parsing_table[{stack[-1]}][{word[1]}]")
                    return False # error

    def enum_productions(self):
        for key, value in self.productions.items():
            if not isinstance(value, list):
                self.num_productions.append([key, value])
                continue
            for prod in value:
                self.num_productions.append([key, prod])

    def first(self, token, visited=None):
        firsts = set()
        if visited is None:
            visited = set()
        if token in visited:
            return firsts
        visited.add(token)
        if token not in self.productions:
            firsts.add(token)
            return firsts
        token_productions = self.productions[token]
        if isinstance(token_productions, str):
            firsts.add(token_productions)
            return firsts
        for production in token_productions:
            for symbol in production:
                symbol_first = self.first(symbol, visited)
                firsts |= symbol_first
                if "epsilon" not in symbol_first:
                    break
            else:
                if production:
                    firsts.add("epsilon")
        visited.remove(token)
        return firsts
    
    def follow(self, token, visited= None):
        follows = set()
        if visited is None:
            visited = set()
        if token in visited:
            return follows
        visited.add(token)
        if token == "DOCUMENT":
            follows.add("$")
            return follows
        visited.add(token)
        for production in self.num_productions:
            if token not in production[1]: # token not in production
                continue
            for idx, production_token in enumerate(production[1]):
                if production_token == token:
                    if idx == len(production[1]) - 1: # token = last e.g. A -> abCd[TOKEN]
                        follows |= self.follow(production[0], visited)
                    else: # token != last e.g. A -> abC[TOKEN]d
                        follows |= self.first(production[1][idx + 1])
        return follows
    
    def fill_parsing_table(self):
        for idx, num_production in enumerate(self.num_productions): # num_production = [key, production]
            if (num_production[0] not in self.parsing_table.keys()):
                self.parsing_table[num_production[0]] = dict()
            if not isinstance(num_production[1], list): # num_production[1] = terminal
                self.parsing_table[num_production[0]][num_production[1]] = idx
            else: # num_production[1] = list
                # Start of first plus
                firsts = self.first(num_production[1][0])
                if "epsilon" in firsts:
                    firsts |= self.follow(num_production[0])
                # End of first plus
                for first in firsts:
                    self.parsing_table[num_production[0]][first] = idx
    
    #Courtsey of chatGPT
    def write_parsing_table_to_file(self, file_name):
        with open(file_name, 'w') as file:
            # Write column headers
            file.write("{:<10}".format("Symbol"))
            terminals = set()
            for symbol, productions in self.parsing_table.items():
                terminals.update(productions.keys())
            for terminal in sorted(terminals):
                file.write("{:<10}".format(terminal))
            file.write("\n")

            # Write table content
            for symbol, productions in self.parsing_table.items():
                file.write("{:<10}".format(symbol))
                for terminal in sorted(terminals):
                    production_number = productions.get(terminal)
                    if production_number is not None:
                        file.write("{:<10}".format(str(production_number)))
                    else:
                        file.write("{:<10}".format("-"))
                file.write("\n")