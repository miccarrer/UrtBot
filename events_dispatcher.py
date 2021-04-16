import logging
from events import *
from events_listeners.test import TestListener

listeners=[TestListener()]

def dispatch(event: GameEvent):
  if(isinstance(event, SeparatorEvent)):
    for listener in listeners:
      listener.on_separator(event)

  elif(isinstance(event, InitGameEvent)):
    for listener in listeners:
      listener.on_init_game(event)

  elif(isinstance(event, InitRoundEvent)):
    for listener in listeners:
      listener.on_init_round(event)

  elif(isinstance(event, InitAuthEvent)):
    for listener in listeners:
      listener.on_init_auth(event)

  elif(isinstance(event, ShutdownGameEvent)):
    for listener in listeners:
      listener.on_shutdown_game(event)

  elif(isinstance(event, WarmUpEvent)):
    for listener in listeners:
      listener.on_warmup(event)

  elif(isinstance(event, SessionDataInitialisedEvent)):
    for listener in listeners:
      listener.on_session_data_initialised(event)

  elif(isinstance(event, ClientConnectEvent)):
    for listener in listeners:
      listener.on_client_connect(event)

  elif(isinstance(event, ClientDisconnectEvent)):
    for listener in listeners:
      listener.on_client_disconnect(event)

  elif(isinstance(event, ClientUserinfoEvent)):
    for listener in listeners:
      listener.on_client_userinfo(event)

  elif(isinstance(event, ClientUserinfoChangedEvent)):
    for listener in listeners:
      listener.on_client_userinfo_changed(event)

  elif(isinstance(event, ClientBeginEvent)):
    for listener in listeners:
      listener.on_client_begin(event)

  elif(isinstance(event, ClientSpawnEvent)):
    for listener in listeners:
      listener.on_client_spawn(event)

  elif(isinstance(event, AccountValidatedEvent)):
    for listener in listeners:
      listener.on_account_validated(event)

  elif(isinstance(event, SayEvent)):
    for listener in listeners:
      listener.on_say(event)

  elif(isinstance(event, SayTellEvent)):
    for listener in listeners:
      listener.on_saytell(event)

  elif(isinstance(event, SayTeamEvent)):
    for listener in listeners:
      listener.on_sayteam(event)

  elif(isinstance(event, TellEvent)):
    for listener in listeners:
      listener.on_tell(event)

  elif(isinstance(event, KillEvent)):
    for listener in listeners:
      listener.on_kill(event)

  elif(isinstance(event, ItemEvent)):
    for listener in listeners:
      listener.on_item(event)

  elif(isinstance(event, FlagEvent)):
    for listener in listeners:
      listener.on_flag(event)

  elif(isinstance(event, FlagCaptureTimeEvent)):
    for listener in listeners:
      listener.on_flag_capture_time(event)

  else:
    logging.warning('Unknown event: ' + str(event))