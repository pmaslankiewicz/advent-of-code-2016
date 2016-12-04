def read_file():
    with open('input4.txt') as f:
        room_list = []
        for line in f:
            room_list.append(line.strip())
        return room_list

def divide_input(room_code):
    letters = room_code.rsplit('-', 1)[0].replace('-', '')
    number = room_code.rsplit('-', 1)[1].rsplit('[', 1)[0]
    checksum = room_code.rsplit('-', 1)[1].rsplit('[', 1)[1].replace(']', '')
    return letters, number, checksum

def letters_to_count_dict(letters):
    count_to_letter_dict = {}
    for letter in letters:
        if letter in count_to_letter_dict.keys():
            count_to_letter_dict[letter] += 1
        else:
            count_to_letter_dict[letter] = 1
    return count_to_letter_dict

def count_dict_to_checksum(count_dict):
    checksum = ""
    for i in range(5):
        highest_letter = ''
        highest_count = 0
        # alphabetic_letter_list = count_dict.keys().sort()
        for letter in sorted(count_dict):
            if count_dict[letter] > highest_count:
                highest_letter = letter
                highest_count = count_dict[letter]
        checksum += highest_letter
        count_dict.pop(highest_letter)
    return checksum

def main():
    room_list = read_file()
    num_sum = 0
    for room_code in room_list:
        letters, number, checksum = divide_input(room_code)
        print divide_input(room_code)
        real_checksum = count_dict_to_checksum(letters_to_count_dict(letters))
        print real_checksum
        print checksum == real_checksum
        if checksum == real_checksum:
            num_sum += int(number)
        print num_sum
    print "sum of room codes: %d" % num_sum