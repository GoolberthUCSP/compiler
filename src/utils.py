def convert_to_string(rules):
    result = ""
    separator = " ::= "
    for key, value in rules.items():
        if not isinstance(value, list):
            if key == "EOF" : continue
            if value == "\n": value = "n"
            elif value == "\n\n" : value = "nn"
            result += key + separator + value + "\n"
            continue
        for prod in value:
            tmp = ""
            for item in prod:
                if item == "EOF" : continue
                elif item == "epsilon" : item = "''"
                tmp += item + " "
            result += key + separator + tmp + "\n"
    return result

def first(token, productions, visited=None):
    firsts = set()
    if visited is None:
        visited = set()
    if token in visited:
        return firsts
    visited.add(token)
    if token not in productions:
        firsts.add(token)
        return firsts
    token_productions = productions[token]
    if isinstance(token_productions, str):
        firsts.add(token_productions)
        return firsts
    for production in token_productions:
        for symbol in production:
            symbol_first = first(symbol, productions, visited)
            firsts |= symbol_first
            if "epsilon" not in symbol_first:
                break
        else:
            if production:
                firsts.add("epsilon")
    visited.remove(token)
    return firsts