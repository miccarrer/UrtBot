# Generated from plugins\commands\parser\Commands.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

from plugins.commands.models import *

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\n")
        buf.write("[\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2(\n\2")
        buf.write("\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b")
        buf.write("\5\bE\n\b\3\t\6\tH\n\t\r\t\16\tI\3\n\6\nM\n\n\r\n\16\n")
        buf.write("N\3\13\6\13R\n\13\r\13\16\13S\3\f\6\fW\n\f\r\f\16\fX\3")
        buf.write("\f\2\2\r\2\4\6\b\n\f\16\20\22\24\26\2\5\3\2\b\b\3\2\7")
        buf.write("\7\3\2\t\t\2X\2\'\3\2\2\2\4)\3\2\2\2\6,\3\2\2\2\b\63\3")
        buf.write("\2\2\2\n9\3\2\2\2\f<\3\2\2\2\16D\3\2\2\2\20G\3\2\2\2\22")
        buf.write("L\3\2\2\2\24Q\3\2\2\2\26V\3\2\2\2\30\31\5\b\5\2\31\32")
        buf.write("\b\2\1\2\32(\3\2\2\2\33\34\5\4\3\2\34\35\b\2\1\2\35(\3")
        buf.write("\2\2\2\36\37\5\6\4\2\37 \b\2\1\2 (\3\2\2\2!\"\5\n\6\2")
        buf.write("\"#\b\2\1\2#(\3\2\2\2$%\5\f\7\2%&\b\2\1\2&(\3\2\2\2\'")
        buf.write("\30\3\2\2\2\'\33\3\2\2\2\'\36\3\2\2\2\'!\3\2\2\2\'$\3")
        buf.write("\2\2\2(\3\3\2\2\2)*\7\4\2\2*+\b\3\1\2+\5\3\2\2\2,-\7\4")
        buf.write("\2\2-.\7\b\2\2./\5\26\f\2/\60\b\4\1\2\60\61\b\4\1\2\61")
        buf.write("\62\b\4\1\2\62\7\3\2\2\2\63\64\7\3\2\2\64\65\7\b\2\2\65")
        buf.write("\66\5\26\f\2\66\67\b\5\1\2\678\b\5\1\28\t\3\2\2\29:\7")
        buf.write("\5\2\2:;\b\6\1\2;\13\3\2\2\2<=\7\5\2\2=>\7\b\2\2>?\5\16")
        buf.write("\b\2?@\b\7\1\2@A\b\7\1\2A\r\3\2\2\2BE\5\20\t\2CE\5\22")
        buf.write("\n\2DB\3\2\2\2DC\3\2\2\2E\17\3\2\2\2FH\7\6\2\2GF\3\2\2")
        buf.write("\2HI\3\2\2\2IG\3\2\2\2IJ\3\2\2\2J\21\3\2\2\2KM\n\2\2\2")
        buf.write("LK\3\2\2\2MN\3\2\2\2NL\3\2\2\2NO\3\2\2\2O\23\3\2\2\2P")
        buf.write("R\n\3\2\2QP\3\2\2\2RS\3\2\2\2SQ\3\2\2\2ST\3\2\2\2T\25")
        buf.write("\3\2\2\2UW\n\4\2\2VU\3\2\2\2WX\3\2\2\2XV\3\2\2\2XY\3\2")
        buf.write("\2\2Y\27\3\2\2\2\b\'DINSX")
        return buf.getvalue()


