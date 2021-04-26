
from typing import Any


class RconHelper:
  service: Any

  def __init__(self, service: Any):
      self.service = service

  def send(self, request):
    return self.service.send_and_receive(request)

  def say(self, message: str):
    for line in message.splitlines():
      self.service.send(f'say \"{line}\"')

  def tell(self, slot, message: str):
    for line in message.splitlines():
      self.service.send(f'tell {slot} \"{line}\"')

  def smite(self, slot):
    self.service.send(f'smite {slot}')