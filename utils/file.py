import time


def get_line_count(filepath):
    with open(filepath, 'r') as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def observe(filepath, on_new_line, starting_line_number=0):
    with open(filepath, 'r') as f:
        current_line = 0
        while True:
            current_line += 1
            line = ''
            while len(line) == 0 or line[-1] != '\n':
                tail = f.readline()
                if tail == '':
                    time.sleep(0.1)
                    continue
                line += tail
            if(current_line > starting_line_number):
                on_new_line(line.strip())
                time.sleep(1)
