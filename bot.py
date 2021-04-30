import logging
from services.events import EventService
from services.plugins import PluginService
from services.rcon import RconService
from utils.yaml import load_yaml

class Bot:
    event_service: EventService = None
    plugin_service: PluginService = None
    rcon_service: RconService = None

    def __init__(self):
        data = load_yaml('config/base.yaml')
        
        self.event_service = EventService(data["log_file"])
        self.rcon_service = RconService(data["ip"], data["port"], data["password"])
        self.plugin_service = PluginService()

    def start(self):
        logging.info('Starting bot..')
        self.event_service.load()
        self.event_service.listen(self.plugin_service.on_new_event)