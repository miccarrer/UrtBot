import logging
from rcon.helper import RconHelper
import socket
from typing import Any, List
from utils.colors import Colors

rcon_request_prefix = b'\xFF' * 4
rcon_response_buffer_size = 65565

class RconService:
  ip: str
  port: int
  password: str

  sock: socket.socket

  helper: RconHelper

  color_info = Colors.LIGHT_BLUE.value
  color_success = Colors.GREEN.value
  color_error = Colors.RED.value

  def __init__(self, ip: str, port: int, password: str):
      self.ip = ip
      self.port = port
      self.password = password
      
      self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      self.sock.settimeout(5)
      self.sock.connect((ip, port))

      self.helper = RconHelper(self)

  
  def __del__(self):
    self.sock.close()

  def send(self, request: str):
    try:
      self.sock.send(rcon_request_prefix + f'rcon {self.password} {request}\n'.encode())
    except Exception as err:
      logging.error(err)

  def send_and_receive(self, request: str):
    try:
      self.sock.send(rcon_request_prefix + f'rcon {self.password} {request}\n'.encode())
      data = self.sock.recv(rcon_response_buffer_size)[len(rcon_request_prefix):-1]
      response = data.decode()
      lines = response.strip().splitlines()
      return (lines[0], lines[1:])
    except Exception as err:
      logging.error(err)
      return ('error', str(err))