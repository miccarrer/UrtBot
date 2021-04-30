from rcon.helper import RconHelper
from typing import Any
from events.models import GameEvent


class Plugin:
    def on_game_event(self, event: GameEvent):
        pass
