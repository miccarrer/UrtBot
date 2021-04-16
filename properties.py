
from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

data = load(open('properties.yaml', 'r'), Loader=Loader)

log_file = data["log_file"]
ip = data["ip"]
port = data["port"]
password = data["password"]