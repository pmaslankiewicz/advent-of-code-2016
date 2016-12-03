turns = {'L': -1, 'R': 1}

def read_coordinates(direction):
    turn = turns[direction[0]]
    steps = int(direction[1:])
    return turn, steps

def read_file():
    with open('input1.txt', 'r') as f:
        for line in f:
            return line.split(', ')

def calculate_distance(x, y):
    return abs(x) + abs(y)

def increment_step(dir_num, x, y):
    return {
        0: (x, y+1),
        1: (x+1, y),
        2: (x, y-1),
        3: (x-1, y),
    }[dir_num]

def main():
    dir_list = read_file()
    visited_set = set()
    x = y = dir_num = 0
    found = False
    for direction in dir_list:
        if found:
            break
        turn, steps = read_coordinates(direction)
        dir_num = (dir_num + turn) % 4
        for step in range(steps):
            if (x, y) not in visited_set:
                visited_set.add((x, y))
            else:
                print "distance: %d" % calculate_distance(x, y)
                found = True
                break
            x, y = increment_step(dir_num, x, y)

main()