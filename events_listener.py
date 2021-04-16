from events import *

class GameEventListener(object):

  def on_separator(self, event: SeparatorEvent):
    pass

  def on_init_game(self, event: InitGameEvent):
    pass

  def on_init_round(self, event: InitRoundEvent):
    pass

  def on_init_auth(self, event: InitAuthEvent):
    pass

  def on_shutdown_game(self, event: ShutdownGameEvent):
    pass

  def on_warmup(self, event: WarmUpEvent):
    pass

  def on_session_data_initialised(self, event: SessionDataInitialisedEvent):
    pass

  def on_client_connect(self, event: ClientConnectEvent):
    pass

  def on_client_disconnect(self, event: ClientDisconnectEvent):
    pass

  def on_client_userinfo(self, event: ClientUserinfoEvent):
    pass

  def on_client_userinfo_changed(self, event: ClientUserinfoChangedEvent):
    pass

  def on_client_begin(self, event: ClientBeginEvent):
    pass

  def on_client_spawn(self, event: ClientSpawnEvent):
    pass

  def on_account_validated(self, event: AccountValidatedEvent):
    pass

  def on_say(self, event: SayEvent):
    pass
    
  def on_saytell(self, event: SayTellEvent):
    pass
    
  def on_sayteam(self, event: SayTeamEvent):
    pass
    
  def on_tell(self, event: TellEvent):
    pass
    
  def on_kill(self, event: KillEvent):
    pass

  def on_item(self, event: ItemEvent):
    pass

  def on_flag(self, event: FlagEvent):
    pass

  def on_flag_capture_time(self, event: FlagCaptureTimeEvent):
    pass