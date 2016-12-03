turns = {'L': -1, 'R': 1}

def update_position(x, y, dir_num, turn, steps):
    dir_num = (dir_num + turn) % 4
    return {
        0: (x, y + steps, 0),
        1: (x + steps, y, 1),
        2: (x, y - steps, 2),
        3: (x - steps, y, 3),
    }[dir_num]

def read_coordinates(direction):
    turn = turns[direction[0]]
    steps = int(direction[1:])
    return turn, steps

def calculate_distance(x, y):
    return abs(x) + abs(y)

def read_file():
    with open('input1.txt', 'r') as f:
        for line in f:
            return line.split(', ')

def main():
    dir_list = read_file()
    x = y = dir_num = 0
    for direction in dir_list:
        turn, steps = read_coordinates(direction)
        x, y, dir_num = update_position(x, y, dir_num, turn, steps)

    print calculate_distance(x, y)

main()