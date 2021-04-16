// Generated from d:\Dev\Repos\u005Curbanterror-bot\events_parser\Events.g4 by ANTLR 4.8
from events import *
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class EventsParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		SEPARATOR=1, INITGAME=2, INITROUND=3, INITAUTH=4, SHUTDOWNGAME=5, WARMUP=6, 
		SESSION_DATA_INITIALISED=7, CLIENTCONNECT=8, CLIENTDISCONNECT=9, CLIENTBEGIN=10, 
		CLIENTSPAWN=11, CLIENTUSERINFO=12, CLIENTUSERINFOCHANGED=13, ACCOUNTVALIDATED=14, 
		SAY=15, SAYTELL=16, SAYTEAM=17, TELL=18, KILL=19, ITEM=20, FLAG=21, FLAGCAPTURETIME=22, 
		BACK_SLASH=23, SLASH=24, COMMA=25, INFERIOR=26, SUPERIOR=27, COLON=28, 
		SEMICOLON=29, DOT=30, UNDERSCORE=31, MINUS=32, PLUS=33, DOUBLE_QUOTE=34, 
		ROUND_BRACKET_LEFT=35, ROUND_BRACKET_RIGHT=36, SQUARE_BRACKET_LEFT=37, 
		SQUARE_BRACKET_RIGHT=38, WHITESPACE=39, NEWLINE=40, LETTER=41, DIGIT=42;
	public static final int
		RULE_events = 0, RULE_event = 1, RULE_separatorEvent = 2, RULE_initGameEvent = 3, 
		RULE_initRoundEvent = 4, RULE_initAuthEvent = 5, RULE_shutdownGameEvent = 6, 
		RULE_warmupEvent = 7, RULE_sessionDataInitEvent = 8, RULE_clientConnectEvent = 9, 
		RULE_clientDisconnectEvent = 10, RULE_clientBeginEvent = 11, RULE_clientSpawnEvent = 12, 
		RULE_clientUserinfoEvent = 13, RULE_clientUserinfoChangedEvent = 14, RULE_accountValidatedEvent = 15, 
		RULE_sayEvent = 16, RULE_sayTellEvent = 17, RULE_sayTeamEvent = 18, RULE_tellEvent = 19, 
		RULE_killEvent = 20, RULE_itemEvent = 21, RULE_flagEvent = 22, RULE_flagCaptureTimeEvent = 23, 
		RULE_intValue = 24, RULE_wordValue = 25, RULE_sentenceValue = 26;
	private static String[] makeRuleNames() {
		return new String[] {
			"events", "event", "separatorEvent", "initGameEvent", "initRoundEvent", 
			"initAuthEvent", "shutdownGameEvent", "warmupEvent", "sessionDataInitEvent", 
			"clientConnectEvent", "clientDisconnectEvent", "clientBeginEvent", "clientSpawnEvent", 
			"clientUserinfoEvent", "clientUserinfoChangedEvent", "accountValidatedEvent", 
			"sayEvent", "sayTellEvent", "sayTeamEvent", "tellEvent", "killEvent", 
			"itemEvent", "flagEvent", "flagCaptureTimeEvent", "intValue", "wordValue", 
			"sentenceValue"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'------------------------------------------------------------'", 
			"'InitGame:'", "'InitRound:'", "'InitAuth:'", "'ShutdownGame:'", "'Warmup:'", 
			"'Session data initialised for client on slot'", "'ClientConnect:'", 
			"'ClientDisconnect:'", "'ClientBegin:'", "'ClientSpawn:'", "'ClientUserinfo:'", 
			"'ClientUserinfoChanged:'", "'AccountValidated:'", "'say:'", "'saytell:'", 
			"'sayteam:'", "'tell:'", "'Kill:'", "'Item:'", "'Flag:'", "'FlagCaptureTime:'", 
			"'\\'", "'/'", "','", "'<'", "'>'", "':'", "';'", "'.'", "'_'", "'-'", 
			"'+'", "'\"'", "'('", "')'", "'['", "']'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "SEPARATOR", "INITGAME", "INITROUND", "INITAUTH", "SHUTDOWNGAME", 
			"WARMUP", "SESSION_DATA_INITIALISED", "CLIENTCONNECT", "CLIENTDISCONNECT", 
			"CLIENTBEGIN", "CLIENTSPAWN", "CLIENTUSERINFO", "CLIENTUSERINFOCHANGED", 
			"ACCOUNTVALIDATED", "SAY", "SAYTELL", "SAYTEAM", "TELL", "KILL", "ITEM", 
			"FLAG", "FLAGCAPTURETIME", "BACK_SLASH", "SLASH", "COMMA", "INFERIOR", 
			"SUPERIOR", "COLON", "SEMICOLON", "DOT", "UNDERSCORE", "MINUS", "PLUS", 
			"DOUBLE_QUOTE", "ROUND_BRACKET_LEFT", "ROUND_BRACKET_RIGHT", "SQUARE_BRACKET_LEFT", 
			"SQUARE_BRACKET_RIGHT", "WHITESPACE", "NEWLINE", "LETTER", "DIGIT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Events.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public EventsParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class EventsContext extends ParserRuleContext {
		public  value;
		public EventContext a;
		public List<EventContext> event() {
			return getRuleContexts(EventContext.class);
		}
		public EventContext event(int i) {
			return getRuleContext(EventContext.class,i);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(EventsParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(EventsParser.NEWLINE, i);
		}
		public EventsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_events; }
	}

	public final EventsContext events() throws RecognitionException {
		EventsContext _localctx = new EventsContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_events);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			_localctx.value = []
			setState(62);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << MINUS) | (1L << WHITESPACE) | (1L << DIGIT))) != 0)) {
				{
				{
				setState(55);
				((EventsContext)_localctx).a = event();
				_localctx.value.append(((EventsContext)_localctx).a.value)
				setState(58);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==NEWLINE) {
					{
					setState(57);
					match(NEWLINE);
					}
				}

				}
				}
				setState(64);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class EventContext extends ParserRuleContext {
		public  value;
		public IntValueContext a;
		public IntValueContext b;
		public SeparatorEventContext separatorEvt;
		public InitGameEventContext initGameEvt;
		public InitRoundEventContext initRoundEvt;
		public InitAuthEventContext initAuthEvt;
		public ShutdownGameEventContext shutdownGameEvt;
		public WarmupEventContext warmupEvt;
		public SessionDataInitEventContext sessionDataInitEvt;
		public ClientConnectEventContext clientConnectEvt;
		public ClientDisconnectEventContext clientDisconnectEvt;
		public ClientBeginEventContext clientBeginEvt;
		public ClientSpawnEventContext clientSpawnEvt;
		public ClientUserinfoEventContext clientUserinfoEvt;
		public ClientUserinfoChangedEventContext clientUserinfoChangedEvt;
		public AccountValidatedEventContext accountValidatedEvt;
		public SayEventContext sayEvt;
		public SayTellEventContext sayTellEvt;
		public SayTeamEventContext sayTeamEvt;
		public TellEventContext tellEvt;
		public KillEventContext killEvt;
		public ItemEventContext itemEvt;
		public FlagEventContext flagEvt;
		public FlagCaptureTimeEventContext flagCaptureTimeEvt;
		public TerminalNode COLON() { return getToken(EventsParser.COLON, 0); }
		public List<TerminalNode> WHITESPACE() { return getTokens(EventsParser.WHITESPACE); }
		public TerminalNode WHITESPACE(int i) {
			return getToken(EventsParser.WHITESPACE, i);
		}
		public List<IntValueContext> intValue() {
			return getRuleContexts(IntValueContext.class);
		}
		public IntValueContext intValue(int i) {
			return getRuleContext(IntValueContext.class,i);
		}
		public SeparatorEventContext separatorEvent() {
			return getRuleContext(SeparatorEventContext.class,0);
		}
		public InitGameEventContext initGameEvent() {
			return getRuleContext(InitGameEventContext.class,0);
		}
		public InitRoundEventContext initRoundEvent() {
			return getRuleContext(InitRoundEventContext.class,0);
		}
		public InitAuthEventContext initAuthEvent() {
			return getRuleContext(InitAuthEventContext.class,0);
		}
		public ShutdownGameEventContext shutdownGameEvent() {
			return getRuleContext(ShutdownGameEventContext.class,0);
		}
		public WarmupEventContext warmupEvent() {
			return getRuleContext(WarmupEventContext.class,0);
		}
		public SessionDataInitEventContext sessionDataInitEvent() {
			return getRuleContext(SessionDataInitEventContext.class,0);
		}
		public ClientConnectEventContext clientConnectEvent() {
			return getRuleContext(ClientConnectEventContext.class,0);
		}
		public ClientDisconnectEventContext clientDisconnectEvent() {
			return getRuleContext(ClientDisconnectEventContext.class,0);
		}
		public ClientBeginEventContext clientBeginEvent() {
			return getRuleContext(ClientBeginEventContext.class,0);
		}
		public ClientSpawnEventContext clientSpawnEvent() {
			return getRuleContext(ClientSpawnEventContext.class,0);
		}
		public ClientUserinfoEventContext clientUserinfoEvent() {
			return getRuleContext(ClientUserinfoEventContext.class,0);
		}
		public ClientUserinfoChangedEventContext clientUserinfoChangedEvent() {
			return getRuleContext(ClientUserinfoChangedEventContext.class,0);
		}
		public AccountValidatedEventContext accountValidatedEvent() {
			return getRuleContext(AccountValidatedEventContext.class,0);
		}
		public SayEventContext sayEvent() {
			return getRuleContext(SayEventContext.class,0);
		}
		public SayTellEventContext sayTellEvent() {
			return getRuleContext(SayTellEventContext.class,0);
		}
		public SayTeamEventContext sayTeamEvent() {
			return getRuleContext(SayTeamEventContext.class,0);
		}
		public TellEventContext tellEvent() {
			return getRuleContext(TellEventContext.class,0);
		}
		public KillEventContext killEvent() {
			return getRuleContext(KillEventContext.class,0);
		}
		public ItemEventContext itemEvent() {
			return getRuleContext(ItemEventContext.class,0);
		}
		public FlagEventContext flagEvent() {
			return getRuleContext(FlagEventContext.class,0);
		}
		public FlagCaptureTimeEventContext flagCaptureTimeEvent() {
			return getRuleContext(FlagCaptureTimeEventContext.class,0);
		}
		public EventContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_event; }
	}

	public final EventContext event() throws RecognitionException {
		EventContext _localctx = new EventContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_event);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(68);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==WHITESPACE) {
				{
				{
				setState(65);
				match(WHITESPACE);
				}
				}
				setState(70);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(71);
			((EventContext)_localctx).a = intValue();
			setState(72);
			match(COLON);
			setState(73);
			((EventContext)_localctx).b = intValue();
			setState(74);
			match(WHITESPACE);
			setState(141);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				{
				setState(75);
				((EventContext)_localctx).separatorEvt = separatorEvent();
				_localctx.value = ((EventContext)_localctx).separatorEvt.value
				}
				break;
			case 2:
				{
				setState(78);
				((EventContext)_localctx).initGameEvt = initGameEvent();
				_localctx.value = ((EventContext)_localctx).initGameEvt.value
				}
				break;
			case 3:
				{
				setState(81);
				((EventContext)_localctx).initRoundEvt = initRoundEvent();
				_localctx.value = ((EventContext)_localctx).initRoundEvt.value
				}
				break;
			case 4:
				{
				setState(84);
				((EventContext)_localctx).initAuthEvt = initAuthEvent();
				_localctx.value = ((EventContext)_localctx).initAuthEvt.value
				}
				break;
			case 5:
				{
				setState(87);
				((EventContext)_localctx).shutdownGameEvt = shutdownGameEvent();
				_localctx.value = ((EventContext)_localctx).shutdownGameEvt.value
				}
				break;
			case 6:
				{
				setState(90);
				((EventContext)_localctx).warmupEvt = warmupEvent();
				_localctx.value = ((EventContext)_localctx).warmupEvt.value
				}
				break;
			case 7:
				{
				setState(93);
				((EventContext)_localctx).sessionDataInitEvt = sessionDataInitEvent();
				_localctx.value = ((EventContext)_localctx).sessionDataInitEvt.value
				}
				break;
			case 8:
				{
				setState(96);
				((EventContext)_localctx).clientConnectEvt = clientConnectEvent();
				_localctx.value = ((EventContext)_localctx).clientConnectEvt.value
				}
				break;
			case 9:
				{
				setState(99);
				((EventContext)_localctx).clientDisconnectEvt = clientDisconnectEvent();
				_localctx.value = ((EventContext)_localctx).clientDisconnectEvt.value
				}
				break;
			case 10:
				{
				setState(102);
				((EventContext)_localctx).clientBeginEvt = clientBeginEvent();
				_localctx.value = ((EventContext)_localctx).clientBeginEvt.value
				}
				break;
			case 11:
				{
				setState(105);
				((EventContext)_localctx).clientSpawnEvt = clientSpawnEvent();
				_localctx.value = ((EventContext)_localctx).clientSpawnEvt.value
				}
				break;
			case 12:
				{
				setState(108);
				((EventContext)_localctx).clientUserinfoEvt = clientUserinfoEvent();
				_localctx.value = ((EventContext)_localctx).clientUserinfoEvt.value
				}
				break;
			case 13:
				{
				setState(111);
				((EventContext)_localctx).clientUserinfoChangedEvt = clientUserinfoChangedEvent();
				_localctx.value = ((EventContext)_localctx).clientUserinfoChangedEvt.value
				}
				break;
			case 14:
				{
				setState(114);
				((EventContext)_localctx).accountValidatedEvt = accountValidatedEvent();
				_localctx.value = ((EventContext)_localctx).accountValidatedEvt.value
				}
				break;
			case 15:
				{
				setState(117);
				((EventContext)_localctx).sayEvt = sayEvent();
				_localctx.value = ((EventContext)_localctx).sayEvt.value
				}
				break;
			case 16:
				{
				setState(120);
				((EventContext)_localctx).sayTellEvt = sayTellEvent();
				_localctx.value = ((EventContext)_localctx).sayTellEvt.value
				}
				break;
			case 17:
				{
				setState(123);
				((EventContext)_localctx).sayTeamEvt = sayTeamEvent();
				_localctx.value = ((EventContext)_localctx).sayTeamEvt.value
				}
				break;
			case 18:
				{
				setState(126);
				((EventContext)_localctx).tellEvt = tellEvent();
				_localctx.value = ((EventContext)_localctx).tellEvt.value
				}
				break;
			case 19:
				{
				setState(129);
				((EventContext)_localctx).killEvt = killEvent();
				_localctx.value = ((EventContext)_localctx).killEvt.value
				}
				break;
			case 20:
				{
				setState(132);
				((EventContext)_localctx).itemEvt = itemEvent();
				_localctx.value = ((EventContext)_localctx).itemEvt.value
				}
				break;
			case 21:
				{
				setState(135);
				((EventContext)_localctx).flagEvt = flagEvent();
				_localctx.value = ((EventContext)_localctx).flagEvt.value
				}
				break;
			case 22:
				{
				setState(138);
				((EventContext)_localctx).flagCaptureTimeEvt = flagCaptureTimeEvent();
				_localctx.value = ((EventContext)_localctx).flagCaptureTimeEvt.value
				}
				break;
			}
			_localctx.value.minutes = int((((EventContext)_localctx).a!=null?_input.getText(((EventContext)_localctx).a.start,((EventContext)_localctx).a.stop):null))
			_localctx.value.seconds = int((((EventContext)_localctx).b!=null?_input.getText(((EventContext)_localctx).b.start,((EventContext)_localctx).b.stop):null))
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SeparatorEventContext extends ParserRuleContext {
		public  value;
		public TerminalNode SEPARATOR() { return getToken(EventsParser.SEPARATOR, 0); }
		public SeparatorEventContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_separatorEvent; }
	}

	public final SeparatorEventContext separatorEvent() throws RecognitionException {
		SeparatorEventContext _localctx = new SeparatorEventContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_separatorEvent);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(146);
			match(SEPARATOR);
			_localctx.value = SeparatorEvent()
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class InitGameEventContext extends ParserRuleContext {
		public  value;
		public WordValueContext a;
		public SentenceValueContext b;
		public TerminalNode INITGAME() { return getToken(EventsParser.INITGAME, 0); }
		public TerminalNode WHITESPACE() { return getToken(EventsParser.WHITESPACE, 0); }
		public List<TerminalNode> BACK_SLASH() { return getTokens(EventsParser.BACK_SLASH); }
		public TerminalNode BACK_SLASH(int i) {
			return getToken(EventsParser.BACK_SLASH, i);
		}
		public List<WordValueContext> wordValue() {
			return getRuleContexts(WordValueContext.class);
		}
		public WordValueContext wordValue(int i) {
			return getRuleContext(WordValueContext.class,i);
		}
		public List<SentenceValueContext> sentenceValue() {
			return getRuleContexts(SentenceValueContext.class);
		}
		public SentenceValueContext sentenceValue(int i) {
			return getRuleContext(SentenceValueContext.class,i);
		}
		public InitGameEventContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_initGameEvent; }
	}

	public final InitGameEventContext initGameEvent() throws RecognitionException {
		InitGameEventContext _localctx = new InitGameEventContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_initGameEvent);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(149);
			match(INITGAME);
			setState(150);
			match(WHITESPACE);
			_localctx.value = InitGameEvent()
			setState(158); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(152);
				match(BACK_SLASH);
				setState(153);
				((InitGameEventContext)_localctx).a = wordValue();
				setState(154);
				match(BACK_SLASH);
				setState(155);
				((InitGameEventContext)_localctx).b = sentenceValue();
				_localctx.value.parameters[(((InitGameEventContext)_localctx).a!=null?_input.getText(((InitGameEventContext)_localctx).a.start,((InitGameEventContext)_localctx).a.stop):null)]=(((InitGameEventContext)_localctx).b!=null?_input.getText(((InitGameEventContext)_localctx).b.start,((InitGameEventContext)_localctx).b.stop):null)
				}
				}
				setState(160); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==BACK_SLASH );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class InitRoundEventContext extends ParserRuleContext {
		public  value;
		public WordValueContext a;
		public SentenceValueContext b;
		public TerminalNode INITROUND() { return getToken(EventsParser.INITROUND, 0); }
		public TerminalNode WHITESPACE() { return getToken(EventsParser.WHITESPACE, 0); }
		public List<TerminalNode> BACK_SLASH() { return getTokens(EventsParser.BACK_SLASH); }
		public TerminalNode BACK_SLASH(int i) {
			return getToken(EventsParser.BACK_SLASH, i);
		}
		public List<WordValueContext> wordValue() {
			return getRuleContexts(WordValueContext.class);
		}
		public WordValueContext wordValue(int i) {
			return getRuleContext(WordValueContext.class,i);
		}
		public List<SentenceValueContext> sentenceValue() {
			return getRuleContexts(SentenceValueContext.class);
		}
		public SentenceValueContext sentenceValue(int i) {
			return getRuleContext(SentenceValueContext.class,i);
		}
		public InitRoundEventContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_initRoundEvent; }
	}

	public final InitRoundEventContext initRoundEvent() throws RecognitionException {
		InitRoundEventContext _localctx = new InitRoundEventContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_initRoundEvent);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(162);
			match(INITROUND);
			setState(163);
			match(WHITESPACE);
			_localctx.value = InitRoundEvent()
			setState(171); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(165);
				match(BACK_SLASH);
				setState(166);
				((InitRoundEventContext)_localctx).a = wordValue();
				setState(167);
				match(BACK_SLASH);
				setState(168);
				((InitRoundEventContext)_localctx).b = sentenceValue();
				_localctx.value.parameters[(((InitRoundEventContext)_localctx).a!=null?_input.getText(((InitRoundEventContext)_localctx).a.start,((InitRoundEventContext)_localctx).a.stop):null)]=(((InitRoundEventContext)_localctx).b!=null?_input.getText(((InitRoundEventContext)_localctx).b.start,((InitRoundEventContext)_localctx).b.stop):null)
				}
				}
				setState(173); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==BACK_SLASH );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class InitAuthEventContext extends ParserRuleContext {
		public  value;
		public WordValueContext a;
		public SentenceValueContext b;
		public TerminalNode INITAUTH() { return getToken(EventsParser.INITAUTH, 0); }
		public TerminalNode WHITESPACE() { return getToken(EventsParser.WHITESPACE, 0); }
		public List<TerminalNode> BACK_SLASH() { return getTokens(EventsParser.BACK_SLASH); }
		public TerminalNode BACK_SLASH(int i) {
			return getToken(EventsParser.BACK_SLASH, i);
		}
		public List<WordValueContext> wordValue() {
			return getRuleContexts(WordValueContext.class);
		}
		public WordValueContext wordValue(int i) {
			return getRuleContext(WordValueContext.class,i);
		}
		public List<SentenceValueContext> sentenceValue() {
			return getRuleContexts(SentenceValueContext.class);
		}
		public SentenceValueContext sentenceValue(int i) {
			return getRuleContext(SentenceValueContext.class,i);
		}
		public InitAuthEventContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_initAuthEvent; }
	}

	public final InitAuthEventContext initAuthEvent() throws RecognitionException {
		InitAuthEventContext _localctx = new InitAuthEventContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_initAuthEvent);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(175);
			match(INITAUTH);
			setState(176);
			match(WHITESPACE);
			_localctx.value = InitAuthEvent()
			setState(184); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(178);
				match(BACK_SLASH);
				setState(179);
				((InitAuthEventContext)_localctx).a = wordValue();
				setState(180);
				match(BACK_SLASH);
				setState(181);
				((InitAuthEventContext)_localctx).b = sentenceValue();
				_localctx.value.parameters[(((InitAuthEventContext)_localctx).a!=null?_input.getText(((InitAuthEventContext)_localctx).a.start,((InitAuthEventContext)_localctx).a.stop):null)]=(((InitAuthEventContext)_localctx).b!=null?_input.getText(((InitAuthEventContext)_localctx).b.start,((InitAuthEventContext)_localctx).b.stop):null)
				}
				}
				setState(186); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==BACK_SLASH );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ShutdownGameEventContext extends ParserRuleContext {
		public  value;
		public TerminalNode SHUTDOWNGAME() { return getToken(EventsParser.SHUTDOWNGAME, 0); }
		public ShutdownGameEventContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_shutdownGameEvent; }
	}

	public final ShutdownGameEventContext shutdownGameEvent() throws RecognitionException {
		ShutdownGameEventContext _localctx = new ShutdownGameEventContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_shutdownGameEvent);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(188);
			match(SHUTDOWNGAME);
			_localctx.value = ShutdownGameEvent()
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class WarmupEventContext extends ParserRuleContext {
		public  value;
		public TerminalNode WARMUP() { return getToken(EventsParser.WARMUP, 0); }
		public WarmupEventContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_warmupEvent; }
	}

	public final WarmupEventContext warmupEvent() throws RecognitionException {
		WarmupEventContext _localctx = new WarmupEventContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_warmupEvent);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(191);
			match(WARMUP);
			_localctx.value = WarmUpEvent()
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SessionDataInitEventContext extends ParserRuleContext {
		public  value;
		public IntValueContext a;
		public IntValueContext b;
		public TerminalNode SESSION_DATA_INITIALISED() { return getToken(EventsParser.SESSION_DATA_INITIALISED, 0); }
		public List<TerminalNode> WHITESPACE() { return getTokens(EventsParser.WHITESPACE); }
		public TerminalNode WHITESPACE(int i) {
			return getToken(EventsParser.WHITESPACE, i);
		}
		public WordValueContext wordValue() {
			return getRuleContext(WordValueContext.class,0);
		}
		public List<IntValueContext> intValue() {
			return getRuleContexts(IntValueContext.class);
		}
		public IntValueContext intValue(int i) {
			return getRuleContext(IntValueContext.class,i);
		}
		public SessionDataInitEventContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sessionDataInitEvent; }
	}

	public final SessionDataInitEventContext sessionDataInitEvent() throws RecognitionException {
		SessionDataInitEventContext _localctx = new SessionDataInitEventContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_sessionDataInitEvent);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(194);
			match(SESSION_DATA_INITIALISED);
			setState(195);
			match(WHITESPACE);
			setState(196);
			((SessionDataInitEventContext)_localctx).a = intValue();
			setState(197);
			match(WHITESPACE);
			setState(198);
			wordValue();
			setState(199);
			match(WHITESPACE);
			setState(200);
			((SessionDataInitEventContext)_localctx).b = intValue();
			_localctx.value = SessionDataInitialisedEvent()
			_localctx.value.slot=int((((SessionDataInitEventContext)_localctx).a!=null?_input.getText(((SessionDataInitEventContext)_localctx).a.start,((SessionDataInitEventContext)_localctx).a.stop):null))
			_localctx.value.unknown=int((((SessionDataInitEventContext)_localctx).b!=null?_input.getText(((SessionDataInitEventContext)_localctx).b.start,((SessionDataInitEventContext)_localctx).b.stop):null))
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ClientConnectEventContext extends ParserRuleContext {
		public  value;
		public IntValueContext a;
		public TerminalNode CLIENTCONNECT() { return getToken(EventsParser.CLIENTCONNECT, 0); }
		public TerminalNode WHITESPACE() { return getToken(EventsParser.WHITESPACE, 0); }
		public IntValueContext intValue() {
			return getRuleContext(IntValueContext.class,0);
		}
		public ClientConnectEventContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_clientConnectEvent; }
	}

	public final ClientConnectEventContext clientConnectEvent() throws RecognitionException {
		ClientConnectEventContext _localctx = new ClientConnectEventContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_clientConnectEvent);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(205);
			match(CLIENTCONNECT);
			setState(206);
			match(WHITESPACE);
			setState(207);
			((ClientConnectEventContext)_localctx).a = intValue();
			_localctx.value=ClientConnectEvent()
			_localctx.value.slot=int((((ClientConnectEventContext)_localctx).a!=null?_input.getText(((ClientConnectEventContext)_localctx).a.start,((ClientConnectEventContext)_localctx).a.stop):null))
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ClientDisconnectEventContext extends ParserRuleContext {
		public  value;
		public IntValueContext a;
		public TerminalNode CLIENTDISCONNECT() { return getToken(EventsParser.CLIENTDISCONNECT, 0); }
		public TerminalNode WHITESPACE() { return getToken(EventsParser.WHITESPACE, 0); }
		public IntValueContext intValue() {
			return getRuleContext(IntValueContext.class,0);
		}
		public ClientDisconnectEventContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_clientDisconnectEvent; }
	}

	public final ClientDisconnectEventContext clientDisconnectEvent() throws RecognitionException {
		ClientDisconnectEventContext _localctx = new ClientDisconnectEventContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_clientDisconnectEvent);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(211);
			match(CLIENTDISCONNECT);
			setState(212);
			match(WHITESPACE);
			setState(213);
			((ClientDisconnectEventContext)_localctx).a = intValue();
			_localctx.value=ClientDisconnectEvent()
			_localctx.value.slot=int((((ClientDisconnectEventContext)_localctx).a!=null?_input.getText(((ClientDisconnectEventContext)_localctx).a.start,((ClientDisconnectEventContext)_localctx).a.stop):null))
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ClientBeginEventContext extends ParserRuleContext {
		public  value;
		public IntValueContext a;
		public TerminalNode CLIENTBEGIN() { return getToken(EventsParser.CLIENTBEGIN, 0); }
		public TerminalNode WHITESPACE() { return getToken(EventsParser.WHITESPACE, 0); }
		public IntValueContext intValue() {
			return getRuleContext(IntValueContext.class,0);
		}
		public ClientBeginEventContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_clientBeginEvent; }
	}

	public final ClientBeginEventContext clientBeginEvent() throws RecognitionException {
		ClientBeginEventContext _localctx = new ClientBeginEventContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_clientBeginEvent);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(217);
			match(CLIENTBEGIN);
			setState(218);
			match(WHITESPACE);
			setState(219);
			((ClientBeginEventContext)_localctx).a = intValue();
			_localctx.value=ClientBeginEvent()
			_localctx.value.slot=int((((ClientBeginEventContext)_localctx).a!=null?_input.getText(((ClientBeginEventContext)_localctx).a.start,((ClientBeginEventContext)_localctx).a.stop):null))
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ClientSpawnEventContext extends ParserRuleContext {
		public  value;
		public IntValueContext a;
		public TerminalNode CLIENTSPAWN() { return getToken(EventsParser.CLIENTSPAWN, 0); }
		public TerminalNode WHITESPACE() { return getToken(EventsParser.WHITESPACE, 0); }
		public IntValueContext intValue() {
			return getRuleContext(IntValueContext.class,0);
		}
		public ClientSpawnEventContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_clientSpawnEvent; }
	}

	public final ClientSpawnEventContext clientSpawnEvent() throws RecognitionException {
		ClientSpawnEventContext _localctx = new ClientSpawnEventContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_clientSpawnEvent);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(223);
			match(CLIENTSPAWN);
			setState(224);
			match(WHITESPACE);
			setState(225);
			((ClientSpawnEventContext)_localctx).a = intValue();
			_localctx.value=ClientSpawnEvent()
			_localctx.value.slot=int((((ClientSpawnEventContext)_localctx).a!=null?_input.getText(((ClientSpawnEventContext)_localctx).a.start,((ClientSpawnEventContext)_localctx).a.stop):null))
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ClientUserinfoEventContext extends ParserRuleContext {
		public  value;
		public IntValueContext a;
		public WordValueContext b;
		public SentenceValueContext c;
		public TerminalNode CLIENTUSERINFO() { return getToken(EventsParser.CLIENTUSERINFO, 0); }
		public List<TerminalNode> WHITESPACE() { return getTokens(EventsParser.WHITESPACE); }
		public TerminalNode WHITESPACE(int i) {
			return getToken(EventsParser.WHITESPACE, i);
		}
		public IntValueContext intValue() {
			return getRuleContext(IntValueContext.class,0);
		}
		public List<TerminalNode> BACK_SLASH() { return getTokens(EventsParser.BACK_SLASH); }
		public TerminalNode BACK_SLASH(int i) {
			return getToken(EventsParser.BACK_SLASH, i);
		}
		public List<WordValueContext> wordValue() {
			return getRuleContexts(WordValueContext.class);
		}
		public WordValueContext wordValue(int i) {
			return getRuleContext(WordValueContext.class,i);
		}
		public List<SentenceValueContext> sentenceValue() {
			return getRuleContexts(SentenceValueContext.class);
		}
		public SentenceValueContext sentenceValue(int i) {
			return getRuleContext(SentenceValueContext.class,i);
		}
		public ClientUserinfoEventContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_clientUserinfoEvent; }
	}

	public final ClientUserinfoEventContext clientUserinfoEvent() throws RecognitionException {
		ClientUserinfoEventContext _localctx = new ClientUserinfoEventContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_clientUserinfoEvent);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(229);
			match(CLIENTUSERINFO);
			setState(230);
			match(WHITESPACE);
			setState(231);
			((ClientUserinfoEventContext)_localctx).a = intValue();
			setState(232);
			match(WHITESPACE);
			_localctx.value=ClientUserinfoEvent()
			_localctx.value.slot=int((((ClientUserinfoEventContext)_localctx).a!=null?_input.getText(((ClientUserinfoEventContext)_localctx).a.start,((ClientUserinfoEventContext)_localctx).a.stop):null))
			setState(241); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(235);
				match(BACK_SLASH);
				setState(236);
				((ClientUserinfoEventContext)_localctx).b = wordValue();
				setState(237);
				match(BACK_SLASH);
				setState(238);
				((ClientUserinfoEventContext)_localctx).c = sentenceValue();
				_localctx.value.parameters[(((ClientUserinfoEventContext)_localctx).b!=null?_input.getText(((ClientUserinfoEventContext)_localctx).b.start,((ClientUserinfoEventContext)_localctx).b.stop):null)]=(((ClientUserinfoEventContext)_localctx).c!=null?_input.getText(((ClientUserinfoEventContext)_localctx).c.start,((ClientUserinfoEventContext)_localctx).c.stop):null)
				}
				}
				setState(243); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==BACK_SLASH );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ClientUserinfoChangedEventContext extends ParserRuleContext {
		public  value;
		public IntValueContext a;
		public WordValueContext b;
		public SentenceValueContext c;
		public TerminalNode CLIENTUSERINFOCHANGED() { return getToken(EventsParser.CLIENTUSERINFOCHANGED, 0); }
		public List<TerminalNode> WHITESPACE() { return getTokens(EventsParser.WHITESPACE); }
		public TerminalNode WHITESPACE(int i) {
			return getToken(EventsParser.WHITESPACE, i);
		}
		public IntValueContext intValue() {
			return getRuleContext(IntValueContext.class,0);
		}
		public List<TerminalNode> BACK_SLASH() { return getTokens(EventsParser.BACK_SLASH); }
		public TerminalNode BACK_SLASH(int i) {
			return getToken(EventsParser.BACK_SLASH, i);
		}
		public List<WordValueContext> wordValue() {
			return getRuleContexts(WordValueContext.class);
		}
		public WordValueContext wordValue(int i) {
			return getRuleContext(WordValueContext.class,i);
		}
		public List<SentenceValueContext> sentenceValue() {
			return getRuleContexts(SentenceValueContext.class);
		}
		public SentenceValueContext sentenceValue(int i) {
			return getRuleContext(SentenceValueContext.class,i);
		}
		public ClientUserinfoChangedEventContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_clientUserinfoChangedEvent; }
	}

	public final ClientUserinfoChangedEventContext clientUserinfoChangedEvent() throws RecognitionException {
		ClientUserinfoChangedEventContext _localctx = new ClientUserinfoChangedEventContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_clientUserinfoChangedEvent);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(245);
			match(CLIENTUSERINFOCHANGED);
			setState(246);
			match(WHITESPACE);
			setState(247);
			((ClientUserinfoChangedEventContext)_localctx).a = intValue();
			setState(248);
			match(WHITESPACE);
			_localctx.value=ClientUserinfoChangedEvent()
			_localctx.value.slot=int((((ClientUserinfoChangedEventContext)_localctx).a!=null?_input.getText(((ClientUserinfoChangedEventContext)_localctx).a.start,((ClientUserinfoChangedEventContext)_localctx).a.stop):null))
			setState(261); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(252);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==BACK_SLASH) {
						{
						setState(251);
						match(BACK_SLASH);
						}
					}

					setState(254);
					((ClientUserinfoChangedEventContext)_localctx).b = wordValue();
					setState(255);
					match(BACK_SLASH);
					setState(257);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
					case 1:
						{
						setState(256);
						((ClientUserinfoChangedEventContext)_localctx).c = sentenceValue();
						}
						break;
					}
					_localctx.value.parameters[(((ClientUserinfoChangedEventContext)_localctx).b!=null?_input.getText(((ClientUserinfoChangedEventContext)_localctx).b.start,((ClientUserinfoChangedEventContext)_localctx).b.stop):null)]=(((ClientUserinfoChangedEventContext)_localctx).c!=null?_input.getText(((ClientUserinfoChangedEventContext)_localctx).c.start,((ClientUserinfoChangedEventContext)_localctx).c.stop):null)
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(263); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AccountValidatedEventContext extends ParserRuleContext {
		public  value;
		public IntValueContext a;
		public WordValueContext b;
		public IntValueContext c;
		public WordValueContext d;
		public TerminalNode ACCOUNTVALIDATED() { return getToken(EventsParser.ACCOUNTVALIDATED, 0); }
		public List<TerminalNode> WHITESPACE() { return getTokens(EventsParser.WHITESPACE); }
		public TerminalNode WHITESPACE(int i) {
			return getToken(EventsParser.WHITESPACE, i);
		}
		public List<TerminalNode> MINUS() { return getTokens(EventsParser.MINUS); }
		public TerminalNode MINUS(int i) {
			return getToken(EventsParser.MINUS, i);
		}
		public List<TerminalNode> DOUBLE_QUOTE() { return getTokens(EventsParser.DOUBLE_QUOTE); }
		public TerminalNode DOUBLE_QUOTE(int i) {
			return getToken(EventsParser.DOUBLE_QUOTE, i);
		}
		public List<IntValueContext> intValue() {
			return getRuleContexts(IntValueContext.class);
		}
		public IntValueContext intValue(int i) {
			return getRuleContext(IntValueContext.class,i);
		}
		public List<WordValueContext> wordValue() {
			return getRuleContexts(WordValueContext.class);
		}
		public WordValueContext wordValue(int i) {
			return getRuleContext(WordValueContext.class,i);
		}
		public AccountValidatedEventContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_accountValidatedEvent; }
	}

	public final AccountValidatedEventContext accountValidatedEvent() throws RecognitionException {
		AccountValidatedEventContext _localctx = new AccountValidatedEventContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_accountValidatedEvent);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			_localctx.value=AccountValidatedEvent()
			setState(266);
			match(ACCOUNTVALIDATED);
			setState(267);
			match(WHITESPACE);
			setState(268);
			((AccountValidatedEventContext)_localctx).a = intValue();
			setState(269);
			match(WHITESPACE);
			setState(270);
			match(MINUS);
			setState(271);
			match(WHITESPACE);
			setState(276);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				{
				setState(272);
				((AccountValidatedEventContext)_localctx).b = wordValue();
				_localctx.value.account=(((AccountValidatedEventContext)_localctx).b!=null?_input.getText(((AccountValidatedEventContext)_localctx).b.start,((AccountValidatedEventContext)_localctx).b.stop):null)
				setState(274);
				match(WHITESPACE);
				}
				break;
			}
			setState(278);
			match(MINUS);
			setState(279);
			match(WHITESPACE);
			setState(280);
			((AccountValidatedEventContext)_localctx).c = intValue();
			setState(281);
			match(WHITESPACE);
			setState(282);
			match(MINUS);
			setState(283);
			match(WHITESPACE);
			setState(284);
			match(DOUBLE_QUOTE);
			setState(288);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << SLASH) | (1L << COMMA) | (1L << INFERIOR) | (1L << SUPERIOR) | (1L << COLON) | (1L << SEMICOLON) | (1L << DOT) | (1L << UNDERSCORE) | (1L << MINUS) | (1L << PLUS) | (1L << ROUND_BRACKET_LEFT) | (1L << ROUND_BRACKET_RIGHT) | (1L << SQUARE_BRACKET_LEFT) | (1L << SQUARE_BRACKET_RIGHT) | (1L << LETTER) | (1L << DIGIT))) != 0)) {
				{
				setState(285);
				((AccountValidatedEventContext)_localctx).d = wordValue();
				_localctx.value.role=(((AccountValidatedEventContext)_localctx).d!=null?_input.getText(((AccountValidatedEventContext)_localctx).d.start,((AccountValidatedEventContext)_localctx).d.stop):null)
				}
			}

			setState(290);
			match(DOUBLE_QUOTE);
			_localctx.value.slot=int((((AccountValidatedEventContext)_localctx).a!=null?_input.getText(((AccountValidatedEventContext)_localctx).a.start,((AccountValidatedEventContext)_localctx).a.stop):null))
			_localctx.value.level=int((((AccountValidatedEventContext)_localctx).c!=null?_input.getText(((AccountValidatedEventContext)_localctx).c.start,((AccountValidatedEventContext)_localctx).c.stop):null))
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SayEventContext extends ParserRuleContext {
		public  value;
		public IntValueContext a;
		public WordValueContext b;
		public SentenceValueContext c;
		public TerminalNode SAY() { return getToken(EventsParser.SAY, 0); }
		public List<TerminalNode> WHITESPACE() { return getTokens(EventsParser.WHITESPACE); }
		public TerminalNode WHITESPACE(int i) {
			return getToken(EventsParser.WHITESPACE, i);
		}
		public TerminalNode COLON() { return getToken(EventsParser.COLON, 0); }
		public IntValueContext intValue() {
			return getRuleContext(IntValueContext.class,0);
		}
		public WordValueContext wordValue() {
			return getRuleContext(WordValueContext.class,0);
		}
		public SentenceValueContext sentenceValue() {
			return getRuleContext(SentenceValueContext.class,0);
		}
		public SayEventContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sayEvent; }
	}

	public final SayEventContext sayEvent() throws RecognitionException {
		SayEventContext _localctx = new SayEventContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_sayEvent);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(294);
			match(SAY);
			setState(295);
			match(WHITESPACE);
			setState(296);
			((SayEventContext)_localctx).a = intValue();
			setState(297);
			match(WHITESPACE);
			setState(298);
			((SayEventContext)_localctx).b = wordValue();
			setState(299);
			match(COLON);
			setState(300);
			match(WHITESPACE);
			setState(301);
			((SayEventContext)_localctx).c = sentenceValue();
			_localctx.value=SayEvent()
			_localctx.value.slot=int((((SayEventContext)_localctx).a!=null?_input.getText(((SayEventContext)_localctx).a.start,((SayEventContext)_localctx).a.stop):null))
			_localctx.value.sender=(((SayEventContext)_localctx).b!=null?_input.getText(((SayEventContext)_localctx).b.start,((SayEventContext)_localctx).b.stop):null)
			_localctx.value.message=(((SayEventContext)_localctx).c!=null?_input.getText(((SayEventContext)_localctx).c.start,((SayEventContext)_localctx).c.stop):null)
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SayTellEventContext extends ParserRuleContext {
		public  value;
		public IntValueContext a;
		public IntValueContext b;
		public WordValueContext c;
		public SentenceValueContext d;
		public TerminalNode SAYTELL() { return getToken(EventsParser.SAYTELL, 0); }
		public List<TerminalNode> WHITESPACE() { return getTokens(EventsParser.WHITESPACE); }
		public TerminalNode WHITESPACE(int i) {
			return getToken(EventsParser.WHITESPACE, i);
		}
		public TerminalNode COLON() { return getToken(EventsParser.COLON, 0); }
		public List<IntValueContext> intValue() {
			return getRuleContexts(IntValueContext.class);
		}
		public IntValueContext intValue(int i) {
			return getRuleContext(IntValueContext.class,i);
		}
		public WordValueContext wordValue() {
			return getRuleContext(WordValueContext.class,0);
		}
		public SentenceValueContext sentenceValue() {
			return getRuleContext(SentenceValueContext.class,0);
		}
		public SayTellEventContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sayTellEvent; }
	}

	public final SayTellEventContext sayTellEvent() throws RecognitionException {
		SayTellEventContext _localctx = new SayTellEventContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_sayTellEvent);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(307);
			match(SAYTELL);
			setState(308);
			match(WHITESPACE);
			setState(309);
			((SayTellEventContext)_localctx).a = intValue();
			setState(310);
			match(WHITESPACE);
			setState(311);
			((SayTellEventContext)_localctx).b = intValue();
			setState(312);
			match(WHITESPACE);
			setState(313);
			((SayTellEventContext)_localctx).c = wordValue();
			setState(314);
			match(COLON);
			setState(315);
			match(WHITESPACE);
			setState(316);
			((SayTellEventContext)_localctx).d = sentenceValue();
			_localctx.value=SayTellEvent()
			_localctx.value.slot=int((((SayTellEventContext)_localctx).a!=null?_input.getText(((SayTellEventContext)_localctx).a.start,((SayTellEventContext)_localctx).a.stop):null))
			_localctx.value.sender_slot=int((((SayTellEventContext)_localctx).b!=null?_input.getText(((SayTellEventContext)_localctx).b.start,((SayTellEventContext)_localctx).b.stop):null))
			_localctx.value.sender=(((SayTellEventContext)_localctx).c!=null?_input.getText(((SayTellEventContext)_localctx).c.start,((SayTellEventContext)_localctx).c.stop):null)
			_localctx.value.message=(((SayTellEventContext)_localctx).d!=null?_input.getText(((SayTellEventContext)_localctx).d.start,((SayTellEventContext)_localctx).d.stop):null)
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SayTeamEventContext extends ParserRuleContext {
		public  value;
		public IntValueContext a;
		public WordValueContext b;
		public SentenceValueContext c;
		public TerminalNode SAYTELL() { return getToken(EventsParser.SAYTELL, 0); }
		public List<TerminalNode> WHITESPACE() { return getTokens(EventsParser.WHITESPACE); }
		public TerminalNode WHITESPACE(int i) {
			return getToken(EventsParser.WHITESPACE, i);
		}
		public TerminalNode COLON() { return getToken(EventsParser.COLON, 0); }
		public IntValueContext intValue() {
			return getRuleContext(IntValueContext.class,0);
		}
		public WordValueContext wordValue() {
			return getRuleContext(WordValueContext.class,0);
		}
		public SentenceValueContext sentenceValue() {
			return getRuleContext(SentenceValueContext.class,0);
		}
		public SayTeamEventContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sayTeamEvent; }
	}

	public final SayTeamEventContext sayTeamEvent() throws RecognitionException {
		SayTeamEventContext _localctx = new SayTeamEventContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_sayTeamEvent);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(323);
			match(SAYTELL);
			setState(324);
			match(WHITESPACE);
			setState(325);
			((SayTeamEventContext)_localctx).a = intValue();
			setState(326);
			match(WHITESPACE);
			setState(327);
			((SayTeamEventContext)_localctx).b = wordValue();
			setState(328);
			match(COLON);
			setState(329);
			match(WHITESPACE);
			setState(330);
			((SayTeamEventContext)_localctx).c = sentenceValue();
			_localctx.value=SayTeamEvent()
			_localctx.value.slot=int((((SayTeamEventContext)_localctx).a!=null?_input.getText(((SayTeamEventContext)_localctx).a.start,((SayTeamEventContext)_localctx).a.stop):null))
			_localctx.value.sender=(((SayTeamEventContext)_localctx).b!=null?_input.getText(((SayTeamEventContext)_localctx).b.start,((SayTeamEventContext)_localctx).b.stop):null)
			_localctx.value.message=(((SayTeamEventContext)_localctx).c!=null?_input.getText(((SayTeamEventContext)_localctx).c.start,((SayTeamEventContext)_localctx).c.stop):null)
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TellEventContext extends ParserRuleContext {
		public  value;
		public WordValueContext a;
		public WordValueContext b;
		public SentenceValueContext c;
		public TerminalNode TELL() { return getToken(EventsParser.TELL, 0); }
		public List<TerminalNode> WHITESPACE() { return getTokens(EventsParser.WHITESPACE); }
		public TerminalNode WHITESPACE(int i) {
			return getToken(EventsParser.WHITESPACE, i);
		}
		public List<WordValueContext> wordValue() {
			return getRuleContexts(WordValueContext.class);
		}
		public WordValueContext wordValue(int i) {
			return getRuleContext(WordValueContext.class,i);
		}
		public TerminalNode COLON() { return getToken(EventsParser.COLON, 0); }
		public SentenceValueContext sentenceValue() {
			return getRuleContext(SentenceValueContext.class,0);
		}
		public TellEventContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tellEvent; }
	}

	public final TellEventContext tellEvent() throws RecognitionException {
		TellEventContext _localctx = new TellEventContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_tellEvent);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(336);
			match(TELL);
			setState(337);
			match(WHITESPACE);
			setState(338);
			((TellEventContext)_localctx).a = wordValue();
			setState(339);
			match(WHITESPACE);
			setState(340);
			wordValue();
			setState(341);
			match(WHITESPACE);
			setState(342);
			((TellEventContext)_localctx).b = wordValue();
			setState(343);
			match(COLON);
			setState(344);
			match(WHITESPACE);
			setState(345);
			((TellEventContext)_localctx).c = sentenceValue();
			_localctx.value=TellEvent()
			_localctx.value.sender=(((TellEventContext)_localctx).a!=null?_input.getText(((TellEventContext)_localctx).a.start,((TellEventContext)_localctx).a.stop):null)
			_localctx.value.target=(((TellEventContext)_localctx).b!=null?_input.getText(((TellEventContext)_localctx).b.start,((TellEventContext)_localctx).b.stop):null)
			_localctx.value.message=(((TellEventContext)_localctx).c!=null?_input.getText(((TellEventContext)_localctx).c.start,((TellEventContext)_localctx).c.stop):null)
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class KillEventContext extends ParserRuleContext {
		public  value;
		public IntValueContext a;
		public IntValueContext b;
		public IntValueContext c;
		public WordValueContext d;
		public WordValueContext e;
		public WordValueContext f;
		public TerminalNode KILL() { return getToken(EventsParser.KILL, 0); }
		public List<TerminalNode> WHITESPACE() { return getTokens(EventsParser.WHITESPACE); }
		public TerminalNode WHITESPACE(int i) {
			return getToken(EventsParser.WHITESPACE, i);
		}
		public TerminalNode COLON() { return getToken(EventsParser.COLON, 0); }
		public List<WordValueContext> wordValue() {
			return getRuleContexts(WordValueContext.class);
		}
		public WordValueContext wordValue(int i) {
			return getRuleContext(WordValueContext.class,i);
		}
		public List<IntValueContext> intValue() {
			return getRuleContexts(IntValueContext.class);
		}
		public IntValueContext intValue(int i) {
			return getRuleContext(IntValueContext.class,i);
		}
		public KillEventContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_killEvent; }
	}

	public final KillEventContext killEvent() throws RecognitionException {
		KillEventContext _localctx = new KillEventContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_killEvent);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(351);
			match(KILL);
			setState(352);
			match(WHITESPACE);
			setState(353);
			((KillEventContext)_localctx).a = intValue();
			setState(354);
			match(WHITESPACE);
			setState(355);
			((KillEventContext)_localctx).b = intValue();
			setState(356);
			match(WHITESPACE);
			setState(357);
			((KillEventContext)_localctx).c = intValue();
			setState(358);
			match(COLON);
			setState(359);
			match(WHITESPACE);
			setState(360);
			((KillEventContext)_localctx).d = wordValue();
			setState(361);
			match(WHITESPACE);
			setState(362);
			wordValue();
			setState(363);
			match(WHITESPACE);
			setState(364);
			((KillEventContext)_localctx).e = wordValue();
			setState(365);
			match(WHITESPACE);
			setState(366);
			wordValue();
			setState(367);
			match(WHITESPACE);
			setState(368);
			((KillEventContext)_localctx).f = wordValue();
			_localctx.value=KillEvent()
			_localctx.value.x=int((((KillEventContext)_localctx).a!=null?_input.getText(((KillEventContext)_localctx).a.start,((KillEventContext)_localctx).a.stop):null))
			_localctx.value.y=int((((KillEventContext)_localctx).b!=null?_input.getText(((KillEventContext)_localctx).b.start,((KillEventContext)_localctx).b.stop):null))
			_localctx.value.z=int((((KillEventContext)_localctx).c!=null?_input.getText(((KillEventContext)_localctx).c.start,((KillEventContext)_localctx).c.stop):null))
			_localctx.value.killer=(((KillEventContext)_localctx).d!=null?_input.getText(((KillEventContext)_localctx).d.start,((KillEventContext)_localctx).d.stop):null)
			_localctx.value.killed=(((KillEventContext)_localctx).e!=null?_input.getText(((KillEventContext)_localctx).e.start,((KillEventContext)_localctx).e.stop):null)
			_localctx.value.how=(((KillEventContext)_localctx).f!=null?_input.getText(((KillEventContext)_localctx).f.start,((KillEventContext)_localctx).f.stop):null)
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ItemEventContext extends ParserRuleContext {
		public  value;
		public IntValueContext a;
		public WordValueContext b;
		public TerminalNode ITEM() { return getToken(EventsParser.ITEM, 0); }
		public List<TerminalNode> WHITESPACE() { return getTokens(EventsParser.WHITESPACE); }
		public TerminalNode WHITESPACE(int i) {
			return getToken(EventsParser.WHITESPACE, i);
		}
		public IntValueContext intValue() {
			return getRuleContext(IntValueContext.class,0);
		}
		public WordValueContext wordValue() {
			return getRuleContext(WordValueContext.class,0);
		}
		public ItemEventContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_itemEvent; }
	}

	public final ItemEventContext itemEvent() throws RecognitionException {
		ItemEventContext _localctx = new ItemEventContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_itemEvent);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(377);
			match(ITEM);
			setState(378);
			match(WHITESPACE);
			setState(379);
			((ItemEventContext)_localctx).a = intValue();
			setState(380);
			match(WHITESPACE);
			setState(381);
			((ItemEventContext)_localctx).b = wordValue();
			_localctx.value=ItemEvent()
			_localctx.value.slot=int((((ItemEventContext)_localctx).a!=null?_input.getText(((ItemEventContext)_localctx).a.start,((ItemEventContext)_localctx).a.stop):null))
			_localctx.value.item=(((ItemEventContext)_localctx).b!=null?_input.getText(((ItemEventContext)_localctx).b.start,((ItemEventContext)_localctx).b.stop):null)
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FlagEventContext extends ParserRuleContext {
		public  value;
		public IntValueContext a;
		public IntValueContext b;
		public WordValueContext c;
		public TerminalNode FLAG() { return getToken(EventsParser.FLAG, 0); }
		public List<TerminalNode> WHITESPACE() { return getTokens(EventsParser.WHITESPACE); }
		public TerminalNode WHITESPACE(int i) {
			return getToken(EventsParser.WHITESPACE, i);
		}
		public TerminalNode COLON() { return getToken(EventsParser.COLON, 0); }
		public List<IntValueContext> intValue() {
			return getRuleContexts(IntValueContext.class);
		}
		public IntValueContext intValue(int i) {
			return getRuleContext(IntValueContext.class,i);
		}
		public WordValueContext wordValue() {
			return getRuleContext(WordValueContext.class,0);
		}
		public FlagEventContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_flagEvent; }
	}

	public final FlagEventContext flagEvent() throws RecognitionException {
		FlagEventContext _localctx = new FlagEventContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_flagEvent);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(386);
			match(FLAG);
			setState(387);
			match(WHITESPACE);
			setState(388);
			((FlagEventContext)_localctx).a = intValue();
			setState(389);
			match(WHITESPACE);
			setState(390);
			((FlagEventContext)_localctx).b = intValue();
			setState(391);
			match(COLON);
			setState(392);
			match(WHITESPACE);
			setState(393);
			((FlagEventContext)_localctx).c = wordValue();
			_localctx.value=FlagEvent()
			_localctx.value.slot=int((((FlagEventContext)_localctx).a!=null?_input.getText(((FlagEventContext)_localctx).a.start,((FlagEventContext)_localctx).a.stop):null))
			_localctx.value.num=int((((FlagEventContext)_localctx).b!=null?_input.getText(((FlagEventContext)_localctx).b.start,((FlagEventContext)_localctx).b.stop):null))
			_localctx.value.item=(((FlagEventContext)_localctx).c!=null?_input.getText(((FlagEventContext)_localctx).c.start,((FlagEventContext)_localctx).c.stop):null)
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FlagCaptureTimeEventContext extends ParserRuleContext {
		public  value;
		public IntValueContext a;
		public IntValueContext b;
		public TerminalNode FLAGCAPTURETIME() { return getToken(EventsParser.FLAGCAPTURETIME, 0); }
		public List<TerminalNode> WHITESPACE() { return getTokens(EventsParser.WHITESPACE); }
		public TerminalNode WHITESPACE(int i) {
			return getToken(EventsParser.WHITESPACE, i);
		}
		public TerminalNode COLON() { return getToken(EventsParser.COLON, 0); }
		public List<IntValueContext> intValue() {
			return getRuleContexts(IntValueContext.class);
		}
		public IntValueContext intValue(int i) {
			return getRuleContext(IntValueContext.class,i);
		}
		public FlagCaptureTimeEventContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_flagCaptureTimeEvent; }
	}

	public final FlagCaptureTimeEventContext flagCaptureTimeEvent() throws RecognitionException {
		FlagCaptureTimeEventContext _localctx = new FlagCaptureTimeEventContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_flagCaptureTimeEvent);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(399);
			match(FLAGCAPTURETIME);
			setState(400);
			match(WHITESPACE);
			setState(401);
			((FlagCaptureTimeEventContext)_localctx).a = intValue();
			setState(402);
			match(COLON);
			setState(403);
			match(WHITESPACE);
			setState(404);
			((FlagCaptureTimeEventContext)_localctx).b = intValue();
			_localctx.value=FlagCaptureTimeEvent()
			_localctx.value.slot=int((((FlagCaptureTimeEventContext)_localctx).a!=null?_input.getText(((FlagCaptureTimeEventContext)_localctx).a.start,((FlagCaptureTimeEventContext)_localctx).a.stop):null))
			_localctx.value.time=int((((FlagCaptureTimeEventContext)_localctx).b!=null?_input.getText(((FlagCaptureTimeEventContext)_localctx).b.start,((FlagCaptureTimeEventContext)_localctx).b.stop):null))
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IntValueContext extends ParserRuleContext {
		public TerminalNode MINUS() { return getToken(EventsParser.MINUS, 0); }
		public List<TerminalNode> DIGIT() { return getTokens(EventsParser.DIGIT); }
		public TerminalNode DIGIT(int i) {
			return getToken(EventsParser.DIGIT, i);
		}
		public IntValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_intValue; }
	}

	public final IntValueContext intValue() throws RecognitionException {
		IntValueContext _localctx = new IntValueContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_intValue);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(410);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==MINUS) {
				{
				setState(409);
				match(MINUS);
				}
			}

			setState(413); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(412);
					match(DIGIT);
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(415); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,14,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class WordValueContext extends ParserRuleContext {
		public List<TerminalNode> LETTER() { return getTokens(EventsParser.LETTER); }
		public TerminalNode LETTER(int i) {
			return getToken(EventsParser.LETTER, i);
		}
		public List<TerminalNode> DIGIT() { return getTokens(EventsParser.DIGIT); }
		public TerminalNode DIGIT(int i) {
			return getToken(EventsParser.DIGIT, i);
		}
		public List<TerminalNode> UNDERSCORE() { return getTokens(EventsParser.UNDERSCORE); }
		public TerminalNode UNDERSCORE(int i) {
			return getToken(EventsParser.UNDERSCORE, i);
		}
		public List<TerminalNode> MINUS() { return getTokens(EventsParser.MINUS); }
		public TerminalNode MINUS(int i) {
			return getToken(EventsParser.MINUS, i);
		}
		public List<TerminalNode> PLUS() { return getTokens(EventsParser.PLUS); }
		public TerminalNode PLUS(int i) {
			return getToken(EventsParser.PLUS, i);
		}
		public List<TerminalNode> ROUND_BRACKET_LEFT() { return getTokens(EventsParser.ROUND_BRACKET_LEFT); }
		public TerminalNode ROUND_BRACKET_LEFT(int i) {
			return getToken(EventsParser.ROUND_BRACKET_LEFT, i);
		}
		public List<TerminalNode> ROUND_BRACKET_RIGHT() { return getTokens(EventsParser.ROUND_BRACKET_RIGHT); }
		public TerminalNode ROUND_BRACKET_RIGHT(int i) {
			return getToken(EventsParser.ROUND_BRACKET_RIGHT, i);
		}
		public List<TerminalNode> SQUARE_BRACKET_LEFT() { return getTokens(EventsParser.SQUARE_BRACKET_LEFT); }
		public TerminalNode SQUARE_BRACKET_LEFT(int i) {
			return getToken(EventsParser.SQUARE_BRACKET_LEFT, i);
		}
		public List<TerminalNode> SQUARE_BRACKET_RIGHT() { return getTokens(EventsParser.SQUARE_BRACKET_RIGHT); }
		public TerminalNode SQUARE_BRACKET_RIGHT(int i) {
			return getToken(EventsParser.SQUARE_BRACKET_RIGHT, i);
		}
		public List<TerminalNode> SLASH() { return getTokens(EventsParser.SLASH); }
		public TerminalNode SLASH(int i) {
			return getToken(EventsParser.SLASH, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(EventsParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(EventsParser.COMMA, i);
		}
		public List<TerminalNode> COLON() { return getTokens(EventsParser.COLON); }
		public TerminalNode COLON(int i) {
			return getToken(EventsParser.COLON, i);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(EventsParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(EventsParser.SEMICOLON, i);
		}
		public List<TerminalNode> INFERIOR() { return getTokens(EventsParser.INFERIOR); }
		public TerminalNode INFERIOR(int i) {
			return getToken(EventsParser.INFERIOR, i);
		}
		public List<TerminalNode> SUPERIOR() { return getTokens(EventsParser.SUPERIOR); }
		public TerminalNode SUPERIOR(int i) {
			return getToken(EventsParser.SUPERIOR, i);
		}
		public List<TerminalNode> DOT() { return getTokens(EventsParser.DOT); }
		public TerminalNode DOT(int i) {
			return getToken(EventsParser.DOT, i);
		}
		public WordValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_wordValue; }
	}

	public final WordValueContext wordValue() throws RecognitionException {
		WordValueContext _localctx = new WordValueContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_wordValue);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(418); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(417);
					_la = _input.LA(1);
					if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << SLASH) | (1L << COMMA) | (1L << INFERIOR) | (1L << SUPERIOR) | (1L << COLON) | (1L << SEMICOLON) | (1L << DOT) | (1L << UNDERSCORE) | (1L << MINUS) | (1L << PLUS) | (1L << ROUND_BRACKET_LEFT) | (1L << ROUND_BRACKET_RIGHT) | (1L << SQUARE_BRACKET_LEFT) | (1L << SQUARE_BRACKET_RIGHT) | (1L << LETTER) | (1L << DIGIT))) != 0)) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(420); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,15,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SentenceValueContext extends ParserRuleContext {
		public List<WordValueContext> wordValue() {
			return getRuleContexts(WordValueContext.class);
		}
		public WordValueContext wordValue(int i) {
			return getRuleContext(WordValueContext.class,i);
		}
		public List<TerminalNode> WHITESPACE() { return getTokens(EventsParser.WHITESPACE); }
		public TerminalNode WHITESPACE(int i) {
			return getToken(EventsParser.WHITESPACE, i);
		}
		public SentenceValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sentenceValue; }
	}

	public final SentenceValueContext sentenceValue() throws RecognitionException {
		SentenceValueContext _localctx = new SentenceValueContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_sentenceValue);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(424); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					setState(424);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case SLASH:
					case COMMA:
					case INFERIOR:
					case SUPERIOR:
					case COLON:
					case SEMICOLON:
					case DOT:
					case UNDERSCORE:
					case MINUS:
					case PLUS:
					case ROUND_BRACKET_LEFT:
					case ROUND_BRACKET_RIGHT:
					case SQUARE_BRACKET_LEFT:
					case SQUARE_BRACKET_RIGHT:
					case LETTER:
					case DIGIT:
						{
						setState(422);
						wordValue();
						}
						break;
					case WHITESPACE:
						{
						setState(423);
						match(WHITESPACE);
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(426); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,17,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3,\u01af\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\3\2\3\2\3\2\3\2\5\2=\n\2\7\2?\n\2\f\2\16"+
		"\2B\13\2\3\3\7\3E\n\3\f\3\16\3H\13\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u0090\n\3\3\3\3\3\3\3\3\4\3\4"+
		"\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\6\5\u00a1\n\5\r\5\16\5\u00a2"+
		"\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\6\6\u00ae\n\6\r\6\16\6\u00af\3\7"+
		"\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\6\7\u00bb\n\7\r\7\16\7\u00bc\3\b\3\b"+
		"\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13"+
		"\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3"+
		"\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3"+
		"\17\3\17\3\17\3\17\6\17\u00f4\n\17\r\17\16\17\u00f5\3\20\3\20\3\20\3\20"+
		"\3\20\3\20\3\20\5\20\u00ff\n\20\3\20\3\20\3\20\5\20\u0104\n\20\3\20\3"+
		"\20\6\20\u0108\n\20\r\20\16\20\u0109\3\21\3\21\3\21\3\21\3\21\3\21\3\21"+
		"\3\21\3\21\3\21\3\21\5\21\u0117\n\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21"+
		"\3\21\3\21\3\21\5\21\u0123\n\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22"+
		"\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23"+
		"\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24"+
		"\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25"+
		"\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26"+
		"\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26"+
		"\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27"+
		"\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30"+
		"\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32"+
		"\5\32\u019d\n\32\3\32\6\32\u01a0\n\32\r\32\16\32\u01a1\3\33\6\33\u01a5"+
		"\n\33\r\33\16\33\u01a6\3\34\3\34\6\34\u01ab\n\34\r\34\16\34\u01ac\3\34"+
		"\2\2\35\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\66\2"+
		"\3\5\2\32#%(+,\2\u01b9\28\3\2\2\2\4F\3\2\2\2\6\u0094\3\2\2\2\b\u0097\3"+
		"\2\2\2\n\u00a4\3\2\2\2\f\u00b1\3\2\2\2\16\u00be\3\2\2\2\20\u00c1\3\2\2"+
		"\2\22\u00c4\3\2\2\2\24\u00cf\3\2\2\2\26\u00d5\3\2\2\2\30\u00db\3\2\2\2"+
		"\32\u00e1\3\2\2\2\34\u00e7\3\2\2\2\36\u00f7\3\2\2\2 \u010b\3\2\2\2\"\u0128"+
		"\3\2\2\2$\u0135\3\2\2\2&\u0145\3\2\2\2(\u0152\3\2\2\2*\u0161\3\2\2\2,"+
		"\u017b\3\2\2\2.\u0184\3\2\2\2\60\u0191\3\2\2\2\62\u019c\3\2\2\2\64\u01a4"+
		"\3\2\2\2\66\u01aa\3\2\2\28@\b\2\1\29:\5\4\3\2:<\b\2\1\2;=\7*\2\2<;\3\2"+
		"\2\2<=\3\2\2\2=?\3\2\2\2>9\3\2\2\2?B\3\2\2\2@>\3\2\2\2@A\3\2\2\2A\3\3"+
		"\2\2\2B@\3\2\2\2CE\7)\2\2DC\3\2\2\2EH\3\2\2\2FD\3\2\2\2FG\3\2\2\2GI\3"+
		"\2\2\2HF\3\2\2\2IJ\5\62\32\2JK\7\36\2\2KL\5\62\32\2L\u008f\7)\2\2MN\5"+
		"\6\4\2NO\b\3\1\2O\u0090\3\2\2\2PQ\5\b\5\2QR\b\3\1\2R\u0090\3\2\2\2ST\5"+
		"\n\6\2TU\b\3\1\2U\u0090\3\2\2\2VW\5\f\7\2WX\b\3\1\2X\u0090\3\2\2\2YZ\5"+
		"\16\b\2Z[\b\3\1\2[\u0090\3\2\2\2\\]\5\20\t\2]^\b\3\1\2^\u0090\3\2\2\2"+
		"_`\5\22\n\2`a\b\3\1\2a\u0090\3\2\2\2bc\5\24\13\2cd\b\3\1\2d\u0090\3\2"+
		"\2\2ef\5\26\f\2fg\b\3\1\2g\u0090\3\2\2\2hi\5\30\r\2ij\b\3\1\2j\u0090\3"+
		"\2\2\2kl\5\32\16\2lm\b\3\1\2m\u0090\3\2\2\2no\5\34\17\2op\b\3\1\2p\u0090"+
		"\3\2\2\2qr\5\36\20\2rs\b\3\1\2s\u0090\3\2\2\2tu\5 \21\2uv\b\3\1\2v\u0090"+
		"\3\2\2\2wx\5\"\22\2xy\b\3\1\2y\u0090\3\2\2\2z{\5$\23\2{|\b\3\1\2|\u0090"+
		"\3\2\2\2}~\5&\24\2~\177\b\3\1\2\177\u0090\3\2\2\2\u0080\u0081\5(\25\2"+
		"\u0081\u0082\b\3\1\2\u0082\u0090\3\2\2\2\u0083\u0084\5*\26\2\u0084\u0085"+
		"\b\3\1\2\u0085\u0090\3\2\2\2\u0086\u0087\5,\27\2\u0087\u0088\b\3\1\2\u0088"+
		"\u0090\3\2\2\2\u0089\u008a\5.\30\2\u008a\u008b\b\3\1\2\u008b\u0090\3\2"+
		"\2\2\u008c\u008d\5\60\31\2\u008d\u008e\b\3\1\2\u008e\u0090\3\2\2\2\u008f"+
		"M\3\2\2\2\u008fP\3\2\2\2\u008fS\3\2\2\2\u008fV\3\2\2\2\u008fY\3\2\2\2"+
		"\u008f\\\3\2\2\2\u008f_\3\2\2\2\u008fb\3\2\2\2\u008fe\3\2\2\2\u008fh\3"+
		"\2\2\2\u008fk\3\2\2\2\u008fn\3\2\2\2\u008fq\3\2\2\2\u008ft\3\2\2\2\u008f"+
		"w\3\2\2\2\u008fz\3\2\2\2\u008f}\3\2\2\2\u008f\u0080\3\2\2\2\u008f\u0083"+
		"\3\2\2\2\u008f\u0086\3\2\2\2\u008f\u0089\3\2\2\2\u008f\u008c\3\2\2\2\u0090"+
		"\u0091\3\2\2\2\u0091\u0092\b\3\1\2\u0092\u0093\b\3\1\2\u0093\5\3\2\2\2"+
		"\u0094\u0095\7\3\2\2\u0095\u0096\b\4\1\2\u0096\7\3\2\2\2\u0097\u0098\7"+
		"\4\2\2\u0098\u0099\7)\2\2\u0099\u00a0\b\5\1\2\u009a\u009b\7\31\2\2\u009b"+
		"\u009c\5\64\33\2\u009c\u009d\7\31\2\2\u009d\u009e\5\66\34\2\u009e\u009f"+
		"\b\5\1\2\u009f\u00a1\3\2\2\2\u00a0\u009a\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2"+
		"\u00a0\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\t\3\2\2\2\u00a4\u00a5\7\5\2\2"+
		"\u00a5\u00a6\7)\2\2\u00a6\u00ad\b\6\1\2\u00a7\u00a8\7\31\2\2\u00a8\u00a9"+
		"\5\64\33\2\u00a9\u00aa\7\31\2\2\u00aa\u00ab\5\66\34\2\u00ab\u00ac\b\6"+
		"\1\2\u00ac\u00ae\3\2\2\2\u00ad\u00a7\3\2\2\2\u00ae\u00af\3\2\2\2\u00af"+
		"\u00ad\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\13\3\2\2\2\u00b1\u00b2\7\6\2"+
		"\2\u00b2\u00b3\7)\2\2\u00b3\u00ba\b\7\1\2\u00b4\u00b5\7\31\2\2\u00b5\u00b6"+
		"\5\64\33\2\u00b6\u00b7\7\31\2\2\u00b7\u00b8\5\66\34\2\u00b8\u00b9\b\7"+
		"\1\2\u00b9\u00bb\3\2\2\2\u00ba\u00b4\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc"+
		"\u00ba\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\r\3\2\2\2\u00be\u00bf\7\7\2\2"+
		"\u00bf\u00c0\b\b\1\2\u00c0\17\3\2\2\2\u00c1\u00c2\7\b\2\2\u00c2\u00c3"+
		"\b\t\1\2\u00c3\21\3\2\2\2\u00c4\u00c5\7\t\2\2\u00c5\u00c6\7)\2\2\u00c6"+
		"\u00c7\5\62\32\2\u00c7\u00c8\7)\2\2\u00c8\u00c9\5\64\33\2\u00c9\u00ca"+
		"\7)\2\2\u00ca\u00cb\5\62\32\2\u00cb\u00cc\b\n\1\2\u00cc\u00cd\b\n\1\2"+
		"\u00cd\u00ce\b\n\1\2\u00ce\23\3\2\2\2\u00cf\u00d0\7\n\2\2\u00d0\u00d1"+
		"\7)\2\2\u00d1\u00d2\5\62\32\2\u00d2\u00d3\b\13\1\2\u00d3\u00d4\b\13\1"+
		"\2\u00d4\25\3\2\2\2\u00d5\u00d6\7\13\2\2\u00d6\u00d7\7)\2\2\u00d7\u00d8"+
		"\5\62\32\2\u00d8\u00d9\b\f\1\2\u00d9\u00da\b\f\1\2\u00da\27\3\2\2\2\u00db"+
		"\u00dc\7\f\2\2\u00dc\u00dd\7)\2\2\u00dd\u00de\5\62\32\2\u00de\u00df\b"+
		"\r\1\2\u00df\u00e0\b\r\1\2\u00e0\31\3\2\2\2\u00e1\u00e2\7\r\2\2\u00e2"+
		"\u00e3\7)\2\2\u00e3\u00e4\5\62\32\2\u00e4\u00e5\b\16\1\2\u00e5\u00e6\b"+
		"\16\1\2\u00e6\33\3\2\2\2\u00e7\u00e8\7\16\2\2\u00e8\u00e9\7)\2\2\u00e9"+
		"\u00ea\5\62\32\2\u00ea\u00eb\7)\2\2\u00eb\u00ec\b\17\1\2\u00ec\u00f3\b"+
		"\17\1\2\u00ed\u00ee\7\31\2\2\u00ee\u00ef\5\64\33\2\u00ef\u00f0\7\31\2"+
		"\2\u00f0\u00f1\5\66\34\2\u00f1\u00f2\b\17\1\2\u00f2\u00f4\3\2\2\2\u00f3"+
		"\u00ed\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00f3\3\2\2\2\u00f5\u00f6\3\2"+
		"\2\2\u00f6\35\3\2\2\2\u00f7\u00f8\7\17\2\2\u00f8\u00f9\7)\2\2\u00f9\u00fa"+
		"\5\62\32\2\u00fa\u00fb\7)\2\2\u00fb\u00fc\b\20\1\2\u00fc\u0107\b\20\1"+
		"\2\u00fd\u00ff\7\31\2\2\u00fe\u00fd\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff"+
		"\u0100\3\2\2\2\u0100\u0101\5\64\33\2\u0101\u0103\7\31\2\2\u0102\u0104"+
		"\5\66\34\2\u0103\u0102\3\2\2\2\u0103\u0104\3\2\2\2\u0104\u0105\3\2\2\2"+
		"\u0105\u0106\b\20\1\2\u0106\u0108\3\2\2\2\u0107\u00fe\3\2\2\2\u0108\u0109"+
		"\3\2\2\2\u0109\u0107\3\2\2\2\u0109\u010a\3\2\2\2\u010a\37\3\2\2\2\u010b"+
		"\u010c\b\21\1\2\u010c\u010d\7\20\2\2\u010d\u010e\7)\2\2\u010e\u010f\5"+
		"\62\32\2\u010f\u0110\7)\2\2\u0110\u0111\7\"\2\2\u0111\u0116\7)\2\2\u0112"+
		"\u0113\5\64\33\2\u0113\u0114\b\21\1\2\u0114\u0115\7)\2\2\u0115\u0117\3"+
		"\2\2\2\u0116\u0112\3\2\2\2\u0116\u0117\3\2\2\2\u0117\u0118\3\2\2\2\u0118"+
		"\u0119\7\"\2\2\u0119\u011a\7)\2\2\u011a\u011b\5\62\32\2\u011b\u011c\7"+
		")\2\2\u011c\u011d\7\"\2\2\u011d\u011e\7)\2\2\u011e\u0122\7$\2\2\u011f"+
		"\u0120\5\64\33\2\u0120\u0121\b\21\1\2\u0121\u0123\3\2\2\2\u0122\u011f"+
		"\3\2\2\2\u0122\u0123\3\2\2\2\u0123\u0124\3\2\2\2\u0124\u0125\7$\2\2\u0125"+
		"\u0126\b\21\1\2\u0126\u0127\b\21\1\2\u0127!\3\2\2\2\u0128\u0129\7\21\2"+
		"\2\u0129\u012a\7)\2\2\u012a\u012b\5\62\32\2\u012b\u012c\7)\2\2\u012c\u012d"+
		"\5\64\33\2\u012d\u012e\7\36\2\2\u012e\u012f\7)\2\2\u012f\u0130\5\66\34"+
		"\2\u0130\u0131\b\22\1\2\u0131\u0132\b\22\1\2\u0132\u0133\b\22\1\2\u0133"+
		"\u0134\b\22\1\2\u0134#\3\2\2\2\u0135\u0136\7\22\2\2\u0136\u0137\7)\2\2"+
		"\u0137\u0138\5\62\32\2\u0138\u0139\7)\2\2\u0139\u013a\5\62\32\2\u013a"+
		"\u013b\7)\2\2\u013b\u013c\5\64\33\2\u013c\u013d\7\36\2\2\u013d\u013e\7"+
		")\2\2\u013e\u013f\5\66\34\2\u013f\u0140\b\23\1\2\u0140\u0141\b\23\1\2"+
		"\u0141\u0142\b\23\1\2\u0142\u0143\b\23\1\2\u0143\u0144\b\23\1\2\u0144"+
		"%\3\2\2\2\u0145\u0146\7\22\2\2\u0146\u0147\7)\2\2\u0147\u0148\5\62\32"+
		"\2\u0148\u0149\7)\2\2\u0149\u014a\5\64\33\2\u014a\u014b\7\36\2\2\u014b"+
		"\u014c\7)\2\2\u014c\u014d\5\66\34\2\u014d\u014e\b\24\1\2\u014e\u014f\b"+
		"\24\1\2\u014f\u0150\b\24\1\2\u0150\u0151\b\24\1\2\u0151\'\3\2\2\2\u0152"+
		"\u0153\7\24\2\2\u0153\u0154\7)\2\2\u0154\u0155\5\64\33\2\u0155\u0156\7"+
		")\2\2\u0156\u0157\5\64\33\2\u0157\u0158\7)\2\2\u0158\u0159\5\64\33\2\u0159"+
		"\u015a\7\36\2\2\u015a\u015b\7)\2\2\u015b\u015c\5\66\34\2\u015c\u015d\b"+
		"\25\1\2\u015d\u015e\b\25\1\2\u015e\u015f\b\25\1\2\u015f\u0160\b\25\1\2"+
		"\u0160)\3\2\2\2\u0161\u0162\7\25\2\2\u0162\u0163\7)\2\2\u0163\u0164\5"+
		"\62\32\2\u0164\u0165\7)\2\2\u0165\u0166\5\62\32\2\u0166\u0167\7)\2\2\u0167"+
		"\u0168\5\62\32\2\u0168\u0169\7\36\2\2\u0169\u016a\7)\2\2\u016a\u016b\5"+
		"\64\33\2\u016b\u016c\7)\2\2\u016c\u016d\5\64\33\2\u016d\u016e\7)\2\2\u016e"+
		"\u016f\5\64\33\2\u016f\u0170\7)\2\2\u0170\u0171\5\64\33\2\u0171\u0172"+
		"\7)\2\2\u0172\u0173\5\64\33\2\u0173\u0174\b\26\1\2\u0174\u0175\b\26\1"+
		"\2\u0175\u0176\b\26\1\2\u0176\u0177\b\26\1\2\u0177\u0178\b\26\1\2\u0178"+
		"\u0179\b\26\1\2\u0179\u017a\b\26\1\2\u017a+\3\2\2\2\u017b\u017c\7\26\2"+
		"\2\u017c\u017d\7)\2\2\u017d\u017e\5\62\32\2\u017e\u017f\7)\2\2\u017f\u0180"+
		"\5\64\33\2\u0180\u0181\b\27\1\2\u0181\u0182\b\27\1\2\u0182\u0183\b\27"+
		"\1\2\u0183-\3\2\2\2\u0184\u0185\7\27\2\2\u0185\u0186\7)\2\2\u0186\u0187"+
		"\5\62\32\2\u0187\u0188\7)\2\2\u0188\u0189\5\62\32\2\u0189\u018a\7\36\2"+
		"\2\u018a\u018b\7)\2\2\u018b\u018c\5\64\33\2\u018c\u018d\b\30\1\2\u018d"+
		"\u018e\b\30\1\2\u018e\u018f\b\30\1\2\u018f\u0190\b\30\1\2\u0190/\3\2\2"+
		"\2\u0191\u0192\7\30\2\2\u0192\u0193\7)\2\2\u0193\u0194\5\62\32\2\u0194"+
		"\u0195\7\36\2\2\u0195\u0196\7)\2\2\u0196\u0197\5\62\32\2\u0197\u0198\b"+
		"\31\1\2\u0198\u0199\b\31\1\2\u0199\u019a\b\31\1\2\u019a\61\3\2\2\2\u019b"+
		"\u019d\7\"\2\2\u019c\u019b\3\2\2\2\u019c\u019d\3\2\2\2\u019d\u019f\3\2"+
		"\2\2\u019e\u01a0\7,\2\2\u019f\u019e\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1"+
		"\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2\63\3\2\2\2\u01a3\u01a5\t\2\2"+
		"\2\u01a4\u01a3\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6\u01a4\3\2\2\2\u01a6\u01a7"+
		"\3\2\2\2\u01a7\65\3\2\2\2\u01a8\u01ab\5\64\33\2\u01a9\u01ab\7)\2\2\u01aa"+
		"\u01a8\3\2\2\2\u01aa\u01a9\3\2\2\2\u01ab\u01ac\3\2\2\2\u01ac\u01aa\3\2"+
		"\2\2\u01ac\u01ad\3\2\2\2\u01ad\67\3\2\2\2\24<@F\u008f\u00a2\u00af\u00bc"+
		"\u00f5\u00fe\u0103\u0109\u0116\u0122\u019c\u01a1\u01a6\u01aa\u01ac";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}