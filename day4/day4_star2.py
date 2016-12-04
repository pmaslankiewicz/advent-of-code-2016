from string import ascii_lowercase as al
import day4_star1

alphabet = {x: i for i, x in enumerate(al, 0)}

def read_file():
    with open('input4.txt') as f:
        room_list = []
        for line in f:
            room_list.append(line.strip())
        return room_list

def decrypt(letters, shift):
    plaintext = ''
    for letter in letters:
        plaintext_index = (alphabet[letter] + shift) % 26
        plaintext += alphabet.keys()[alphabet.values().index(plaintext_index)]
    return plaintext

def main():
    room_list = read_file()
    expected_name = 'northpoleobjects'
    for room_code in room_list:
        letters, number, checksum = day4_star1.divide_input(room_code)
        real_checksum = day4_star1.count_dict_to_checksum(day4_star1.letters_to_count_dict(letters))
        room_name = decrypt(letters, int(number))
        if (checksum == real_checksum) & (expected_name in room_name):
            print "code is: %s" % number

main()
