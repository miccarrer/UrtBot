
from rcon.helper import RconHelper
from typing import List
from events.models import GameEvent
from plugins.commands.plugin import CommandsPlugin
from plugins.models import Plugin


class PluginService:
    plugins: List[Plugin] = []

    def __init__(self, rcon: RconHelper):
      self.plugins.append(CommandsPlugin(rcon))

    def on_new_event(self, event: GameEvent):
      for plugin in self.plugins:
          plugin.on_game_event(event)
    