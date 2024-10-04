symbol = input()
word = ''
final_word = ''
found_symbol = 0
first_found = 0
first_c = 0
first_o = 0
first_n = 0
while symbol != 'End':
    if symbol in ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-',
                  '_', '+', '=', ',', '<', '>', '?', '/', ';', ':', '{', '}', '[', ']']:
        continue
    if symbol == 'c':
        if first_c == 1:
            word += symbol
            symbol = input()
            continue
        elif first_c > 1:
            word += symbol
        first_found += 1
        first_c += 1
        if first_found == 3:
            final_word += word
            word = ''
        symbol = input()
        continue
    elif symbol == 'o':
        if first_o == 1:
            word += symbol
            symbol = input()
            continue
        elif first_o > 1:
            word += symbol
        first_o += 1
        first_found += 1
        if first_found == 3:
            final_word += word
            word = ''
        symbol = input()
        continue
    elif symbol == 'n':
        if first_n == 1:
            word += symbol
            symbol = input()
            continue
        elif first_n > 1:
            word += symbol
        first_n += 1
        first_found += 1
        if first_found == 3:
            final_word += word
            word = ''
        symbol = input()
        continue
    word += symbol
    symbol = input()

print(final_word)
