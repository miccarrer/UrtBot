from typing import Any
from events.models import GameEvent


class Plugin:
    bot: Any

    def __init__(self, bot):
        self.bot = bot

    def on_game_event(self, event: GameEvent):
        pass
