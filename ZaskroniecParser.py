# Generated from Zaskroniec.g4 by ANTLR 4.13.1
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
        4,1,58,15,2,0,7,0,2,1,7,1,1,0,5,0,6,8,0,10,0,12,0,9,9,0,1,0,1,0,
        1,1,1,1,1,1,0,0,2,0,2,0,1,1,0,1,58,13,0,7,1,0,0,0,2,12,1,0,0,0,4,
        6,3,2,1,0,5,4,1,0,0,0,6,9,1,0,0,0,7,5,1,0,0,0,7,8,1,0,0,0,8,10,1,
        0,0,0,9,7,1,0,0,0,10,11,5,0,0,1,11,1,1,0,0,0,12,13,7,0,0,0,13,3,
        1,0,0,0,1,7
    ]

class ZaskroniecParser ( Parser ):

    grammarFileName = "Zaskroniec.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'albo_jesli'", "<INVALID>", 
                     "'dopoki'", "'dla'", "'w'", "'przerwij'", "'kontynuuj'", 
                     "'pomin'", "'zdefiniuj'", "'zwroc'", "'klasa'", "'dostarcz'", 
                     "'anonimowa'", "'oraz'", "<INVALID>", "'nie'", "'jest'", 
                     "'Prawda'", "'Falsz'", "'Nic'", "'zaimportuj'", "'z'", 
                     "'jako'", "'z_kontekstem'", "'sprobuj'", "<INVALID>", 
                     "'wreszcie'", "'rzuc'", "'zapewnij'", "'globalna'", 
                     "'nielokalna'", "'asynchronicznie'", "'oczekuj'", "'usun'", 
                     "'wypisz'", "'zasieg'", "'dlugosc'", "'napis'", "'calkowita'", 
                     "'zmienna_przecinkowa'", "'logiczna'", "'lista'", "'slownik'", 
                     "'zbior'", "'krotka'", "'bezwzgledna'", "'suma'", "'minimum'", 
                     "'maksimum'", "'zaokraglij'", "'typ'", "'otworz'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELIF", "ELSE", "WHILE", "FOR", 
                      "IN", "BREAK", "CONTINUE", "PASS", "DEF", "RETURN", 
                      "CLASS", "YIELD", "LAMBDA", "AND", "OR", "NOT", "IS", 
                      "TRUE", "FALSE", "NONE", "IMPORT", "FROM", "AS", "WITH", 
                      "TRY", "EXCEPT", "FINALLY", "RAISE", "ASSERT", "GLOBAL", 
                      "NONLOCAL", "ASYNC", "AWAIT", "DEL", "PRINT", "RANGE", 
                      "LEN", "STR", "INT", "FLOAT", "BOOL", "LIST", "DICT", 
                      "SET", "TUPLE", "ABS", "SUM", "MIN", "MAX", "ROUND", 
                      "TYPE", "OPEN", "ID", "STRING", "NUMBER", "WS", "SYMBOL" ]

    RULE_program = 0
    RULE_element = 1

    ruleNames =  [ "program", "element" ]

    EOF = Token.EOF
    IF=1
    ELIF=2
    ELSE=3
    WHILE=4
    FOR=5
    IN=6
    BREAK=7
    CONTINUE=8
    PASS=9
    DEF=10
    RETURN=11
    CLASS=12
    YIELD=13
    LAMBDA=14
    AND=15
    OR=16
    NOT=17
    IS=18
    TRUE=19
    FALSE=20
    NONE=21
    IMPORT=22
    FROM=23
    AS=24
    WITH=25
    TRY=26
    EXCEPT=27
    FINALLY=28
    RAISE=29
    ASSERT=30
    GLOBAL=31
    NONLOCAL=32
    ASYNC=33
    AWAIT=34
    DEL=35
    PRINT=36
    RANGE=37
    LEN=38
    STR=39
    INT=40
    FLOAT=41
    BOOL=42
    LIST=43
    DICT=44
    SET=45
    TUPLE=46
    ABS=47
    SUM=48
    MIN=49
    MAX=50
    ROUND=51
    TYPE=52
    OPEN=53
    ID=54
    STRING=55
    NUMBER=56
    WS=57
    SYMBOL=58

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ZaskroniecParser.EOF, 0)

        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZaskroniecParser.ElementContext)
            else:
                return self.getTypedRuleContext(ZaskroniecParser.ElementContext,i)


        def getRuleIndex(self):
            return ZaskroniecParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = ZaskroniecParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 576460752303423486) != 0):
                self.state = 4
                self.element()
                self.state = 9
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 10
            self.match(ZaskroniecParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZaskroniecParser.IF, 0)

        def ELIF(self):
            return self.getToken(ZaskroniecParser.ELIF, 0)

        def ELSE(self):
            return self.getToken(ZaskroniecParser.ELSE, 0)

        def WHILE(self):
            return self.getToken(ZaskroniecParser.WHILE, 0)

        def FOR(self):
            return self.getToken(ZaskroniecParser.FOR, 0)

        def IN(self):
            return self.getToken(ZaskroniecParser.IN, 0)

        def BREAK(self):
            return self.getToken(ZaskroniecParser.BREAK, 0)

        def CONTINUE(self):
            return self.getToken(ZaskroniecParser.CONTINUE, 0)

        def PASS(self):
            return self.getToken(ZaskroniecParser.PASS, 0)

        def DEF(self):
            return self.getToken(ZaskroniecParser.DEF, 0)

        def RETURN(self):
            return self.getToken(ZaskroniecParser.RETURN, 0)

        def CLASS(self):
            return self.getToken(ZaskroniecParser.CLASS, 0)

        def YIELD(self):
            return self.getToken(ZaskroniecParser.YIELD, 0)

        def LAMBDA(self):
            return self.getToken(ZaskroniecParser.LAMBDA, 0)

        def AND(self):
            return self.getToken(ZaskroniecParser.AND, 0)

        def OR(self):
            return self.getToken(ZaskroniecParser.OR, 0)

        def NOT(self):
            return self.getToken(ZaskroniecParser.NOT, 0)

        def IS(self):
            return self.getToken(ZaskroniecParser.IS, 0)

        def TRUE(self):
            return self.getToken(ZaskroniecParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(ZaskroniecParser.FALSE, 0)

        def NONE(self):
            return self.getToken(ZaskroniecParser.NONE, 0)

        def WITH(self):
            return self.getToken(ZaskroniecParser.WITH, 0)

        def IMPORT(self):
            return self.getToken(ZaskroniecParser.IMPORT, 0)

        def FROM(self):
            return self.getToken(ZaskroniecParser.FROM, 0)

        def AS(self):
            return self.getToken(ZaskroniecParser.AS, 0)

        def TRY(self):
            return self.getToken(ZaskroniecParser.TRY, 0)

        def EXCEPT(self):
            return self.getToken(ZaskroniecParser.EXCEPT, 0)

        def FINALLY(self):
            return self.getToken(ZaskroniecParser.FINALLY, 0)

        def RAISE(self):
            return self.getToken(ZaskroniecParser.RAISE, 0)

        def ASSERT(self):
            return self.getToken(ZaskroniecParser.ASSERT, 0)

        def GLOBAL(self):
            return self.getToken(ZaskroniecParser.GLOBAL, 0)

        def NONLOCAL(self):
            return self.getToken(ZaskroniecParser.NONLOCAL, 0)

        def ASYNC(self):
            return self.getToken(ZaskroniecParser.ASYNC, 0)

        def AWAIT(self):
            return self.getToken(ZaskroniecParser.AWAIT, 0)

        def DEL(self):
            return self.getToken(ZaskroniecParser.DEL, 0)

        def PRINT(self):
            return self.getToken(ZaskroniecParser.PRINT, 0)

        def RANGE(self):
            return self.getToken(ZaskroniecParser.RANGE, 0)

        def LEN(self):
            return self.getToken(ZaskroniecParser.LEN, 0)

        def STR(self):
            return self.getToken(ZaskroniecParser.STR, 0)

        def INT(self):
            return self.getToken(ZaskroniecParser.INT, 0)

        def FLOAT(self):
            return self.getToken(ZaskroniecParser.FLOAT, 0)

        def BOOL(self):
            return self.getToken(ZaskroniecParser.BOOL, 0)

        def LIST(self):
            return self.getToken(ZaskroniecParser.LIST, 0)

        def DICT(self):
            return self.getToken(ZaskroniecParser.DICT, 0)

        def SET(self):
            return self.getToken(ZaskroniecParser.SET, 0)

        def TUPLE(self):
            return self.getToken(ZaskroniecParser.TUPLE, 0)

        def ABS(self):
            return self.getToken(ZaskroniecParser.ABS, 0)

        def SUM(self):
            return self.getToken(ZaskroniecParser.SUM, 0)

        def MIN(self):
            return self.getToken(ZaskroniecParser.MIN, 0)

        def MAX(self):
            return self.getToken(ZaskroniecParser.MAX, 0)

        def ROUND(self):
            return self.getToken(ZaskroniecParser.ROUND, 0)

        def TYPE(self):
            return self.getToken(ZaskroniecParser.TYPE, 0)

        def OPEN(self):
            return self.getToken(ZaskroniecParser.OPEN, 0)

        def ID(self):
            return self.getToken(ZaskroniecParser.ID, 0)

        def STRING(self):
            return self.getToken(ZaskroniecParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(ZaskroniecParser.NUMBER, 0)

        def WS(self):
            return self.getToken(ZaskroniecParser.WS, 0)

        def SYMBOL(self):
            return self.getToken(ZaskroniecParser.SYMBOL, 0)

        def getRuleIndex(self):
            return ZaskroniecParser.RULE_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElement" ):
                listener.enterElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElement" ):
                listener.exitElement(self)




    def element(self):

        localctx = ZaskroniecParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_element)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 576460752303423486) != 0)):
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





