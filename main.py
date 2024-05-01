from src.grammar import *
from src.rules import productions
from src.utils import *
import io
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

if __name__ == "__main__":
    my_grammar = Grammar(productions)
    with open("test/testdata.txt", "r", encoding="utf-8") as file:
        buffer = MyStringIO(file.read())
        my_grammar.validate(buffer)