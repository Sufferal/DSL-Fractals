# Generated from SimpleArithmetic.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SimpleArithmeticParser import SimpleArithmeticParser
else:
    from SimpleArithmeticParser import SimpleArithmeticParser

# This class defines a complete listener for a parse tree produced by SimpleArithmeticParser.
class SimpleArithmeticListener(ParseTreeListener):

    # Enter a parse tree produced by SimpleArithmeticParser#expr.
    def enterExpr(self, ctx:SimpleArithmeticParser.ExprContext):
        pass

    # Exit a parse tree produced by SimpleArithmeticParser#expr.
    def exitExpr(self, ctx:SimpleArithmeticParser.ExprContext):
        pass


    # Enter a parse tree produced by SimpleArithmeticParser#term.
    def enterTerm(self, ctx:SimpleArithmeticParser.TermContext):
        pass

    # Exit a parse tree produced by SimpleArithmeticParser#term.
    def exitTerm(self, ctx:SimpleArithmeticParser.TermContext):
        pass


    # Enter a parse tree produced by SimpleArithmeticParser#factor.
    def enterFactor(self, ctx:SimpleArithmeticParser.FactorContext):
        pass

    # Exit a parse tree produced by SimpleArithmeticParser#factor.
    def exitFactor(self, ctx:SimpleArithmeticParser.FactorContext):
        pass



del SimpleArithmeticParser