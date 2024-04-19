from src import scanner
import io
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

if __name__ == "__main__":
    file = open("test/data.txt", "r", encoding="utf-8")
    file = scanner.MyStringIO(file.read())
    tokens = scanner.Scanner(file)
    file.close()
    for token in tokens:
        print(token)