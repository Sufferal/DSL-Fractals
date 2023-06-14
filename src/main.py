from lexer import Lexer
from parser import Parser
from fractal import Fractal

if __name__ == '__main__':
    fractal = Fractal()

    with open('source.txt', 'r') as file:
        text = file.read()

    lexer = Lexer(text)
    parser = Parser(lexer, fractal)
    parser.parse()
