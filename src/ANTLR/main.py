from antlr4 import *
from grammar_fractalsLexer import grammar_fractalsLexer
from grammar_fractalsParser import grammar_fractalsParser

# create a stream of input characters
input_stream = InputStream("size 100")

# create a lexer that reads from the input stream
lexer = grammar_fractalsLexer(input_stream)

# create a stream of tokens from the lexer
token_stream = CommonTokenStream(lexer)

# create a parser that reads from the token stream
parser = grammar_fractalsParser(token_stream)

# parse the input and print the result
tree = parser.program()
print(tree.toStringTree(recog=parser))

print(input_stream)
print(lexer)
print(token_stream)
print(parser)
