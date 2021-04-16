grammar Events;

@header {from events import *}

//////////////////////////////////////////////////
// PARSER

events
	returns[value]:
	{$value = []} 
  (
    a = event 
    {$value.append($a.value)} 
    NEWLINE?
  )*;

event
	returns[value]:
	WHITESPACE* a = intValue COLON b = intValue WHITESPACE (
		separatorEvt = separatorEvent {$value = $separatorEvt.value}
		| initGameEvt = initGameEvent {$value = $initGameEvt.value}
		| initRoundEvt = initRoundEvent {$value = $initRoundEvt.value}
		| initAuthEvt = initAuthEvent {$value = $initAuthEvt.value}
		| shutdownGameEvt = shutdownGameEvent {$value = $shutdownGameEvt.value}
		| warmupEvt = warmupEvent {$value = $warmupEvt.value}
		| sessionDataInitEvt = sessionDataInitEvent {$value = $sessionDataInitEvt.value}
		| clientConnectEvt = clientConnectEvent {$value = $clientConnectEvt.value}
		| clientDisconnectEvt = clientDisconnectEvent {$value = $clientDisconnectEvt.value}
		| clientBeginEvt = clientBeginEvent {$value = $clientBeginEvt.value}
		| clientSpawnEvt = clientSpawnEvent {$value = $clientSpawnEvt.value}
		| clientUserinfoEvt = clientUserinfoEvent {$value = $clientUserinfoEvt.value}
		| clientUserinfoChangedEvt = clientUserinfoChangedEvent {$value = $clientUserinfoChangedEvt.value}
		| accountValidatedEvt = accountValidatedEvent {$value = $accountValidatedEvt.value}
		| sayEvt = sayEvent {$value = $sayEvt.value}
		| sayTellEvt = sayTellEvent {$value = $sayTellEvt.value}
		| sayTeamEvt = sayTeamEvent {$value = $sayTeamEvt.value}
		| tellEvt = tellEvent {$value = $tellEvt.value}
		| killEvt = killEvent {$value = $killEvt.value}
		| itemEvt = itemEvent {$value = $itemEvt.value}
		| flagEvt = flagEvent {$value = $flagEvt.value}
		| flagCaptureTimeEvt = flagCaptureTimeEvent {$value = $flagCaptureTimeEvt.value}
	) 
  {$value.minutes = int($a.text)} 
  {$value.seconds = int($b.text)};

// events

separatorEvent
	returns[value]: 
  SEPARATOR 
  {$value = SeparatorEvent()};

initGameEvent
	returns[value]:
	INITGAME WHITESPACE 
  {$value = InitGameEvent()} 
  (
		BACK_SLASH a = wordValue BACK_SLASH b = sentenceValue 
    {$value.parameters[$a.text]=$b.text}
	)+;

initRoundEvent
	returns[value]:
	INITROUND WHITESPACE 
  {$value = InitRoundEvent()} 
  (
		BACK_SLASH a = wordValue BACK_SLASH b = sentenceValue 
    {$value.parameters[$a.text]=$b.text}
	)+;

initAuthEvent
	returns[value]:
	INITAUTH WHITESPACE 
  {$value = InitAuthEvent()} 
  (
		BACK_SLASH a = wordValue BACK_SLASH b = sentenceValue 
    {$value.parameters[$a.text]=$b.text}
	)+;

shutdownGameEvent
	returns[value]: 
  SHUTDOWNGAME 
  {$value = ShutdownGameEvent()};

warmupEvent
	returns[value]: 
  WARMUP 
  {$value = WarmUpEvent()};

sessionDataInitEvent
	returns[value]:
	SESSION_DATA_INITIALISED WHITESPACE a = intValue WHITESPACE wordValue WHITESPACE b = intValue 
  {$value = SessionDataInitialisedEvent()} 
  {$value.slot=int($a.text)} 
  {$value.unknown=int($b.text)};

clientConnectEvent
	returns[value]:
	CLIENTCONNECT WHITESPACE a = intValue 
  {$value=ClientConnectEvent()} 
  {$value.slot=int($a.text)};

clientDisconnectEvent
	returns[value]:
	CLIENTDISCONNECT WHITESPACE a = intValue 
  {$value=ClientDisconnectEvent()} 
  {$value.slot=int($a.text)};

clientBeginEvent
	returns[value]:
	CLIENTBEGIN WHITESPACE a = intValue 
  {$value=ClientBeginEvent()}
  {$value.slot=int($a.text)};

clientSpawnEvent
	returns[value]:
	CLIENTSPAWN WHITESPACE a = intValue 
  {$value=ClientSpawnEvent()}
  {$value.slot=int($a.text)};

clientUserinfoEvent
	returns[value]:
	CLIENTUSERINFO WHITESPACE a = intValue WHITESPACE 
  {$value=ClientUserinfoEvent()}
  {$value.slot=int($a.text)}
  (
		BACK_SLASH b = wordValue BACK_SLASH c = sentenceValue
    {$value.parameters[$b.text]=$c.text}
	)+;

clientUserinfoChangedEvent
	returns[value]:
	CLIENTUSERINFOCHANGED WHITESPACE a = intValue WHITESPACE
  {$value=ClientUserinfoChangedEvent()}
  {$value.slot=int($a.text)}
  (
		BACK_SLASH? b = wordValue BACK_SLASH c = sentenceValue?
    {$value.parameters[$b.text]=$c.text}
	)+;

