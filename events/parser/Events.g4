grammar Events;

@header {from events.models import *}

//////////////////////////////////////////////////
// PARSER

events
	returns[value]:
	{$value = []}
	(a = event NEWLINE? {$value.append($a.value)})*;

event
	returns[value]:
	WHITESPACE*
  time = eventTime
  WHITESPACE
  (
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
		| radioEvt = radioEvent {$value = $radioEvt.value}
		| killEvt = killEvent {$value = $killEvt.value}
		| itemEvt = itemEvent {$value = $itemEvt.value}
		| flagEvt = flagEvent {$value = $flagEvt.value}
		| flagCaptureTimeEvt = flagCaptureTimeEvent {$value = $flagCaptureTimeEvt.value}
		| flagReturnEvt = flagReturnEvent {$value = $flagReturnEvt.value}
	)
  {$value.time = $time.value};

eventTime returns[value]:
  a = intValue COLON b = intValue
  {$value = int($a.text) * 60 + int($b.text)}
  ;

// events

separatorEvent
	returns[value]: SEPARATOR {$value = SeparatorEvent()};

initGameEvent
	returns[value]:
	INITGAME COLON WHITESPACE {$value = InitGameEvent()} (
		BACK_SLASH a = manyButBackSlash BACK_SLASH b = manyButBackSlashOrNewLine
		{$value.parameters[$a.text]=$b.text}
	)+;

initRoundEvent
	returns[value]:
	INITROUND COLON WHITESPACE {$value = InitRoundEvent()} (
		BACK_SLASH a = manyButBackSlash BACK_SLASH b = manyButBackSlashOrNewLine
		{$value.parameters[$a.text]=$b.text}
	)+;

initAuthEvent
	returns[value]:
	INITAUTH COLON WHITESPACE {$value = InitAuthEvent()} (
		BACK_SLASH a = manyButBackSlash BACK_SLASH b = manyButBackSlashOrNewLine?
		{$value.parameters[$a.text]=$b.text}
	)+;

shutdownGameEvent
	returns[value]: SHUTDOWNGAME COLON {$value = ShutdownGameEvent()};

warmupEvent
	returns[value]: WARMUP COLON {$value = WarmUpEvent()};

sessionDataInitEvent
	returns[value]:
	SESSION_DATA_INITIALISED WHITESPACE a = intValue WHITESPACE AT WHITESPACE b = intValue
	{$value = SessionDataInitialisedEvent()}
	{$value.slot=int($a.text)}
	{$value.unknown=int($b.text)};

clientConnectEvent
	returns[value]:
	CLIENTCONNECT COLON WHITESPACE a = intValue
	{$value=ClientConnectEvent()}
	{$value.slot=int($a.text)};

clientDisconnectEvent
	returns[value]:
	CLIENTDISCONNECT COLON WHITESPACE a = intValue
	{$value=ClientDisconnectEvent()}
	{$value.slot=int($a.text)};

clientBeginEvent
	returns[value]:
	CLIENTBEGIN COLON WHITESPACE a = intValue
	{$value=ClientBeginEvent()}
	{$value.slot=int($a.text)};

clientSpawnEvent
	returns[value]:
	CLIENTSPAWN COLON WHITESPACE a = intValue
	{$value=ClientSpawnEvent()}
	{$value.slot=int($a.text)};

clientUserinfoEvent
	returns[value]:
	CLIENTUSERINFO COLON WHITESPACE a = intValue WHITESPACE
	{$value=ClientUserinfoEvent()}
	{$value.slot=int($a.text)}
	(
		BACK_SLASH b = manyButBackSlash BACK_SLASH c = manyButBackSlashOrNewLine
		{$value.parameters[$b.text]=$c.text}
	)+;

clientUserinfoChangedEvent
	returns[value]:
	CLIENTUSERINFOCHANGED COLON WHITESPACE a = intValue WHITESPACE
	{$value=ClientUserinfoChangedEvent()}
	{$value.slot=int($a.text)}
	(
		b = manyButBackSlash BACK_SLASH c = manyButBackSlashOrNewLine?
		{$value.parameters[$b.text]=$c.text}
	)
  (
    BACK_SLASH b2 = manyButBackSlash BACK_SLASH c2 = manyButBackSlashOrNewLine?
		{$value.parameters[$b2.text]=$c2.text}
  )*;

accountValidatedEvent
	returns[value]:
	ACCOUNTVALIDATED COLON WHITESPACE a = intValue WHITESPACE
	MINUS WHITESPACE b = manyButWhitespace? WHITESPACE 
	MINUS WHITESPACE c = intValue WHITESPACE
	MINUS WHITESPACE DOUBLE_QUOTE d = manyButDoubleQuote? DOUBLE_QUOTE
	{$value=AccountValidatedEvent()}
	{$value.slot=int($a.text)}
  {$value.account=$b.text}
	{$value.level=int($c.text)}
  {$value.role=$d.text};

sayEvent
	returns[value]:
	SAY COLON WHITESPACE a = intValue WHITESPACE b = manyButWhitespace WHITESPACE c = manyButNewLine
	{$value=SayEvent()}
	{$value.slot=int($a.text)}
	{$value.sender=$b.text[:-1]}
	{$value.message=$c.text};

