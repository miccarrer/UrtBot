from plugins.commands.utils.antlr import parse_command
from plugins.commands.models import ChatCommand
from events.models import ChatEvent, GameEvent
from plugins.models import Plugin
from plugins.commands.models import ChatCommandPrefix


class CommandsPlugin(Plugin):

    def on_game_event(self, event: GameEvent):
        if(isinstance(event, ChatEvent)):
            chat_event: ChatEvent = event

            for prefix in ChatCommandPrefix:
                if(chat_event.message.startswith(prefix.value)):
                    command_without_prefix = chat_event.message[len(prefix.value):]

                    command_space_index = -1 if command_without_prefix.count(' ') == 0 else command_without_prefix.index(' ')
                    command_name = command_without_prefix if command_space_index < 0 else command_without_prefix[:command_space_index]

                    def on_syntax_error(recognizer, offendingSymbol, line, column, msg, e):
                        if(column == 0):
                          self.rcon.tell(chat_event.slot, f'Unknown command \'{command_name}\'. Use \'!help\' to get the list')
                        else:
                          self.rcon.tell(chat_event.slot, f'Bad usage. Use \'!help {command_name}\' ')

                    command: ChatCommand = parse_command(command_without_prefix, on_syntax_error)

                    if(command):
                        command.prefix = prefix
                        command.execute(chat_event, self.rcon)

                    break
