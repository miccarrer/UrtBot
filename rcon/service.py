from typing import Any, List
from utils.colors import Colors
from utils.rcon import send
import time

class RconService:
  ip: str
  port: int
  password: str

  color_info = Colors.LIGHT_BLUE.value
  color_success = Colors.GREEN.value
  color_error = Colors.RED.value

  last_send_time: float = 0.
  delay = 0.5
  
  def __init__(self, ip: str, port: int, password: str):
      self.ip = ip
      self.port = port
      self.password = password
  
  def send(self, request: str):
    while time.time() - self.last_send_time < self.delay:
      time.sleep(0.1)
    self.last_send_time = time.time()
    return send(self.ip, self.port, self.password, request)

  def safe_msg(self, msg: str):
    return msg.replace('\"', '').split('\n')

  def safe_content(self, content, format):
    messages = content if isinstance(content, List) else [content]
    for message in messages:
      for line in self.safe_msg(message):
        self.send(format(line))

  # rcon

  def rcon(self, var: str):
    (response_type, response_lines) = self.send(var)
    if(response_type == 'print' and len(response_lines) > 0):
      return response_lines
    else:
      return ["Command executed"]

  # say

  def say(self, content):
    self.safe_content(content, lambda line: f'say \"{line}\"')

  def say_info(self, content):
    self.safe_content(content, lambda line: f'say {self.color_info}\"{line}\"')
    
  def say_success(self, content):
    self.safe_content(content, lambda line: f'say {self.color_success}\"{line}\"')
    
  def say_error(self, content):
    self.safe_content(content, lambda line: f'say {self.color_error}\"{line}\"')
    
  # tell

  def tell(self, slot: int, content):
    self.safe_content(content, lambda line: f'tell {slot} \"{line}\"')

  def tell_info(self, slot: int, content):
    self.safe_content(content, lambda line: f'tell {slot} \"{self.color_info}{line}\"')

  def tell_success(self, slot: int, content):
    self.safe_content(content, lambda line: f'tell {slot} \"{self.color_success}{line}\"')

  def tell_error(self, slot: int, content):
    self.safe_content(content, lambda line: f'tell {slot} \"{self.color_error}{line}\"')
  
  # smite

  def smite(self, player: Any):
    self.send(f'smite {player}')