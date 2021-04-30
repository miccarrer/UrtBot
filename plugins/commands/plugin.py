from events.models import ChatEvent, GameEvent
from plugins.commands.models import ChatCommand, ChatCommandPrefix
from plugins.commands.utils.antlr import parse_command
from plugins.models import Plugin


class CommandsPlugin(Plugin):

    def on_game_event(self, event: GameEvent):
        if(isinstance(event, ChatEvent)):
            self.on_chat_event(event)

    def on_chat_event(self, event: ChatEvent):
        for prefix in ChatCommandPrefix:
            if(event.message.startswith(prefix.value)):
                cmd_raw = event.message[len(prefix.value):]
                cmd_space_index = -1 if cmd_raw.count(' ') == 0 else cmd_raw.index(' ')
                cmd_name = cmd_raw if cmd_space_index < 0 else cmd_raw[:cmd_space_index]

                def on_syntax_error(recognizer, offendingSymbol, line, column, msg, e):
                    if(column == 0):
                        self.rcon.tell(event.slot, self.fmt.unknown_cmd(cmd_name))
                    else:
                        self.rcon.tell(event.slot, self.fmt.bad_usage())

                cmd: ChatCommand = parse_command(cmd_raw, on_syntax_error)

                if(cmd):
                    cmd.execute()

                break