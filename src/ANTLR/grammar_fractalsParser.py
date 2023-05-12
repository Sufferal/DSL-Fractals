# Generated from grammar_fractals.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,38,115,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        1,0,1,0,1,0,3,0,45,8,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,3,1,58,8,1,1,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,1,5,1,5,1,5,1,6,
        1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,10,1,
        11,1,11,1,12,1,12,1,13,1,13,1,13,1,14,1,14,1,15,1,15,1,16,1,16,1,
        16,1,16,3,16,103,8,16,1,17,1,17,1,18,5,18,108,8,18,10,18,12,18,111,
        9,18,1,19,1,19,1,19,0,0,20,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,34,36,38,0,5,1,0,10,11,1,0,14,17,1,0,18,27,1,0,28,29,1,
        0,29,37,107,0,44,1,0,0,0,2,57,1,0,0,0,4,59,1,0,0,0,6,62,1,0,0,0,
        8,65,1,0,0,0,10,68,1,0,0,0,12,71,1,0,0,0,14,74,1,0,0,0,16,78,1,0,
        0,0,18,81,1,0,0,0,20,84,1,0,0,0,22,87,1,0,0,0,24,89,1,0,0,0,26,91,
        1,0,0,0,28,94,1,0,0,0,30,96,1,0,0,0,32,102,1,0,0,0,34,104,1,0,0,
        0,36,109,1,0,0,0,38,112,1,0,0,0,40,45,3,2,1,0,41,42,3,2,1,0,42,43,
        3,0,0,0,43,45,1,0,0,0,44,40,1,0,0,0,44,41,1,0,0,0,45,1,1,0,0,0,46,
        58,3,4,2,0,47,58,3,6,3,0,48,58,3,8,4,0,49,58,3,10,5,0,50,58,3,12,
        6,0,51,58,3,14,7,0,52,58,3,16,8,0,53,58,3,18,9,0,54,58,3,20,10,0,
        55,58,3,24,12,0,56,58,3,26,13,0,57,46,1,0,0,0,57,47,1,0,0,0,57,48,
        1,0,0,0,57,49,1,0,0,0,57,50,1,0,0,0,57,51,1,0,0,0,57,52,1,0,0,0,
        57,53,1,0,0,0,57,54,1,0,0,0,57,55,1,0,0,0,57,56,1,0,0,0,58,3,1,0,
        0,0,59,60,5,1,0,0,60,61,3,36,18,0,61,5,1,0,0,0,62,63,5,2,0,0,63,
        64,3,36,18,0,64,7,1,0,0,0,65,66,5,3,0,0,66,67,3,36,18,0,67,9,1,0,
        0,0,68,69,5,4,0,0,69,70,3,36,18,0,70,11,1,0,0,0,71,72,5,5,0,0,72,
        73,3,28,14,0,73,13,1,0,0,0,74,75,5,6,0,0,75,76,3,36,18,0,76,77,3,
        36,18,0,77,15,1,0,0,0,78,79,5,7,0,0,79,80,3,36,18,0,80,17,1,0,0,
        0,81,82,5,8,0,0,82,83,3,36,18,0,83,19,1,0,0,0,84,85,5,9,0,0,85,86,
        3,22,11,0,86,21,1,0,0,0,87,88,7,0,0,0,88,23,1,0,0,0,89,90,5,12,0,
        0,90,25,1,0,0,0,91,92,5,13,0,0,92,93,3,34,17,0,93,27,1,0,0,0,94,
        95,7,1,0,0,95,29,1,0,0,0,96,97,7,2,0,0,97,31,1,0,0,0,98,103,3,38,
        19,0,99,100,3,38,19,0,100,101,3,32,16,0,101,103,1,0,0,0,102,98,1,
        0,0,0,102,99,1,0,0,0,103,33,1,0,0,0,104,105,5,28,0,0,105,35,1,0,
        0,0,106,108,7,3,0,0,107,106,1,0,0,0,108,111,1,0,0,0,109,107,1,0,
        0,0,109,110,1,0,0,0,110,37,1,0,0,0,111,109,1,0,0,0,112,113,7,4,0,
        0,113,39,1,0,0,0,4,44,57,102,109
    ]

