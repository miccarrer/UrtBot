grammar Commands;

@header {from plugins.commands.models import *}

//////////////////////////////////////////////////
// PARSER

command 
  returns[value]:
  (
    rconCmd = rconCommand {$value = $rconCmd.value}
    | helpAllCmd = helpAllCommand {$value = $helpAllCmd.value}
    | helpOneCmd = helpOneCommand {$value = $helpOneCmd.value}
    | killMeCmd = killMeCommand {$value = $killMeCmd.value}
    | killPlayerCmd = killPlayerCommand {$value = $killPlayerCmd.value}
  );

// help

helpAllCommand returns[value]:
  HELP 
  {$value = HelpAllCommand()};

helpOneCommand returns[value]:
  HELP WHITESPACE cmd=manyButNewLine {$value = HelpAllCommand()}
  {$value = HelpOneCommand()}
  {$value.target = $cmd.text}
  ;

// rcon

rconCommand returns[value]:
  RCON WHITESPACE request=manyButNewLine 
  {$value = RconCommand()}
  {$value.request = $request.text}
  ;

// kill

killMeCommand returns[value]:
  KILL
  {$value = KillMeCommand()};

killPlayerCommand returns[value]:
  KILL WHITESPACE client=clientValue
  {$value = KillPlayerCommand()}
  {$value.target = $client.text}
;

// parameters

clientValue: intValue| manyButWhitespace;

intValue: DIGIT+;

// misc

manyButWhitespace: ~(WHITESPACE)+;
manyButDoubleQuote: ~(DOUBLE_QUOTE)+;
manyButNewLine: ~(NEWLINE)+;

//////////////////////////////////////////////////
// LEXER

RCON: 'rcon' | 'r';
HELP: 'help' | 'h';
KILL: 'kill' | 'k';

DIGIT: '0' ..'9';

DOUBLE_QUOTE: '"';
WHITESPACE: ' ' | '\t';
NEWLINE: '\r'? '\n' | '\r';

ANY_CHAR: .;