import io

class MyStringIO(io.StringIO):
    def peek(self, size=1):
        current_position = self.tell()
        data = self.read(size)
        self.seek(current_position)
        return data

class Grammar:
    def __init__(self, productions):
        self.productions = productions
        self.num_productions = []
        self.parsing_table = dict(dict())
        self.tokens = []
        self.errors = []
        self.file = None
        self.enum_productions()
        self.fill_parsing_table()

    def validate(self, input : MyStringIO):
        self.file = input
        self.tokens = self.scanner()
        done = self.parser()
        if not done:
            for error in self.errors:
                print(error)
        return done

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
                self.tokens.append(["TEXTMARK", self.file.read(1)])  # value = '
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
        for token in self.tokens:
            value = token[1]
            queue = [value] # TODO

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
        visited.add(token)
        if token not in self.productions:
            firsts.add(token)
            firsts.add(token)
            return firsts
        token_productions = self.productions[token]
        if isinstance(token_productions, str):
            firsts.add(token_productions)
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
                    firsts.add("epsilon")
        visited.remove(token)
        return firsts
    
    def follow(self, token, visited= None):
        #print(f"calculating follow of: {token}")
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
                #print(f"idx: {idx}, production token: {production_token}")
                if production_token == token:
                    #print(f"idx: {idx}, production token: {production_token}, production: {production}")
                    if idx == len(production[1]) - 1: # token = last e.g. A -> abCd[TOKEN]
                        follows |= self.follow(production[0], visited)
                    else: # token != last e.g. A -> abC[TOKEN]d
                        follows |= self.first(production[1][idx + 1])
        return follows
    
    def fill_parsing_table(self):
        for idx, num_production in enumerate(self.num_productions): # num_production = [key, production]
            self.parsing_table[num_production[0]] = dict()
            if not isinstance(num_production[1], list): # num_production[1] = terminal
                if num_production[0] not in parsing_tab:
                        parsing_tab[num_production[0]] = {}
                self.parsing_table[num_production[0]][num_production[1]] = idx
            else: # num_production[1] = list
                # Start of first plus
                print(f"Production: {num_production[0]}")
                firsts = self.first(num_production[1][0])
                print(f"Set after first: {firsts}")
                if "epsilon" in firsts:
                    #print(f"follow function of: {num_production[0]}")
                    firsts |= self.follow(num_production[0])
                # End of first plus
                print(f"Set after follow: {firsts}")
                for first in firsts:
                    self.parsing_table[num_production[0]][first] = idx
