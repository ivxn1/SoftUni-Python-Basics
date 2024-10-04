n = int(input())

for current_number in range(1111, 10_000):
    is_num_magic = True
    num_to_str = str(current_number)
    for digit in num_to_str:
        digit = int(digit)
        if digit == 0:
            is_num_magic = False
            break
        if n % digit != 0:
            is_num_magic = False
            break

    if is_num_magic:
        print(current_number, end=' ')
