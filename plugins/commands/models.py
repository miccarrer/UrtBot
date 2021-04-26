
from enum import Enum, unique
from plugins.commands.utils.config import get_cmd_list
from utils.colors import Colors
from events.models import ChatEvent
from typing import Any

class ChatCommandPrefix(Enum):
    PUBLIC = "@"
    PRIVATE = "!"


class ChatCommand:
    prefix = ChatCommandPrefix

    def execute(self, event: ChatEvent, bot):
        pass

################### commands

# help

class HelpAllCommand(ChatCommand):

    def execute(self, event: ChatEvent, bot):
      bot.rcon_service.tell_info(event.slot, 'Available commands are: ' + Colors.LIGHT_YELLOW.value + get_cmd_list())


class HelpOneCommand(ChatCommand):
    cmd: str = ""

    def execute(self, event: ChatEvent, bot):
        bot.rcon_service.tell_error(event.slot, 'Help all command not available yet')

# rcon

class RconCommand(ChatCommand):
    request: str

    def execute(self, event: ChatEvent, bot):
        response_lines = bot.rcon_service.rcon(self.request)
        for line in response_lines:
            bot.rcon_service.tell_info(event.slot, line)

# kill

class KillMeCommand(ChatCommand):
    def execute(self, event: ChatEvent, bot):
        bot.rcon_service.smite(event.slot)


class KillPlayerCommand(ChatCommand):
    target: Any = None

    def execute(self, event: ChatEvent, bot):
        bot.rcon_service.smite(self.target)
