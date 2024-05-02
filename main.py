from src.grammar import *
from src.utils import *
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    my_grammar = Grammar()
    with open(script_dir + "/test/testdata.txt", "r", encoding="utf-8") as file:
        buffer = MyStringIO(file.read())
        my_grammar.validate(buffer)
    print(my_grammar.strings)