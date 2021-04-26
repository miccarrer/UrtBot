
from typing import List
from events.models import GameEvent
from plugins.commands.plugin import CommandsPlugin
from plugins.models import Plugin


class PluginService:
    plugins: List[Plugin] = []

    def __init__(self, bot):
      self.plugins.append(CommandsPlugin(bot))

    def on_new_event(self, event: GameEvent):
      for plugin in self.plugins:
          plugin.on_game_event(event)
    