class CommandsParser ( Parser ):

    grammarFileName = "Commands.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'\"'" ]

    symbolicNames = [ "<INVALID>", "RCON", "HELP", "KILL", "DIGIT", "DOUBLE_QUOTE", 
                      "WHITESPACE", "NEWLINE", "ANY_CHAR" ]

    RULE_command = 0
    RULE_helpAllCommand = 1
    RULE_helpOneCommand = 2
    RULE_rconCommand = 3
    RULE_killMeCommand = 4
    RULE_killPlayerCommand = 5
    RULE_clientValue = 6
    RULE_intValue = 7
    RULE_manyButWhitespace = 8
    RULE_manyButDoubleQuote = 9
    RULE_manyButNewLine = 10

    ruleNames =  [ "command", "helpAllCommand", "helpOneCommand", "rconCommand", 
                   "killMeCommand", "killPlayerCommand", "clientValue", 
                   "intValue", "manyButWhitespace", "manyButDoubleQuote", 
                   "manyButNewLine" ]

    EOF = Token.EOF
    RCON=1
    HELP=2
    KILL=3
    DIGIT=4
    DOUBLE_QUOTE=5
    WHITESPACE=6
    NEWLINE=7
    ANY_CHAR=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None
            self.rconCmd = None # RconCommandContext
            self.helpAllCmd = None # HelpAllCommandContext
            self.helpOneCmd = None # HelpOneCommandContext
            self.killMeCmd = None # KillMeCommandContext
            self.killPlayerCmd = None # KillPlayerCommandContext

        def rconCommand(self):
            return self.getTypedRuleContext(CommandsParser.RconCommandContext,0)


        def helpAllCommand(self):
            return self.getTypedRuleContext(CommandsParser.HelpAllCommandContext,0)


        def helpOneCommand(self):
            return self.getTypedRuleContext(CommandsParser.HelpOneCommandContext,0)


        def killMeCommand(self):
            return self.getTypedRuleContext(CommandsParser.KillMeCommandContext,0)


        def killPlayerCommand(self):
            return self.getTypedRuleContext(CommandsParser.KillPlayerCommandContext,0)


        def getRuleIndex(self):
            return CommandsParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)




    def command(self):

        localctx = CommandsParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_command)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 22
                localctx.rconCmd = self.rconCommand()
                localctx.value = localctx.rconCmd.value
                pass

            elif la_ == 2:
                self.state = 25
                localctx.helpAllCmd = self.helpAllCommand()
                localctx.value = localctx.helpAllCmd.value
                pass

            elif la_ == 3:
                self.state = 28
                localctx.helpOneCmd = self.helpOneCommand()
                localctx.value = localctx.helpOneCmd.value
                pass

            elif la_ == 4:
                self.state = 31
                localctx.killMeCmd = self.killMeCommand()
                localctx.value = localctx.killMeCmd.value
                pass

            elif la_ == 5:
                self.state = 34
                localctx.killPlayerCmd = self.killPlayerCommand()
                localctx.value = localctx.killPlayerCmd.value
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HelpAllCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None

        def HELP(self):
            return self.getToken(CommandsParser.HELP, 0)

        def getRuleIndex(self):
            return CommandsParser.RULE_helpAllCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHelpAllCommand" ):
                listener.enterHelpAllCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHelpAllCommand" ):
                listener.exitHelpAllCommand(self)




    def helpAllCommand(self):

        localctx = CommandsParser.HelpAllCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_helpAllCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(CommandsParser.HELP)
            localctx.value = HelpAllCommand()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HelpOneCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None
            self.cmd = None # ManyButNewLineContext

        def HELP(self):
            return self.getToken(CommandsParser.HELP, 0)

        def WHITESPACE(self):
            return self.getToken(CommandsParser.WHITESPACE, 0)

        def manyButNewLine(self):
            return self.getTypedRuleContext(CommandsParser.ManyButNewLineContext,0)


        def getRuleIndex(self):
            return CommandsParser.RULE_helpOneCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHelpOneCommand" ):
                listener.enterHelpOneCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHelpOneCommand" ):
                listener.exitHelpOneCommand(self)




    def helpOneCommand(self):

        localctx = CommandsParser.HelpOneCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_helpOneCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(CommandsParser.HELP)
            self.state = 43
            self.match(CommandsParser.WHITESPACE)
            self.state = 44
            localctx.cmd = self.manyButNewLine()
            localctx.value = HelpAllCommand()
            localctx.value = HelpOneCommand()
            localctx.value.target = (None if localctx.cmd is None else self._input.getText(localctx.cmd.start,localctx.cmd.stop))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RconCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None
            self.request = None # ManyButNewLineContext

        def RCON(self):
            return self.getToken(CommandsParser.RCON, 0)

        def WHITESPACE(self):
            return self.getToken(CommandsParser.WHITESPACE, 0)

        def manyButNewLine(self):
            return self.getTypedRuleContext(CommandsParser.ManyButNewLineContext,0)


        def getRuleIndex(self):
            return CommandsParser.RULE_rconCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRconCommand" ):
                listener.enterRconCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRconCommand" ):
                listener.exitRconCommand(self)




    def rconCommand(self):

        localctx = CommandsParser.RconCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_rconCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(CommandsParser.RCON)
            self.state = 50
            self.match(CommandsParser.WHITESPACE)
            self.state = 51
            localctx.request = self.manyButNewLine()
            localctx.value = RconCommand()
            localctx.value.request = (None if localctx.request is None else self._input.getText(localctx.request.start,localctx.request.stop))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KillMeCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None

        def KILL(self):
            return self.getToken(CommandsParser.KILL, 0)

        def getRuleIndex(self):
            return CommandsParser.RULE_killMeCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKillMeCommand" ):
                listener.enterKillMeCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKillMeCommand" ):
                listener.exitKillMeCommand(self)




    def killMeCommand(self):

        localctx = CommandsParser.KillMeCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_killMeCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(CommandsParser.KILL)
            localctx.value = KillMeCommand()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KillPlayerCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None
            self.client = None # ClientValueContext

        def KILL(self):
            return self.getToken(CommandsParser.KILL, 0)

        def WHITESPACE(self):
            return self.getToken(CommandsParser.WHITESPACE, 0)

        def clientValue(self):
            return self.getTypedRuleContext(CommandsParser.ClientValueContext,0)


        def getRuleIndex(self):
            return CommandsParser.RULE_killPlayerCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKillPlayerCommand" ):
                listener.enterKillPlayerCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKillPlayerCommand" ):
                listener.exitKillPlayerCommand(self)




    def killPlayerCommand(self):

        localctx = CommandsParser.KillPlayerCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_killPlayerCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(CommandsParser.KILL)
            self.state = 59
            self.match(CommandsParser.WHITESPACE)
            self.state = 60
            localctx.client = self.clientValue()
            localctx.value = KillPlayerCommand()
            localctx.value.target = (None if localctx.client is None else self._input.getText(localctx.client.start,localctx.client.stop))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClientValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def intValue(self):
            return self.getTypedRuleContext(CommandsParser.IntValueContext,0)


        def manyButWhitespace(self):
            return self.getTypedRuleContext(CommandsParser.ManyButWhitespaceContext,0)


        def getRuleIndex(self):
            return CommandsParser.RULE_clientValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClientValue" ):
                listener.enterClientValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClientValue" ):
                listener.exitClientValue(self)




    def clientValue(self):

        localctx = CommandsParser.ClientValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_clientValue)
        try:
            self.state = 66
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.intValue()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.manyButWhitespace()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(CommandsParser.DIGIT)
            else:
                return self.getToken(CommandsParser.DIGIT, i)

        def getRuleIndex(self):
            return CommandsParser.RULE_intValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntValue" ):
                listener.enterIntValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntValue" ):
                listener.exitIntValue(self)




    def intValue(self):

        localctx = CommandsParser.IntValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_intValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 68
                self.match(CommandsParser.DIGIT)
                self.state = 71 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CommandsParser.DIGIT):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ManyButWhitespaceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(CommandsParser.WHITESPACE)
            else:
                return self.getToken(CommandsParser.WHITESPACE, i)

        def getRuleIndex(self):
            return CommandsParser.RULE_manyButWhitespace

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterManyButWhitespace" ):
                listener.enterManyButWhitespace(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitManyButWhitespace" ):
                listener.exitManyButWhitespace(self)




    def manyButWhitespace(self):

        localctx = CommandsParser.ManyButWhitespaceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_manyButWhitespace)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 73
                _la = self._input.LA(1)
                if _la <= 0 or _la==CommandsParser.WHITESPACE:
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 76 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CommandsParser.RCON) | (1 << CommandsParser.HELP) | (1 << CommandsParser.KILL) | (1 << CommandsParser.DIGIT) | (1 << CommandsParser.DOUBLE_QUOTE) | (1 << CommandsParser.NEWLINE) | (1 << CommandsParser.ANY_CHAR))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ManyButDoubleQuoteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOUBLE_QUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(CommandsParser.DOUBLE_QUOTE)
            else:
                return self.getToken(CommandsParser.DOUBLE_QUOTE, i)

        def getRuleIndex(self):
            return CommandsParser.RULE_manyButDoubleQuote

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterManyButDoubleQuote" ):
                listener.enterManyButDoubleQuote(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitManyButDoubleQuote" ):
                listener.exitManyButDoubleQuote(self)




    def manyButDoubleQuote(self):

        localctx = CommandsParser.ManyButDoubleQuoteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_manyButDoubleQuote)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 78
                _la = self._input.LA(1)
                if _la <= 0 or _la==CommandsParser.DOUBLE_QUOTE:
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 81 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CommandsParser.RCON) | (1 << CommandsParser.HELP) | (1 << CommandsParser.KILL) | (1 << CommandsParser.DIGIT) | (1 << CommandsParser.WHITESPACE) | (1 << CommandsParser.NEWLINE) | (1 << CommandsParser.ANY_CHAR))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ManyButNewLineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(CommandsParser.NEWLINE)
            else:
                return self.getToken(CommandsParser.NEWLINE, i)

        def getRuleIndex(self):
            return CommandsParser.RULE_manyButNewLine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterManyButNewLine" ):
                listener.enterManyButNewLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitManyButNewLine" ):
                listener.exitManyButNewLine(self)




    def manyButNewLine(self):

        localctx = CommandsParser.ManyButNewLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_manyButNewLine)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 83
                _la = self._input.LA(1)
                if _la <= 0 or _la==CommandsParser.NEWLINE:
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 86 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CommandsParser.RCON) | (1 << CommandsParser.HELP) | (1 << CommandsParser.KILL) | (1 << CommandsParser.DIGIT) | (1 << CommandsParser.DOUBLE_QUOTE) | (1 << CommandsParser.WHITESPACE) | (1 << CommandsParser.ANY_CHAR))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