class grammar_fractalsParser ( Parser ):

    grammarFileName = "grammar_fractals.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'size'", "'color'", "'angle'", "'iterations'", 
                     "'shape'", "'move'", "'scale'", "'rotate'", "'mirror'", 
                     "'x'", "'y'", "'draw'", "'save'", "'circle'", "'square'", 
                     "'triangle'", "'polygon'", "'0'", "'1'", "'2'", "'3'", 
                     "'4'", "'5'", "'6'", "'7'", "'8'", "'9'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'='", "'.'", "','", "'['", 
                     "']'", "' '", "'_'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "STRING", "DIGIT", "LETTER", "EQ", "DOT", "COMMA", 
                      "LBRACK", "RBRACK", "SPACE", "UNDERSCORE", "ESC" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_size_statement = 2
    RULE_color_statement = 3
    RULE_angle_statement = 4
    RULE_iterations_statement = 5
    RULE_shape_statement = 6
    RULE_move_statement = 7
    RULE_scale_statement = 8
    RULE_rotate_statement = 9
    RULE_mirror_statement = 10
    RULE_axis = 11
    RULE_draw_statement = 12
    RULE_save_statement = 13
    RULE_shape = 14
    RULE_digit = 15
    RULE_string = 16
    RULE_filename = 17
    RULE_value = 18
    RULE_char = 19

    ruleNames =  [ "program", "statement", "size_statement", "color_statement", 
                   "angle_statement", "iterations_statement", "shape_statement", 
                   "move_statement", "scale_statement", "rotate_statement", 
                   "mirror_statement", "axis", "draw_statement", "save_statement", 
                   "shape", "digit", "string", "filename", "value", "char" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    STRING=28
    DIGIT=29
    LETTER=30
    EQ=31
    DOT=32
    COMMA=33
    LBRACK=34
    RBRACK=35
    SPACE=36
    UNDERSCORE=37
    ESC=38

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(grammar_fractalsParser.StatementContext,0)


        def program(self):
            return self.getTypedRuleContext(grammar_fractalsParser.ProgramContext,0)


        def getRuleIndex(self):
            return grammar_fractalsParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = grammar_fractalsParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.state = 44
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.statement()
                self.state = 42
                self.program()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def size_statement(self):
            return self.getTypedRuleContext(grammar_fractalsParser.Size_statementContext,0)


        def color_statement(self):
            return self.getTypedRuleContext(grammar_fractalsParser.Color_statementContext,0)


        def angle_statement(self):
            return self.getTypedRuleContext(grammar_fractalsParser.Angle_statementContext,0)


        def iterations_statement(self):
            return self.getTypedRuleContext(grammar_fractalsParser.Iterations_statementContext,0)


        def shape_statement(self):
            return self.getTypedRuleContext(grammar_fractalsParser.Shape_statementContext,0)


        def move_statement(self):
            return self.getTypedRuleContext(grammar_fractalsParser.Move_statementContext,0)


        def scale_statement(self):
            return self.getTypedRuleContext(grammar_fractalsParser.Scale_statementContext,0)


        def rotate_statement(self):
            return self.getTypedRuleContext(grammar_fractalsParser.Rotate_statementContext,0)


        def mirror_statement(self):
            return self.getTypedRuleContext(grammar_fractalsParser.Mirror_statementContext,0)


        def draw_statement(self):
            return self.getTypedRuleContext(grammar_fractalsParser.Draw_statementContext,0)


        def save_statement(self):
            return self.getTypedRuleContext(grammar_fractalsParser.Save_statementContext,0)


        def getRuleIndex(self):
            return grammar_fractalsParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = grammar_fractalsParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 57
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.size_statement()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.color_statement()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 48
                self.angle_statement()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 49
                self.iterations_statement()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 5)
                self.state = 50
                self.shape_statement()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 6)
                self.state = 51
                self.move_statement()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 7)
                self.state = 52
                self.scale_statement()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 8)
                self.state = 53
                self.rotate_statement()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 9)
                self.state = 54
                self.mirror_statement()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 10)
                self.state = 55
                self.draw_statement()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 11)
                self.state = 56
                self.save_statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Size_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(grammar_fractalsParser.ValueContext,0)


        def getRuleIndex(self):
            return grammar_fractalsParser.RULE_size_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSize_statement" ):
                listener.enterSize_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSize_statement" ):
                listener.exitSize_statement(self)




    def size_statement(self):

        localctx = grammar_fractalsParser.Size_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_size_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(grammar_fractalsParser.T__0)
            self.state = 60
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Color_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(grammar_fractalsParser.ValueContext,0)


        def getRuleIndex(self):
            return grammar_fractalsParser.RULE_color_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColor_statement" ):
                listener.enterColor_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColor_statement" ):
                listener.exitColor_statement(self)




    def color_statement(self):

        localctx = grammar_fractalsParser.Color_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_color_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(grammar_fractalsParser.T__1)
            self.state = 63
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Angle_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(grammar_fractalsParser.ValueContext,0)


        def getRuleIndex(self):
            return grammar_fractalsParser.RULE_angle_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAngle_statement" ):
                listener.enterAngle_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAngle_statement" ):
                listener.exitAngle_statement(self)




    def angle_statement(self):

        localctx = grammar_fractalsParser.Angle_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_angle_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(grammar_fractalsParser.T__2)
            self.state = 66
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Iterations_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(grammar_fractalsParser.ValueContext,0)


        def getRuleIndex(self):
            return grammar_fractalsParser.RULE_iterations_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIterations_statement" ):
                listener.enterIterations_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIterations_statement" ):
                listener.exitIterations_statement(self)




    def iterations_statement(self):

        localctx = grammar_fractalsParser.Iterations_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_iterations_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(grammar_fractalsParser.T__3)
            self.state = 69
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Shape_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def shape(self):
            return self.getTypedRuleContext(grammar_fractalsParser.ShapeContext,0)


        def getRuleIndex(self):
            return grammar_fractalsParser.RULE_shape_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShape_statement" ):
                listener.enterShape_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShape_statement" ):
                listener.exitShape_statement(self)




    def shape_statement(self):

        localctx = grammar_fractalsParser.Shape_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_shape_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(grammar_fractalsParser.T__4)
            self.state = 72
            self.shape()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Move_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammar_fractalsParser.ValueContext)
            else:
                return self.getTypedRuleContext(grammar_fractalsParser.ValueContext,i)


        def getRuleIndex(self):
            return grammar_fractalsParser.RULE_move_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMove_statement" ):
                listener.enterMove_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMove_statement" ):
                listener.exitMove_statement(self)




    def move_statement(self):

        localctx = grammar_fractalsParser.Move_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_move_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(grammar_fractalsParser.T__5)
            self.state = 75
            self.value()
            self.state = 76
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scale_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(grammar_fractalsParser.ValueContext,0)


        def getRuleIndex(self):
            return grammar_fractalsParser.RULE_scale_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScale_statement" ):
                listener.enterScale_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScale_statement" ):
                listener.exitScale_statement(self)




    def scale_statement(self):

        localctx = grammar_fractalsParser.Scale_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_scale_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(grammar_fractalsParser.T__6)
            self.state = 79
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rotate_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(grammar_fractalsParser.ValueContext,0)


        def getRuleIndex(self):
            return grammar_fractalsParser.RULE_rotate_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRotate_statement" ):
                listener.enterRotate_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRotate_statement" ):
                listener.exitRotate_statement(self)




    def rotate_statement(self):

        localctx = grammar_fractalsParser.Rotate_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_rotate_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(grammar_fractalsParser.T__7)
            self.state = 82
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mirror_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def axis(self):
            return self.getTypedRuleContext(grammar_fractalsParser.AxisContext,0)


        def getRuleIndex(self):
            return grammar_fractalsParser.RULE_mirror_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMirror_statement" ):
                listener.enterMirror_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMirror_statement" ):
                listener.exitMirror_statement(self)




    def mirror_statement(self):

        localctx = grammar_fractalsParser.Mirror_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_mirror_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(grammar_fractalsParser.T__8)
            self.state = 85
            self.axis()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AxisContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return grammar_fractalsParser.RULE_axis

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAxis" ):
                listener.enterAxis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAxis" ):
                listener.exitAxis(self)




    def axis(self):

        localctx = grammar_fractalsParser.AxisContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_axis)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            _la = self._input.LA(1)
            if not(_la==10 or _la==11):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Draw_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return grammar_fractalsParser.RULE_draw_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDraw_statement" ):
                listener.enterDraw_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDraw_statement" ):
                listener.exitDraw_statement(self)




    def draw_statement(self):

        localctx = grammar_fractalsParser.Draw_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_draw_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(grammar_fractalsParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Save_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def filename(self):
            return self.getTypedRuleContext(grammar_fractalsParser.FilenameContext,0)


        def getRuleIndex(self):
            return grammar_fractalsParser.RULE_save_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSave_statement" ):
                listener.enterSave_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSave_statement" ):
                listener.exitSave_statement(self)




    def save_statement(self):

        localctx = grammar_fractalsParser.Save_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_save_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(grammar_fractalsParser.T__12)
            self.state = 92
            self.filename()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShapeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return grammar_fractalsParser.RULE_shape

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShape" ):
                listener.enterShape(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShape" ):
                listener.exitShape(self)




    def shape(self):

        localctx = grammar_fractalsParser.ShapeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_shape)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 245760) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DigitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return grammar_fractalsParser.RULE_digit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDigit" ):
                listener.enterDigit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDigit" ):
                listener.exitDigit(self)




    def digit(self):

        localctx = grammar_fractalsParser.DigitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_digit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 268173312) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def char(self):
            return self.getTypedRuleContext(grammar_fractalsParser.CharContext,0)


        def string(self):
            return self.getTypedRuleContext(grammar_fractalsParser.StringContext,0)


        def getRuleIndex(self):
            return grammar_fractalsParser.RULE_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)




    def string(self):

        localctx = grammar_fractalsParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_string)
        try:
            self.state = 102
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.char()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 99
                self.char()
                self.state = 100
                self.string()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilenameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(grammar_fractalsParser.STRING, 0)

        def getRuleIndex(self):
            return grammar_fractalsParser.RULE_filename

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilename" ):
                listener.enterFilename(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilename" ):
                listener.exitFilename(self)




    def filename(self):

        localctx = grammar_fractalsParser.FilenameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_filename)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(grammar_fractalsParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(grammar_fractalsParser.DIGIT)
            else:
                return self.getToken(grammar_fractalsParser.DIGIT, i)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(grammar_fractalsParser.STRING)
            else:
                return self.getToken(grammar_fractalsParser.STRING, i)

        def getRuleIndex(self):
            return grammar_fractalsParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = grammar_fractalsParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 106
                    _la = self._input.LA(1)
                    if not(_la==28 or _la==29):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 111
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CharContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LETTER(self):
            return self.getToken(grammar_fractalsParser.LETTER, 0)

        def DIGIT(self):
            return self.getToken(grammar_fractalsParser.DIGIT, 0)

        def EQ(self):
            return self.getToken(grammar_fractalsParser.EQ, 0)

        def DOT(self):
            return self.getToken(grammar_fractalsParser.DOT, 0)

        def COMMA(self):
            return self.getToken(grammar_fractalsParser.COMMA, 0)

        def LBRACK(self):
            return self.getToken(grammar_fractalsParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(grammar_fractalsParser.RBRACK, 0)

        def SPACE(self):
            return self.getToken(grammar_fractalsParser.SPACE, 0)

        def UNDERSCORE(self):
            return self.getToken(grammar_fractalsParser.UNDERSCORE, 0)

        def getRuleIndex(self):
            return grammar_fractalsParser.RULE_char

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChar" ):
                listener.enterChar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChar" ):
                listener.exitChar(self)




    def char(self):

        localctx = grammar_fractalsParser.CharContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_char)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 274341036032) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





