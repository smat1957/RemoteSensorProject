import time

def tail_f(filename, keyword):
    with open(filename, 'r') as f:
        f.seek(0, 2)    # move cursor to the end of the file
        while True:
            line = f.readline() # read 1 line
            if not line:    # no line was there
                time.sleep(1)
                continue
            if keyword in line:
                print(line.strip()) # print the line

if __name__=="__main__":
    tail_f('example.log', '2024')
