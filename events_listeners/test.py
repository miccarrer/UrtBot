from events_listener import GameEventListener
from events import *
from rcon import send


class TestListener(GameEventListener):

    def on_say(self, event: SayEvent):
        send(event.message)
