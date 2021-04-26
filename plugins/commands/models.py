
from enum import Enum, unique
from rcon.helper import RconHelper
from plugins.commands.utils.config import get_cmd, get_cmd_list
from utils.colors import Colors
from events.models import ChatEvent
from typing import Any

class ChatCommandPrefix(Enum):
    PUBLIC = "@"
    PRIVATE = "!"


class ChatCommand:
    prefix = ChatCommandPrefix

    def execute(self, event: ChatEvent, rcon: RconHelper):
        pass

################### commands

# help

class HelpAllCommand(ChatCommand):

    def execute(self, event: ChatEvent, rcon: RconHelper):
      rcon.tell(event.slot, 'Available commands are: ' + Colors.LIGHT_YELLOW.value + get_cmd_list())


class HelpOneCommand(ChatCommand):
    cmd: str = ""

    def execute(self, event: ChatEvent, rcon: RconHelper):
        rcon.tell(event.slot, get_cmd(self.cmd))

# rcon

class RconCommand(ChatCommand):
    request: str

    def execute(self, event: ChatEvent, rcon: RconHelper):
        rcon.send(self.request)

# kill

class KillMeCommand(ChatCommand):
    def execute(self, event: ChatEvent, rcon: RconHelper):
        rcon.smite(event.slot)


class KillPlayerCommand(ChatCommand):
    target: Any = None

    def execute(self, event: ChatEvent, rcon: RconHelper):
        rcon.smite(self.target)
