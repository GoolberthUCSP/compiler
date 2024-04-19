from src.grammar import *
import io
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

if __name__ == "__main__":
    file = open("test/data.txt", "r", encoding="utf-8")
    my_grammar = Grammar()
    my_grammar.validate(MyStringIO(file.read()))
    file.close()
    for token in my_grammar.tokens:
        print(token)