sayTellEvent
	returns[value]:
	SAYTELL COLON WHITESPACE a = intValue WHITESPACE b = intValue WHITESPACE c = manyButWhitespace WHITESPACE d = manyButNewLine
	{$value=SayTellEvent()}
	{$value.slot=int($a.text)}
	{$value.sender_slot=int($b.text)}
	{$value.sender=$c.text[:-1]}
	{$value.message=$d.text};

sayTeamEvent
	returns[value]:
	SAYTEAM COLON WHITESPACE a = intValue WHITESPACE b = manyButWhitespace WHITESPACE c = manyButNewLine
	{$value=SayTeamEvent()}
	{$value.slot=int($a.text)}
	{$value.sender=$b.text[:-1]}
	{$value.message=$c.text};

tellEvent
	returns[value]:
	TELL COLON WHITESPACE a = manyButWhitespace WHITESPACE TO WHITESPACE b = manyButWhitespace WHITESPACE c = manyButNewLine
	{$value=TellEvent()}
	{$value.sender=$a.text}
	{$value.target=$b.text[:-1]}
	{$value.message=$c.text};
  

radioEvent
	returns[value]:
	RADIO COLON WHITESPACE a = intValue WHITESPACE
	MINUS WHITESPACE b = intValue WHITESPACE 
	MINUS WHITESPACE c = intValue WHITESPACE
	MINUS WHITESPACE DOUBLE_QUOTE d = manyButDoubleQuote? DOUBLE_QUOTE WHITESPACE
	MINUS WHITESPACE DOUBLE_QUOTE e = manyButDoubleQuote? DOUBLE_QUOTE
	{$value=RadioEvent()}
	{$value.slot=int($a.text)}
  {$value.menu1=int($b.text)}
  {$value.menu2=int($c.text)}
	{$value.location=$d.text}
  {$value.message=$e.text};

killEvent
	returns[value]:
	KILL COLON WHITESPACE a = intValue WHITESPACE b = intValue WHITESPACE c = intValue COLON WHITESPACE d = manyButWhitespace WHITESPACE manyButWhitespace WHITESPACE e = manyButWhitespace WHITESPACE BY WHITESPACE f = manyButNewLine
	{$value=KillEvent()}
	{$value.x=int($a.text)}
	{$value.y=int($b.text)}
	{$value.z=int($c.text)}
	{$value.killer=$d.text}
	{$value.killed=$e.text}
	{$value.how=$f.text};

itemEvent
	returns[value]:
	ITEM COLON WHITESPACE a = intValue WHITESPACE b = manyButNewLine
	{$value=ItemEvent()}
	{$value.slot=int($a.text)}
	{$value.item=$b.text};

flagEvent
	returns[value]:
	FLAG COLON WHITESPACE a = intValue WHITESPACE b = intValue COLON WHITESPACE c = manyButNewLine
	{$value=FlagEvent()}
	{$value.slot=int($a.text)}
	{$value.num=int($b.text)}
	{$value.item=$c.text};

flagCaptureTimeEvent
	returns[value]:
	FLAGCAPTURETIME COLON WHITESPACE a = intValue COLON WHITESPACE b = intValue
	{$value=FlagCaptureTimeEvent()}
	{$value.slot=int($a.text)}
	{$value.time=int($b.text)};

flagReturnEvent
	returns[value]:
	FLAGRETURN COLON WHITESPACE a = manyButNewLine
	{$value=FlagReturnEvent()}
	{$value.flag=$a.text};

// misc

intValue: MINUS? DIGIT+;

manyButNewLine: ~(NEWLINE)+;
manyButWhitespace: ~(WHITESPACE)+;
manyButBackSlash: ~(BACK_SLASH)+;
manyButBackSlashOrNewLine: ~(NEWLINE | BACK_SLASH)+;
manyButDoubleQuote: ~(DOUBLE_QUOTE)+;


//////////////////////////////////////////////////
// LEXER

SEPARATOR: '------------------------------------------------------------';
INITGAME: 'InitGame';
INITROUND: 'InitRound';
INITAUTH: 'InitAuth';
SHUTDOWNGAME: 'ShutdownGame';
WARMUP: 'Warmup';
SESSION_DATA_INITIALISED: 'Session data initialised for client on slot';
AT: 'at';
CLIENTCONNECT: 'ClientConnect';
CLIENTDISCONNECT: 'ClientDisconnect';
CLIENTBEGIN: 'ClientBegin';
CLIENTSPAWN: 'ClientSpawn';
CLIENTUSERINFO: 'ClientUserinfo';
CLIENTUSERINFOCHANGED: 'ClientUserinfoChanged';
ACCOUNTVALIDATED: 'AccountValidated';
SAY: 'say';
SAYTELL: 'saytell';
SAYTEAM: 'sayteam';
RADIO: 'Radio';
TELL: 'tell';
KILL: 'Kill';
ITEM: 'Item';
FLAG: 'Flag';
FLAGCAPTURETIME: 'FlagCaptureTime';
FLAGRETURN: 'Flag Return';
TO: 'to';
BY: 'by';

WHITESPACE: ' ' | '\t';
NEWLINE: '\r'? '\n' | '\r';

BACK_SLASH: '\\';
COLON: ':';
MINUS: '-';
DOUBLE_QUOTE: '"';

DIGIT: '0' ..'9';

ANY_CHAR: .;