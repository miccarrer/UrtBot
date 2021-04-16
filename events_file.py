import time


def get_line_count(filepath):
    with open(filepath, 'r') as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def observe(filepath, on_new_line):
    ignore_line_count = get_line_count(filepath)
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
            if(current_line > ignore_line_count):
                on_new_line(line)
