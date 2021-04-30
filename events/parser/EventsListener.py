# Generated from events/parser/Events.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .EventsParser import EventsParser
else:
    from EventsParser import EventsParser
from events.models import *

# This class defines a complete listener for a parse tree produced by EventsParser.
class EventsListener(ParseTreeListener):

    # Enter a parse tree produced by EventsParser#events.
    def enterEvents(self, ctx:EventsParser.EventsContext):
        pass

    # Exit a parse tree produced by EventsParser#events.
    def exitEvents(self, ctx:EventsParser.EventsContext):
        pass


    # Enter a parse tree produced by EventsParser#event.
    def enterEvent(self, ctx:EventsParser.EventContext):
        pass

    # Exit a parse tree produced by EventsParser#event.
    def exitEvent(self, ctx:EventsParser.EventContext):
        pass


    # Enter a parse tree produced by EventsParser#eventTime.
    def enterEventTime(self, ctx:EventsParser.EventTimeContext):
        pass

    # Exit a parse tree produced by EventsParser#eventTime.
    def exitEventTime(self, ctx:EventsParser.EventTimeContext):
        pass


    # Enter a parse tree produced by EventsParser#separatorEvent.
    def enterSeparatorEvent(self, ctx:EventsParser.SeparatorEventContext):
        pass

    # Exit a parse tree produced by EventsParser#separatorEvent.
    def exitSeparatorEvent(self, ctx:EventsParser.SeparatorEventContext):
        pass


    # Enter a parse tree produced by EventsParser#initGameEvent.
    def enterInitGameEvent(self, ctx:EventsParser.InitGameEventContext):
        pass

    # Exit a parse tree produced by EventsParser#initGameEvent.
    def exitInitGameEvent(self, ctx:EventsParser.InitGameEventContext):
        pass


    # Enter a parse tree produced by EventsParser#initRoundEvent.
    def enterInitRoundEvent(self, ctx:EventsParser.InitRoundEventContext):
        pass

    # Exit a parse tree produced by EventsParser#initRoundEvent.
    def exitInitRoundEvent(self, ctx:EventsParser.InitRoundEventContext):
        pass


    # Enter a parse tree produced by EventsParser#initAuthEvent.
    def enterInitAuthEvent(self, ctx:EventsParser.InitAuthEventContext):
        pass

    # Exit a parse tree produced by EventsParser#initAuthEvent.
    def exitInitAuthEvent(self, ctx:EventsParser.InitAuthEventContext):
        pass


    # Enter a parse tree produced by EventsParser#shutdownGameEvent.
    def enterShutdownGameEvent(self, ctx:EventsParser.ShutdownGameEventContext):
        pass

    # Exit a parse tree produced by EventsParser#shutdownGameEvent.
    def exitShutdownGameEvent(self, ctx:EventsParser.ShutdownGameEventContext):
        pass


    # Enter a parse tree produced by EventsParser#warmupEvent.
    def enterWarmupEvent(self, ctx:EventsParser.WarmupEventContext):
        pass

    # Exit a parse tree produced by EventsParser#warmupEvent.
    def exitWarmupEvent(self, ctx:EventsParser.WarmupEventContext):
        pass


    # Enter a parse tree produced by EventsParser#sessionDataInitEvent.
    def enterSessionDataInitEvent(self, ctx:EventsParser.SessionDataInitEventContext):
        pass

    # Exit a parse tree produced by EventsParser#sessionDataInitEvent.
    def exitSessionDataInitEvent(self, ctx:EventsParser.SessionDataInitEventContext):
        pass


    # Enter a parse tree produced by EventsParser#clientConnectEvent.
    def enterClientConnectEvent(self, ctx:EventsParser.ClientConnectEventContext):
        pass

    # Exit a parse tree produced by EventsParser#clientConnectEvent.
    def exitClientConnectEvent(self, ctx:EventsParser.ClientConnectEventContext):
        pass


    # Enter a parse tree produced by EventsParser#clientDisconnectEvent.
    def enterClientDisconnectEvent(self, ctx:EventsParser.ClientDisconnectEventContext):
        pass

    # Exit a parse tree produced by EventsParser#clientDisconnectEvent.
    def exitClientDisconnectEvent(self, ctx:EventsParser.ClientDisconnectEventContext):
        pass


    # Enter a parse tree produced by EventsParser#clientBeginEvent.
    def enterClientBeginEvent(self, ctx:EventsParser.ClientBeginEventContext):
        pass

    # Exit a parse tree produced by EventsParser#clientBeginEvent.
    def exitClientBeginEvent(self, ctx:EventsParser.ClientBeginEventContext):
        pass


    # Enter a parse tree produced by EventsParser#clientSpawnEvent.
    def enterClientSpawnEvent(self, ctx:EventsParser.ClientSpawnEventContext):
        pass

    # Exit a parse tree produced by EventsParser#clientSpawnEvent.
    def exitClientSpawnEvent(self, ctx:EventsParser.ClientSpawnEventContext):
        pass


    # Enter a parse tree produced by EventsParser#clientUserinfoEvent.
    def enterClientUserinfoEvent(self, ctx:EventsParser.ClientUserinfoEventContext):
        pass

    # Exit a parse tree produced by EventsParser#clientUserinfoEvent.
    def exitClientUserinfoEvent(self, ctx:EventsParser.ClientUserinfoEventContext):
        pass


    # Enter a parse tree produced by EventsParser#clientUserinfoChangedEvent.
    def enterClientUserinfoChangedEvent(self, ctx:EventsParser.ClientUserinfoChangedEventContext):
        pass

    # Exit a parse tree produced by EventsParser#clientUserinfoChangedEvent.
    def exitClientUserinfoChangedEvent(self, ctx:EventsParser.ClientUserinfoChangedEventContext):
        pass


    # Enter a parse tree produced by EventsParser#accountValidatedEvent.
    def enterAccountValidatedEvent(self, ctx:EventsParser.AccountValidatedEventContext):
        pass

    # Exit a parse tree produced by EventsParser#accountValidatedEvent.
    def exitAccountValidatedEvent(self, ctx:EventsParser.AccountValidatedEventContext):
        pass


    # Enter a parse tree produced by EventsParser#sayEvent.
    def enterSayEvent(self, ctx:EventsParser.SayEventContext):
        pass

    # Exit a parse tree produced by EventsParser#sayEvent.
    def exitSayEvent(self, ctx:EventsParser.SayEventContext):
        pass


    # Enter a parse tree produced by EventsParser#sayTellEvent.
    def enterSayTellEvent(self, ctx:EventsParser.SayTellEventContext):
        pass

    # Exit a parse tree produced by EventsParser#sayTellEvent.
    def exitSayTellEvent(self, ctx:EventsParser.SayTellEventContext):
        pass


    # Enter a parse tree produced by EventsParser#sayTeamEvent.
    def enterSayTeamEvent(self, ctx:EventsParser.SayTeamEventContext):
        pass

    # Exit a parse tree produced by EventsParser#sayTeamEvent.
    def exitSayTeamEvent(self, ctx:EventsParser.SayTeamEventContext):
        pass


    # Enter a parse tree produced by EventsParser#tellEvent.
    def enterTellEvent(self, ctx:EventsParser.TellEventContext):
        pass

    # Exit a parse tree produced by EventsParser#tellEvent.
    def exitTellEvent(self, ctx:EventsParser.TellEventContext):
        pass


    # Enter a parse tree produced by EventsParser#radioEvent.
    def enterRadioEvent(self, ctx:EventsParser.RadioEventContext):
        pass

    # Exit a parse tree produced by EventsParser#radioEvent.
    def exitRadioEvent(self, ctx:EventsParser.RadioEventContext):
        pass


    # Enter a parse tree produced by EventsParser#killEvent.
    def enterKillEvent(self, ctx:EventsParser.KillEventContext):
        pass

    # Exit a parse tree produced by EventsParser#killEvent.
    def exitKillEvent(self, ctx:EventsParser.KillEventContext):
        pass


    # Enter a parse tree produced by EventsParser#itemEvent.
    def enterItemEvent(self, ctx:EventsParser.ItemEventContext):
        pass

    # Exit a parse tree produced by EventsParser#itemEvent.
    def exitItemEvent(self, ctx:EventsParser.ItemEventContext):
        pass


    # Enter a parse tree produced by EventsParser#flagEvent.
    def enterFlagEvent(self, ctx:EventsParser.FlagEventContext):
        pass

    # Exit a parse tree produced by EventsParser#flagEvent.
    def exitFlagEvent(self, ctx:EventsParser.FlagEventContext):
        pass


    # Enter a parse tree produced by EventsParser#flagCaptureTimeEvent.
    def enterFlagCaptureTimeEvent(self, ctx:EventsParser.FlagCaptureTimeEventContext):
        pass

    # Exit a parse tree produced by EventsParser#flagCaptureTimeEvent.
    def exitFlagCaptureTimeEvent(self, ctx:EventsParser.FlagCaptureTimeEventContext):
        pass


    # Enter a parse tree produced by EventsParser#flagReturnEvent.
    def enterFlagReturnEvent(self, ctx:EventsParser.FlagReturnEventContext):
        pass

    # Exit a parse tree produced by EventsParser#flagReturnEvent.
    def exitFlagReturnEvent(self, ctx:EventsParser.FlagReturnEventContext):
        pass


    # Enter a parse tree produced by EventsParser#intValue.
    def enterIntValue(self, ctx:EventsParser.IntValueContext):
        pass

    # Exit a parse tree produced by EventsParser#intValue.
    def exitIntValue(self, ctx:EventsParser.IntValueContext):
        pass


    # Enter a parse tree produced by EventsParser#manyButNewLine.
    def enterManyButNewLine(self, ctx:EventsParser.ManyButNewLineContext):
        pass

    # Exit a parse tree produced by EventsParser#manyButNewLine.
    def exitManyButNewLine(self, ctx:EventsParser.ManyButNewLineContext):
        pass


    # Enter a parse tree produced by EventsParser#manyButWhitespace.
    def enterManyButWhitespace(self, ctx:EventsParser.ManyButWhitespaceContext):
        pass

    # Exit a parse tree produced by EventsParser#manyButWhitespace.
    def exitManyButWhitespace(self, ctx:EventsParser.ManyButWhitespaceContext):
        pass


    # Enter a parse tree produced by EventsParser#manyButBackSlash.
    def enterManyButBackSlash(self, ctx:EventsParser.ManyButBackSlashContext):
        pass

    # Exit a parse tree produced by EventsParser#manyButBackSlash.
    def exitManyButBackSlash(self, ctx:EventsParser.ManyButBackSlashContext):
        pass


    # Enter a parse tree produced by EventsParser#manyButBackSlashOrNewLine.
    def enterManyButBackSlashOrNewLine(self, ctx:EventsParser.ManyButBackSlashOrNewLineContext):
        pass

    # Exit a parse tree produced by EventsParser#manyButBackSlashOrNewLine.
    def exitManyButBackSlashOrNewLine(self, ctx:EventsParser.ManyButBackSlashOrNewLineContext):
        pass


    # Enter a parse tree produced by EventsParser#manyButDoubleQuote.
    def enterManyButDoubleQuote(self, ctx:EventsParser.ManyButDoubleQuoteContext):
        pass

    # Exit a parse tree produced by EventsParser#manyButDoubleQuote.
    def exitManyButDoubleQuote(self, ctx:EventsParser.ManyButDoubleQuoteContext):
        pass



del EventsParser