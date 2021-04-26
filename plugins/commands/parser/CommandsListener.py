# Generated from plugins\commands\parser\Commands.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CommandsParser import CommandsParser
else:
    from CommandsParser import CommandsParser
from plugins.commands.models import *

# This class defines a complete listener for a parse tree produced by CommandsParser.
class CommandsListener(ParseTreeListener):

    # Enter a parse tree produced by CommandsParser#command.
    def enterCommand(self, ctx:CommandsParser.CommandContext):
        pass

    # Exit a parse tree produced by CommandsParser#command.
    def exitCommand(self, ctx:CommandsParser.CommandContext):
        pass


    # Enter a parse tree produced by CommandsParser#helpAllCommand.
    def enterHelpAllCommand(self, ctx:CommandsParser.HelpAllCommandContext):
        pass

    # Exit a parse tree produced by CommandsParser#helpAllCommand.
    def exitHelpAllCommand(self, ctx:CommandsParser.HelpAllCommandContext):
        pass


    # Enter a parse tree produced by CommandsParser#helpOneCommand.
    def enterHelpOneCommand(self, ctx:CommandsParser.HelpOneCommandContext):
        pass

    # Exit a parse tree produced by CommandsParser#helpOneCommand.
    def exitHelpOneCommand(self, ctx:CommandsParser.HelpOneCommandContext):
        pass


    # Enter a parse tree produced by CommandsParser#rconCommand.
    def enterRconCommand(self, ctx:CommandsParser.RconCommandContext):
        pass

    # Exit a parse tree produced by CommandsParser#rconCommand.
    def exitRconCommand(self, ctx:CommandsParser.RconCommandContext):
        pass


    # Enter a parse tree produced by CommandsParser#killMeCommand.
    def enterKillMeCommand(self, ctx:CommandsParser.KillMeCommandContext):
        pass

    # Exit a parse tree produced by CommandsParser#killMeCommand.
    def exitKillMeCommand(self, ctx:CommandsParser.KillMeCommandContext):
        pass


    # Enter a parse tree produced by CommandsParser#killPlayerCommand.
    def enterKillPlayerCommand(self, ctx:CommandsParser.KillPlayerCommandContext):
        pass

    # Exit a parse tree produced by CommandsParser#killPlayerCommand.
    def exitKillPlayerCommand(self, ctx:CommandsParser.KillPlayerCommandContext):
        pass


    # Enter a parse tree produced by CommandsParser#clientValue.
    def enterClientValue(self, ctx:CommandsParser.ClientValueContext):
        pass

    # Exit a parse tree produced by CommandsParser#clientValue.
    def exitClientValue(self, ctx:CommandsParser.ClientValueContext):
        pass


    # Enter a parse tree produced by CommandsParser#intValue.
    def enterIntValue(self, ctx:CommandsParser.IntValueContext):
        pass

    # Exit a parse tree produced by CommandsParser#intValue.
    def exitIntValue(self, ctx:CommandsParser.IntValueContext):
        pass


    # Enter a parse tree produced by CommandsParser#manyButWhitespace.
    def enterManyButWhitespace(self, ctx:CommandsParser.ManyButWhitespaceContext):
        pass

    # Exit a parse tree produced by CommandsParser#manyButWhitespace.
    def exitManyButWhitespace(self, ctx:CommandsParser.ManyButWhitespaceContext):
        pass


    # Enter a parse tree produced by CommandsParser#manyButDoubleQuote.
    def enterManyButDoubleQuote(self, ctx:CommandsParser.ManyButDoubleQuoteContext):
        pass

    # Exit a parse tree produced by CommandsParser#manyButDoubleQuote.
    def exitManyButDoubleQuote(self, ctx:CommandsParser.ManyButDoubleQuoteContext):
        pass


    # Enter a parse tree produced by CommandsParser#manyButNewLine.
    def enterManyButNewLine(self, ctx:CommandsParser.ManyButNewLineContext):
        pass

    # Exit a parse tree produced by CommandsParser#manyButNewLine.
    def exitManyButNewLine(self, ctx:CommandsParser.ManyButNewLineContext):
        pass



del CommandsParser