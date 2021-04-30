
from enum import Enum, unique
from rcon.helper import RconHelper
from events.models import ChatEvent
from typing import Any
from utils.yaml import load_yaml
from plugins.commands.formatter import Formatter
from bot import Bot

commands_help = load_yaml('config/commands.yaml')

class ChatCommandPrefix(Enum):
    PUBLIC = "@"
    PRIVATE = "!"

class ChatCommand:
    bot: Bot
    event: ChatEvent
    prefix: ChatCommandPrefix

    def inform(self, msg: str):
        if(self.prefix == ChatCommandPrefix.PRIVATE):
            self.bot.rcon_service.tell(self.event.slot, msg)
        else:
            self.bot.rcon_service.say(msg)

    def execute(self):
        pass

################### commands

# help

class HelpAllCommand(ChatCommand):

    def execute(self):
        cmds = []
        for cmd_name in commands_help:
            if(cmd_name not in cmds):
                cmds.append(cmd_name)
        cmds.sort()
        self.inform(self.ctx.fmt.command_list(cmds))


class HelpOneCommand(ChatCommand):
    cmd: str = ""

    def execute(self):
        if(self.cmd in commands_help):
            cmds = commands_help[self.cmd]
            self.inform(self.ctx.fmt.command_help(cmds))
        else:
            self.ctx.rcon.tell(self.ctx.event.slot, self.ctx.fmt.command_not_found(self.cmd))

# kill

class KillMeCommand(ChatCommand):
    def execute(self):
        self.ctx.rcon.smite(self.ctx.event.slot)


class KillPlayerCommand(ChatCommand):
    target: Any = None

    def execute(self):
        self.ctx.rcon.smite(self.target)
