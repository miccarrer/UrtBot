import time

def observe(filepath, on_new_line, starting_line_number=0):
  current_line = 0
  with open(filepath) as file:
    while 1:
        where = file.tell()
        line = file.readline()
        if not line:
            time.sleep(0.1)
            file.seek(where)
        else:
          current_line += 1
          if(current_line > starting_line_number):
            on_new_line(line)
