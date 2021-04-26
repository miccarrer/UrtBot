
# base

class GameEvent:
    time: int


class ClientEvent(GameEvent):
    slot: int


class ChatEvent(ClientEvent):
    message: str

# implementations


class SeparatorEvent(GameEvent):
    pass


class InitGameEvent(GameEvent):
    parameters: dict = {}


class InitRoundEvent(GameEvent):
    parameters: dict = {}


class InitAuthEvent(GameEvent):
    parameters: dict = {}


class ShutdownGameEvent(GameEvent):
    pass


class WarmUpEvent(GameEvent):
    pass


class SessionDataInitialisedEvent(ClientEvent):
    unknown: int


class ClientConnectEvent(ClientEvent):
    pass


class ClientDisconnectEvent(ClientEvent):
    pass


class ClientUserinfoEvent(ClientEvent):
    parameters: dict = {}


class ClientUserinfoChangedEvent(ClientEvent):
    parameters: dict = {}


class ClientBeginEvent(ClientEvent):
    pass


class ClientSpawnEvent(ClientEvent):
    pass


class AccountValidatedEvent(ClientEvent):
    account: str
    level: int
    role: str


class SayEvent(ChatEvent):
    sender: str


class SayTellEvent(ChatEvent):
    sender: str
    sender_slot: int


class SayTeamEvent(ChatEvent):
    sender: str


class RadioEvent(ChatEvent):
    menu1: int
    menu2: int
    location: str


class TellEvent(GameEvent):
    sender: str
    target: str
    message: str


class KillEvent(GameEvent):
    x: int
    y: int
    z: int
    killer: str
    killed: str
    how: str


class ItemEvent(ClientEvent):
    item: str


class FlagEvent(ClientEvent):
    num: int
    item: str


class FlagCaptureTimeEvent(ClientEvent):
    time: int


class FlagReturnEvent(GameEvent):
    flag: str
