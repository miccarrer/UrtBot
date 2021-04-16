
# base

class GameEvent:
  minutes=0
  seconds=0

class ClientEvent(GameEvent):
  slot=0

# implementations

class SeparatorEvent(GameEvent):
  pass

class InitGameEvent(GameEvent):
  parameters={}

class InitRoundEvent(GameEvent):
  parameters={}

class InitAuthEvent(GameEvent):
  parameters={}

class ShutdownGameEvent(GameEvent):
  pass

class WarmUpEvent(GameEvent):
  pass

class SessionDataInitialisedEvent(ClientEvent):
  unknown=0

class ClientConnectEvent(ClientEvent):
  pass

class ClientDisconnectEvent(ClientEvent):
  pass

class ClientUserinfoEvent(ClientEvent):
  parameters={}

class ClientUserinfoChangedEvent(ClientEvent):
  parameters={}
  
class ClientBeginEvent(ClientEvent):
  pass
  
class ClientSpawnEvent(ClientEvent):
  pass

class AccountValidatedEvent(ClientEvent):
  account=''
  level=0
  role=''

class SayEvent(ClientEvent):
  sender=''
  message=''

class SayTellEvent(ClientEvent):
  sender=''
  sender_slot=''
  message=''

class SayTeamEvent(ClientEvent):
  sender=''
  message=''

class TellEvent(GameEvent):
  sender=''
  target=''
  message=''

class KillEvent(GameEvent):
  x=0
  y=0
  z=0
  killer=''
  killed=''
  how=''

class ItemEvent(ClientEvent):
  item=''
  
class FlagEvent(ClientEvent):
  num=0
  item=''
  
class FlagCaptureTimeEvent(ClientEvent):
  time=0