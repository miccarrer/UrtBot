import socket, struct

rcon_request_prefix = b'\xFF' * 4
rcon_request_suffix = b'\x00' * 2
rcon_response_buffer_size = 65565


def send(ip, port, password, rcon_request):

    try:
      request = f'rcon {password} {rcon_request}\n'
      request_bytes = request.encode()

      sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      sock.connect((ip, port))
      sock.send(rcon_request_prefix + request_bytes + rcon_request_suffix)
      response_bytes = sock.recv(rcon_response_buffer_size)
      sock.close()

      response_bytes = response_bytes[len(rcon_request_prefix):]
      response = response_bytes.decode()

      all_response_lines = response.splitlines()

      response_type = all_response_lines[0]
      response_lines = all_response_lines[1:]

      return (response_type, response_lines)
    except print(0):
        pass

