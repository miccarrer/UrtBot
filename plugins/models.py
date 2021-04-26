from rcon.helper import RconHelper
from typing import Any
from events.models import GameEvent


class Plugin:
    rcon: RconHelper

    def __init__(self, rcon: RconHelper):
        self.rcon = rcon

    def on_game_event(self, event: GameEvent):
        pass
