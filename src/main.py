from antlr4 import *
from SimpleArithmeticLexer import SimpleArithmeticLexer
from SimpleArithmeticParser import SimpleArithmeticParser

# create a stream of input characters
input_stream = InputStream("3 + 4 * (5 - 2)")

# create a lexer that reads from the input stream
lexer = SimpleArithmeticLexer(input_stream)

# create a stream of tokens from the lexer
token_stream = CommonTokenStream(lexer)

# create a parser that reads from the token stream
parser = SimpleArithmeticParser(token_stream)

# parse the input and print the result
tree = parser.expr()
print(tree.toStringTree(recog=parser))
