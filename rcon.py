import socket
from properties import ip, port, password

def send(str):
    full_str = "\xFF\xFF\xFF\xFFrcon " + password + " " + str
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect((ip, port))
    s_new: bytes = bytes(full_str, encoding="raw_unicode_escape")
    sock.send(s_new)
    response = sock.recv(65565)
    sock.close()
    return response
