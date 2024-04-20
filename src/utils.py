import rules

separator = " -> "

def convert_to_string(rules):
    result = ""
    for key, value in rules.items():
        if not isinstance(value, list):
            if key == "EOF" or key == "EPSILON" : continue
            if value == "\n": value = "n"
            elif value == "\n\n" : value = "nn"
            result += key + separator + value + "\n"
            continue
        for prod in value:
            tmp = ""
            for item in prod:
                if item == "EOF" : continue
                elif item == "EPSILON" : item = "''"
                tmp += item + " "
            result += key + separator + tmp + "\n"
    return result

print(convert_to_string(rules.productions))