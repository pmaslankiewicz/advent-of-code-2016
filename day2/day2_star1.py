digit_map = {(-1, 1): '1', (0, 1): '2', (1, 1): '3',
             (-1, 0): '4', (0, 0): '5', (1, 0): '6',
             (-1, -1): '7', (0, -1): '8', (1, -1): '9'}

def read_file():
    with open('input2.txt') as f:
        dir_list = []
        for line in f:
            dir_list.append(line)
        return dir_list

def keyboard_move(dir_value, increment):
    dir_value += increment
    return dir_value if abs(dir_value) < 2 else dir_value / abs(dir_value)

def get_one_digit(x, y, directions):
    for letter in directions:
        x, y = {
            'U': (x, keyboard_move(y, 1)),
            'R': (keyboard_move(x, 1), y),
            'D': (x, keyboard_move(y, -1)),
            'L': (keyboard_move(x, -1), y),
            '\n': (x, y)
        }[letter]
    return x, y

def main():
    dir_list = read_file()
    x = y = 0
    bathroom_code = ""
    for directions in dir_list:
        x, y = get_one_digit(x, y, directions)
        bathroom_code += digit_map[(x, y)]
    print bathroom_code

main()