// Generated from d:\Dev\Repos\u005Curbanterror-bot\events_parser\Events.g4 by ANTLR 4.8
from events import *
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class EventsLexer extends Lexer {
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
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"SEPARATOR", "INITGAME", "INITROUND", "INITAUTH", "SHUTDOWNGAME", "WARMUP", 
			"SESSION_DATA_INITIALISED", "CLIENTCONNECT", "CLIENTDISCONNECT", "CLIENTBEGIN", 
			"CLIENTSPAWN", "CLIENTUSERINFO", "CLIENTUSERINFOCHANGED", "ACCOUNTVALIDATED", 
			"SAY", "SAYTELL", "SAYTEAM", "TELL", "KILL", "ITEM", "FLAG", "FLAGCAPTURETIME", 
			"BACK_SLASH", "SLASH", "COMMA", "INFERIOR", "SUPERIOR", "COLON", "SEMICOLON", 
			"DOT", "UNDERSCORE", "MINUS", "PLUS", "DOUBLE_QUOTE", "ROUND_BRACKET_LEFT", 
			"ROUND_BRACKET_RIGHT", "SQUARE_BRACKET_LEFT", "SQUARE_BRACKET_RIGHT", 
			"WHITESPACE", "NEWLINE", "LETTER", "DIGIT"
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


	public EventsLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Events.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2,\u01db\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\3"+
		"\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2"+
		"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3"+
		"\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2"+
		"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5"+
		"\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3"+
		"\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b"+
		"\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3"+
		"\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b"+
		"\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3"+
		"\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3"+
		"\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f"+
		"\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3"+
		"\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16"+
		"\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16"+
		"\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17"+
		"\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21"+
		"\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22"+
		"\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25"+
		"\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27"+
		"\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27"+
		"\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36"+
		"\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\6(\u01cb"+
		"\n(\r(\16(\u01cc\3)\5)\u01d0\n)\3)\3)\6)\u01d4\n)\r)\16)\u01d5\3*\3*\3"+
		"+\3+\2\2,\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33"+
		"\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67"+
		"\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,\3\2\4\4\2\13\13\"\"\4\2C\\c|\2"+
		"\u01de\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2"+
		"\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3"+
		"\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2"+
		"\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2"+
		"/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2"+
		"\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2"+
		"G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3"+
		"\2\2\2\2U\3\2\2\2\3W\3\2\2\2\5\u0094\3\2\2\2\7\u009e\3\2\2\2\t\u00a9\3"+
		"\2\2\2\13\u00b3\3\2\2\2\r\u00c1\3\2\2\2\17\u00c9\3\2\2\2\21\u00f5\3\2"+
		"\2\2\23\u0104\3\2\2\2\25\u0116\3\2\2\2\27\u0123\3\2\2\2\31\u0130\3\2\2"+
		"\2\33\u0140\3\2\2\2\35\u0157\3\2\2\2\37\u0169\3\2\2\2!\u016e\3\2\2\2#"+
		"\u0177\3\2\2\2%\u0180\3\2\2\2\'\u0186\3\2\2\2)\u018c\3\2\2\2+\u0192\3"+
		"\2\2\2-\u0198\3\2\2\2/\u01a9\3\2\2\2\61\u01ab\3\2\2\2\63\u01ad\3\2\2\2"+
		"\65\u01af\3\2\2\2\67\u01b1\3\2\2\29\u01b3\3\2\2\2;\u01b5\3\2\2\2=\u01b7"+
		"\3\2\2\2?\u01b9\3\2\2\2A\u01bb\3\2\2\2C\u01bd\3\2\2\2E\u01bf\3\2\2\2G"+
		"\u01c1\3\2\2\2I\u01c3\3\2\2\2K\u01c5\3\2\2\2M\u01c7\3\2\2\2O\u01ca\3\2"+
		"\2\2Q\u01d3\3\2\2\2S\u01d7\3\2\2\2U\u01d9\3\2\2\2WX\7/\2\2XY\7/\2\2YZ"+
		"\7/\2\2Z[\7/\2\2[\\\7/\2\2\\]\7/\2\2]^\7/\2\2^_\7/\2\2_`\7/\2\2`a\7/\2"+
		"\2ab\7/\2\2bc\7/\2\2cd\7/\2\2de\7/\2\2ef\7/\2\2fg\7/\2\2gh\7/\2\2hi\7"+
		"/\2\2ij\7/\2\2jk\7/\2\2kl\7/\2\2lm\7/\2\2mn\7/\2\2no\7/\2\2op\7/\2\2p"+
		"q\7/\2\2qr\7/\2\2rs\7/\2\2st\7/\2\2tu\7/\2\2uv\7/\2\2vw\7/\2\2wx\7/\2"+
		"\2xy\7/\2\2yz\7/\2\2z{\7/\2\2{|\7/\2\2|}\7/\2\2}~\7/\2\2~\177\7/\2\2\177"+
		"\u0080\7/\2\2\u0080\u0081\7/\2\2\u0081\u0082\7/\2\2\u0082\u0083\7/\2\2"+
		"\u0083\u0084\7/\2\2\u0084\u0085\7/\2\2\u0085\u0086\7/\2\2\u0086\u0087"+
		"\7/\2\2\u0087\u0088\7/\2\2\u0088\u0089\7/\2\2\u0089\u008a\7/\2\2\u008a"+
		"\u008b\7/\2\2\u008b\u008c\7/\2\2\u008c\u008d\7/\2\2\u008d\u008e\7/\2\2"+
		"\u008e\u008f\7/\2\2\u008f\u0090\7/\2\2\u0090\u0091\7/\2\2\u0091\u0092"+
		"\7/\2\2\u0092\u0093\7/\2\2\u0093\4\3\2\2\2\u0094\u0095\7K\2\2\u0095\u0096"+
		"\7p\2\2\u0096\u0097\7k\2\2\u0097\u0098\7v\2\2\u0098\u0099\7I\2\2\u0099"+
		"\u009a\7c\2\2\u009a\u009b\7o\2\2\u009b\u009c\7g\2\2\u009c\u009d\7<\2\2"+
		"\u009d\6\3\2\2\2\u009e\u009f\7K\2\2\u009f\u00a0\7p\2\2\u00a0\u00a1\7k"+
		"\2\2\u00a1\u00a2\7v\2\2\u00a2\u00a3\7T\2\2\u00a3\u00a4\7q\2\2\u00a4\u00a5"+
		"\7w\2\2\u00a5\u00a6\7p\2\2\u00a6\u00a7\7f\2\2\u00a7\u00a8\7<\2\2\u00a8"+
		"\b\3\2\2\2\u00a9\u00aa\7K\2\2\u00aa\u00ab\7p\2\2\u00ab\u00ac\7k\2\2\u00ac"+
		"\u00ad\7v\2\2\u00ad\u00ae\7C\2\2\u00ae\u00af\7w\2\2\u00af\u00b0\7v\2\2"+
		"\u00b0\u00b1\7j\2\2\u00b1\u00b2\7<\2\2\u00b2\n\3\2\2\2\u00b3\u00b4\7U"+
		"\2\2\u00b4\u00b5\7j\2\2\u00b5\u00b6\7w\2\2\u00b6\u00b7\7v\2\2\u00b7\u00b8"+
		"\7f\2\2\u00b8\u00b9\7q\2\2\u00b9\u00ba\7y\2\2\u00ba\u00bb\7p\2\2\u00bb"+
		"\u00bc\7I\2\2\u00bc\u00bd\7c\2\2\u00bd\u00be\7o\2\2\u00be\u00bf\7g\2\2"+
		"\u00bf\u00c0\7<\2\2\u00c0\f\3\2\2\2\u00c1\u00c2\7Y\2\2\u00c2\u00c3\7c"+
		"\2\2\u00c3\u00c4\7t\2\2\u00c4\u00c5\7o\2\2\u00c5\u00c6\7w\2\2\u00c6\u00c7"+
		"\7r\2\2\u00c7\u00c8\7<\2\2\u00c8\16\3\2\2\2\u00c9\u00ca\7U\2\2\u00ca\u00cb"+
		"\7g\2\2\u00cb\u00cc\7u\2\2\u00cc\u00cd\7u\2\2\u00cd\u00ce\7k\2\2\u00ce"+
		"\u00cf\7q\2\2\u00cf\u00d0\7p\2\2\u00d0\u00d1\7\"\2\2\u00d1\u00d2\7f\2"+
		"\2\u00d2\u00d3\7c\2\2\u00d3\u00d4\7v\2\2\u00d4\u00d5\7c\2\2\u00d5\u00d6"+
		"\7\"\2\2\u00d6\u00d7\7k\2\2\u00d7\u00d8\7p\2\2\u00d8\u00d9\7k\2\2\u00d9"+
		"\u00da\7v\2\2\u00da\u00db\7k\2\2\u00db\u00dc\7c\2\2\u00dc\u00dd\7n\2\2"+
		"\u00dd\u00de\7k\2\2\u00de\u00df\7u\2\2\u00df\u00e0\7g\2\2\u00e0\u00e1"+
		"\7f\2\2\u00e1\u00e2\7\"\2\2\u00e2\u00e3\7h\2\2\u00e3\u00e4\7q\2\2\u00e4"+
		"\u00e5\7t\2\2\u00e5\u00e6\7\"\2\2\u00e6\u00e7\7e\2\2\u00e7\u00e8\7n\2"+
		"\2\u00e8\u00e9\7k\2\2\u00e9\u00ea\7g\2\2\u00ea\u00eb\7p\2\2\u00eb\u00ec"+
		"\7v\2\2\u00ec\u00ed\7\"\2\2\u00ed\u00ee\7q\2\2\u00ee\u00ef\7p\2\2\u00ef"+
		"\u00f0\7\"\2\2\u00f0\u00f1\7u\2\2\u00f1\u00f2\7n\2\2\u00f2\u00f3\7q\2"+
		"\2\u00f3\u00f4\7v\2\2\u00f4\20\3\2\2\2\u00f5\u00f6\7E\2\2\u00f6\u00f7"+
		"\7n\2\2\u00f7\u00f8\7k\2\2\u00f8\u00f9\7g\2\2\u00f9\u00fa\7p\2\2\u00fa"+
		"\u00fb\7v\2\2\u00fb\u00fc\7E\2\2\u00fc\u00fd\7q\2\2\u00fd\u00fe\7p\2\2"+
		"\u00fe\u00ff\7p\2\2\u00ff\u0100\7g\2\2\u0100\u0101\7e\2\2\u0101\u0102"+
		"\7v\2\2\u0102\u0103\7<\2\2\u0103\22\3\2\2\2\u0104\u0105\7E\2\2\u0105\u0106"+
		"\7n\2\2\u0106\u0107\7k\2\2\u0107\u0108\7g\2\2\u0108\u0109\7p\2\2\u0109"+
		"\u010a\7v\2\2\u010a\u010b\7F\2\2\u010b\u010c\7k\2\2\u010c\u010d\7u\2\2"+
		"\u010d\u010e\7e\2\2\u010e\u010f\7q\2\2\u010f\u0110\7p\2\2\u0110\u0111"+
		"\7p\2\2\u0111\u0112\7g\2\2\u0112\u0113\7e\2\2\u0113\u0114\7v\2\2\u0114"+
		"\u0115\7<\2\2\u0115\24\3\2\2\2\u0116\u0117\7E\2\2\u0117\u0118\7n\2\2\u0118"+
		"\u0119\7k\2\2\u0119\u011a\7g\2\2\u011a\u011b\7p\2\2\u011b\u011c\7v\2\2"+
		"\u011c\u011d\7D\2\2\u011d\u011e\7g\2\2\u011e\u011f\7i\2\2\u011f\u0120"+
		"\7k\2\2\u0120\u0121\7p\2\2\u0121\u0122\7<\2\2\u0122\26\3\2\2\2\u0123\u0124"+
		"\7E\2\2\u0124\u0125\7n\2\2\u0125\u0126\7k\2\2\u0126\u0127\7g\2\2\u0127"+
		"\u0128\7p\2\2\u0128\u0129\7v\2\2\u0129\u012a\7U\2\2\u012a\u012b\7r\2\2"+
		"\u012b\u012c\7c\2\2\u012c\u012d\7y\2\2\u012d\u012e\7p\2\2\u012e\u012f"+
		"\7<\2\2\u012f\30\3\2\2\2\u0130\u0131\7E\2\2\u0131\u0132\7n\2\2\u0132\u0133"+
		"\7k\2\2\u0133\u0134\7g\2\2\u0134\u0135\7p\2\2\u0135\u0136\7v\2\2\u0136"+
		"\u0137\7W\2\2\u0137\u0138\7u\2\2\u0138\u0139\7g\2\2\u0139\u013a\7t\2\2"+
		"\u013a\u013b\7k\2\2\u013b\u013c\7p\2\2\u013c\u013d\7h\2\2\u013d\u013e"+
		"\7q\2\2\u013e\u013f\7<\2\2\u013f\32\3\2\2\2\u0140\u0141\7E\2\2\u0141\u0142"+
		"\7n\2\2\u0142\u0143\7k\2\2\u0143\u0144\7g\2\2\u0144\u0145\7p\2\2\u0145"+
		"\u0146\7v\2\2\u0146\u0147\7W\2\2\u0147\u0148\7u\2\2\u0148\u0149\7g\2\2"+
		"\u0149\u014a\7t\2\2\u014a\u014b\7k\2\2\u014b\u014c\7p\2\2\u014c\u014d"+
		"\7h\2\2\u014d\u014e\7q\2\2\u014e\u014f\7E\2\2\u014f\u0150\7j\2\2\u0150"+
		"\u0151\7c\2\2\u0151\u0152\7p\2\2\u0152\u0153\7i\2\2\u0153\u0154\7g\2\2"+
		"\u0154\u0155\7f\2\2\u0155\u0156\7<\2\2\u0156\34\3\2\2\2\u0157\u0158\7"+
		"C\2\2\u0158\u0159\7e\2\2\u0159\u015a\7e\2\2\u015a\u015b\7q\2\2\u015b\u015c"+
		"\7w\2\2\u015c\u015d\7p\2\2\u015d\u015e\7v\2\2\u015e\u015f\7X\2\2\u015f"+
		"\u0160\7c\2\2\u0160\u0161\7n\2\2\u0161\u0162\7k\2\2\u0162\u0163\7f\2\2"+
		"\u0163\u0164\7c\2\2\u0164\u0165\7v\2\2\u0165\u0166\7g\2\2\u0166\u0167"+
		"\7f\2\2\u0167\u0168\7<\2\2\u0168\36\3\2\2\2\u0169\u016a\7u\2\2\u016a\u016b"+
		"\7c\2\2\u016b\u016c\7{\2\2\u016c\u016d\7<\2\2\u016d \3\2\2\2\u016e\u016f"+
		"\7u\2\2\u016f\u0170\7c\2\2\u0170\u0171\7{\2\2\u0171\u0172\7v\2\2\u0172"+
		"\u0173\7g\2\2\u0173\u0174\7n\2\2\u0174\u0175\7n\2\2\u0175\u0176\7<\2\2"+
		"\u0176\"\3\2\2\2\u0177\u0178\7u\2\2\u0178\u0179\7c\2\2\u0179\u017a\7{"+
		"\2\2\u017a\u017b\7v\2\2\u017b\u017c\7g\2\2\u017c\u017d\7c\2\2\u017d\u017e"+
		"\7o\2\2\u017e\u017f\7<\2\2\u017f$\3\2\2\2\u0180\u0181\7v\2\2\u0181\u0182"+
		"\7g\2\2\u0182\u0183\7n\2\2\u0183\u0184\7n\2\2\u0184\u0185\7<\2\2\u0185"+
		"&\3\2\2\2\u0186\u0187\7M\2\2\u0187\u0188\7k\2\2\u0188\u0189\7n\2\2\u0189"+
		"\u018a\7n\2\2\u018a\u018b\7<\2\2\u018b(\3\2\2\2\u018c\u018d\7K\2\2\u018d"+
		"\u018e\7v\2\2\u018e\u018f\7g\2\2\u018f\u0190\7o\2\2\u0190\u0191\7<\2\2"+
		"\u0191*\3\2\2\2\u0192\u0193\7H\2\2\u0193\u0194\7n\2\2\u0194\u0195\7c\2"+
		"\2\u0195\u0196\7i\2\2\u0196\u0197\7<\2\2\u0197,\3\2\2\2\u0198\u0199\7"+
		"H\2\2\u0199\u019a\7n\2\2\u019a\u019b\7c\2\2\u019b\u019c\7i\2\2\u019c\u019d"+
		"\7E\2\2\u019d\u019e\7c\2\2\u019e\u019f\7r\2\2\u019f\u01a0\7v\2\2\u01a0"+
		"\u01a1\7w\2\2\u01a1\u01a2\7t\2\2\u01a2\u01a3\7g\2\2\u01a3\u01a4\7V\2\2"+
		"\u01a4\u01a5\7k\2\2\u01a5\u01a6\7o\2\2\u01a6\u01a7\7g\2\2\u01a7\u01a8"+
		"\7<\2\2\u01a8.\3\2\2\2\u01a9\u01aa\7^\2\2\u01aa\60\3\2\2\2\u01ab\u01ac"+
		"\7\61\2\2\u01ac\62\3\2\2\2\u01ad\u01ae\7.\2\2\u01ae\64\3\2\2\2\u01af\u01b0"+
		"\7>\2\2\u01b0\66\3\2\2\2\u01b1\u01b2\7@\2\2\u01b28\3\2\2\2\u01b3\u01b4"+
		"\7<\2\2\u01b4:\3\2\2\2\u01b5\u01b6\7=\2\2\u01b6<\3\2\2\2\u01b7\u01b8\7"+
		"\60\2\2\u01b8>\3\2\2\2\u01b9\u01ba\7a\2\2\u01ba@\3\2\2\2\u01bb\u01bc\7"+
		"/\2\2\u01bcB\3\2\2\2\u01bd\u01be\7-\2\2\u01beD\3\2\2\2\u01bf\u01c0\7$"+
		"\2\2\u01c0F\3\2\2\2\u01c1\u01c2\7*\2\2\u01c2H\3\2\2\2\u01c3\u01c4\7+\2"+
		"\2\u01c4J\3\2\2\2\u01c5\u01c6\7]\2\2\u01c6L\3\2\2\2\u01c7\u01c8\7_\2\2"+
		"\u01c8N\3\2\2\2\u01c9\u01cb\t\2\2\2\u01ca\u01c9\3\2\2\2\u01cb\u01cc\3"+
		"\2\2\2\u01cc\u01ca\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cdP\3\2\2\2\u01ce\u01d0"+
		"\7\17\2\2\u01cf\u01ce\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0\u01d1\3\2\2\2"+
		"\u01d1\u01d4\7\f\2\2\u01d2\u01d4\7\17\2\2\u01d3\u01cf\3\2\2\2\u01d3\u01d2"+
		"\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d5\u01d3\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6"+
		"R\3\2\2\2\u01d7\u01d8\t\3\2\2\u01d8T\3\2\2\2\u01d9\u01da\4\62;\2\u01da"+
		"V\3\2\2\2\7\2\u01cc\u01cf\u01d3\u01d5\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}