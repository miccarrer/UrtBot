from events import GameEvent
import sys, os, logging
from events_file import observe
from events_reader import read_one
from events_dispatcher import dispatch
from properties import log_file

def main():
  logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
  logging.info('Starting bot..')

  events=[]

  def on_event(event: GameEvent):
    dispatch(event)
    events.append(event)

  observe(log_file, lambda newline: on_event(read_one(newline)))

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)