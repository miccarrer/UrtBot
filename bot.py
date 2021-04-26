import logging

from events.service import EventService
from plugins.service import PluginService
from rcon.service import RconService
from utils.yaml import load_yaml

class Bot:
    event_service: EventService = None
    plugin_service: PluginService = None
    rcon_service: RconService = None

    def __init__(self):
        data = load_yaml('config/base.yaml')
        
        self.event_service = EventService(data["log_file"])
        self.plugin_service = PluginService(self)
        self.rcon_service = RconService(data["ip"], data["port"], data["password"])

    def start(self):
        logging.info('Starting bot..')
        self.event_service.load()
        self.rcon_service.say_success('Bot started')
        self.event_service.listen(self.plugin_service.on_new_event)
