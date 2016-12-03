symbol_map = {(0, 2): '1', (0, -2): 'D', (-2, 0): '5', (2, 0): '9',
              (-1, 1): '2', (0, 1): '3', (1, 1): '4',
              (-1, 0): '6', (0, 0): '7', (1, 0): '8',
              (-1, -1): 'A', (0, -1): 'B', (1, -1): 'C'}

def read_file():
    with open('input2.txt') as f:
        dir_list = []
        for line in f:
            dir_list.append(line)
        return dir_list

def keyboard_move(x, y, x_increment, y_increment):
    new_x, new_y = x + x_increment, y + y_increment
    dist = city_dist(new_x, new_y)
    return (x, y) if dist > 2 else (new_x, new_y)

def city_dist(x, y):
    return abs(x) + abs(y)

def get_one_digit(x, y, directions):
    for letter in directions:
        x, y = {
            'U': (keyboard_move(x, y, 0, 1)),
            'R': (keyboard_move(x, y, 1, 0)),
            'D': (keyboard_move(x, y, 0, -1)),
            'L': (keyboard_move(x, y, -1, 0)),
            '\n': (x, y)
        }[letter]
    return x, y

def main():
    dir_list = read_file()
    x = y = 0
    bathroom_code = ""
    for directions in dir_list:
        x, y = get_one_digit(x, y, directions)
        bathroom_code += symbol_map[(x, y)]
    print bathroom_code

main()