accountValidatedEvent
  returns [value]:
  {$value=AccountValidatedEvent()}
  ACCOUNTVALIDATED WHITESPACE a=intValue WHITESPACE 
  MINUS WHITESPACE (b=wordValue {$value.account=$b.text} WHITESPACE)?
  MINUS WHITESPACE c=intValue WHITESPACE 
  MINUS WHITESPACE DOUBLE_QUOTE (d=wordValue {$value.role=$d.text})? DOUBLE_QUOTE
  {$value.slot=int($a.text)}
  {$value.level=int($c.text)};

sayEvent
	returns[value]:
	SAY WHITESPACE a = intValue WHITESPACE b = wordValue COLON WHITESPACE c = sentenceValue
  {$value=SayEvent()}
  {$value.slot=int($a.text)}
  {$value.sender=$b.text}
  {$value.message=$c.text};

sayTellEvent
	returns[value]:
	SAYTELL WHITESPACE a = intValue WHITESPACE b = intValue WHITESPACE c = wordValue COLON WHITESPACE d = sentenceValue
  {$value=SayTellEvent()}
  {$value.slot=int($a.text)}
  {$value.sender_slot=int($b.text)}
  {$value.sender=$c.text}
  {$value.message=$d.text};

sayTeamEvent
	returns[value]:
	SAYTELL WHITESPACE a = intValue WHITESPACE b = wordValue COLON WHITESPACE c = sentenceValue
  {$value=SayTeamEvent()}
  {$value.slot=int($a.text)}
  {$value.sender=$b.text}
  {$value.message=$c.text};

tellEvent
	returns[value]:
	TELL WHITESPACE a = wordValue WHITESPACE wordValue WHITESPACE b = wordValue COLON WHITESPACE c = sentenceValue
  {$value=TellEvent()}
  {$value.sender=$a.text}
  {$value.target=$b.text}
  {$value.message=$c.text};

killEvent
	returns[value]:
	KILL WHITESPACE a = intValue WHITESPACE b = intValue WHITESPACE c = intValue COLON WHITESPACE d = wordValue WHITESPACE wordValue WHITESPACE e = wordValue WHITESPACE wordValue WHITESPACE f = wordValue
  {$value=KillEvent()}
  {$value.x=int($a.text)}
  {$value.y=int($b.text)}
  {$value.z=int($c.text)}
  {$value.killer=$d.text}
  {$value.killed=$e.text}
  {$value.how=$f.text};

itemEvent
	returns[value]:
	ITEM WHITESPACE a = intValue WHITESPACE b = wordValue
  {$value=ItemEvent()}
  {$value.slot=int($a.text)}
  {$value.item=$b.text};

flagEvent
	returns[value]:
	FLAG WHITESPACE a = intValue WHITESPACE b = intValue COLON WHITESPACE c = wordValue
  {$value=FlagEvent()}
  {$value.slot=int($a.text)}
  {$value.num=int($b.text)}
  {$value.item=$c.text};

flagCaptureTimeEvent
	returns[value]:
	FLAGCAPTURETIME WHITESPACE a = intValue COLON WHITESPACE b = intValue
  {$value=FlagCaptureTimeEvent()}
  {$value.slot=int($a.text)}
  {$value.time=int($b.text)};

// misc

intValue: MINUS? DIGIT+;

wordValue: (
  LETTER
  | DIGIT
  | UNDERSCORE
  | MINUS
  | PLUS
  | ROUND_BRACKET_LEFT
  | ROUND_BRACKET_RIGHT
  | SQUARE_BRACKET_LEFT
  | SQUARE_BRACKET_RIGHT
  | SLASH
  | COMMA
  | COLON
  | SEMICOLON
  | INFERIOR
  | SUPERIOR
  | DOT)+;

sentenceValue: (wordValue | WHITESPACE)+;

//////////////////////////////////////////////////
// LEXER

SEPARATOR: '------------------------------------------------------------';
INITGAME: 'InitGame:';
INITROUND: 'InitRound:';
INITAUTH: 'InitAuth:';
SHUTDOWNGAME: 'ShutdownGame:';
WARMUP: 'Warmup:';
SESSION_DATA_INITIALISED: 'Session data initialised for client on slot';
CLIENTCONNECT: 'ClientConnect:';
CLIENTDISCONNECT: 'ClientDisconnect:';
CLIENTBEGIN: 'ClientBegin:';
CLIENTSPAWN: 'ClientSpawn:';
CLIENTUSERINFO: 'ClientUserinfo:';
CLIENTUSERINFOCHANGED: 'ClientUserinfoChanged:';
ACCOUNTVALIDATED: 'AccountValidated:';
SAY: 'say:';
SAYTELL: 'saytell:';
SAYTEAM: 'sayteam:';
TELL: 'tell:';
KILL: 'Kill:';
ITEM: 'Item:';
FLAG: 'Flag:';
FLAGCAPTURETIME: 'FlagCaptureTime:';

BACK_SLASH: '\\';
SLASH: '/';
COMMA: ',';
INFERIOR: '<';
SUPERIOR: '>';
COLON: ':';
SEMICOLON: ';';
DOT: '.';
UNDERSCORE: '_';
MINUS: '-';
PLUS: '+';
DOUBLE_QUOTE: '"';
ROUND_BRACKET_LEFT: '(';
ROUND_BRACKET_RIGHT: ')';
SQUARE_BRACKET_LEFT: '[';
SQUARE_BRACKET_RIGHT: ']';

WHITESPACE: (' ' | '\t')+;
NEWLINE: ('\r'? '\n' | '\r')+;

LETTER: ('a' ..'z' | 'A' ..'Z');
DIGIT: '0' ..'9';
