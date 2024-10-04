n = int(input())
current_num = 1
is_num_bigger = False
for row in range(1, n + 1):
    for nums in range(1, row + 1):
        if current_num > n:
            is_num_bigger = True
            break

        print(current_num, end=' ')
        current_num += 1
    if is_num_bigger:
        break
    print()
