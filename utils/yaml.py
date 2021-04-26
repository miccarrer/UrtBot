
from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

def load_yaml(filepath):
  return load(open(filepath, 'r'), Loader=Loader)