import sys
from lexer import Lexer
from parser import Parser
from fractal import Fractal

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("[USAGE]: py main.py file_name.txt")
        sys.exit(1)
    
    filename = sys.argv[1]
    fractal = Fractal()

    with open(filename, 'r') as file:
        text = file.read()

    lexer = Lexer(text)
    parser = Parser(lexer, fractal)
    parser.parse()
