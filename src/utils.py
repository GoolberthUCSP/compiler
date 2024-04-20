import rules

def convert_to_string(rules):
    result = ""
    for key, value in rules.items():
        if not isinstance(value, list):
            if key == "EOF" or key == "EPSILON" : continue
            if value == "\n": value = "n"
            elif value == "\n\n" : value = "nn"
            result += key + " ::= " + value + "\n"
            continue
        for prod in value:
            tmp = ""
            for item in prod:
                if item == "EOF" : continue
                elif item == "EPSILON" : item = "''"
                tmp += item + " "
            result += key + " ::= " + tmp + "\n"
    return result

print(convert_to_string(rules.productions))