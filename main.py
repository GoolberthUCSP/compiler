from src.grammar import *
from src.utils import *
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    my_grammar = Grammar()
    file_path = "/test/test2.txt"
    with open(script_dir + file_path, "r", encoding="utf-8") as file:
        buffer = MyStringIO(file.read())
        my_grammar.file_name = file_path
        my_grammar.validate(buffer)