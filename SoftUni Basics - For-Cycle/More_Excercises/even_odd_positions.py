import sys
odd_max_num = -sys.maxsize
odd_min_num = sys.maxsize
even_max_num = -sys.maxsize
even_min_num = sys.maxsize

odd_sum = 0.00
even_sum = 0.00
nums_count = int(input())
is_no_nums = False
is_num_only_one = False

if nums_count == 0:
    is_no_nums = True
for i in range(1, nums_count + 1):
    current_num = float(input())
    if i % 2 != 0:
        if nums_count == 1:
            is_num_only_one = True
        odd_sum += current_num
        if current_num > odd_max_num:
            odd_max_num = current_num
        if current_num < odd_min_num:
            odd_min_num = current_num

    if i % 2 == 0:
        even_sum += current_num
        if current_num > even_max_num:
            even_max_num = current_num
        if current_num < even_min_num:
            even_min_num = current_num

print(f'OddSum={odd_sum:.2f},')
if is_no_nums:
    print('OddMin=No,\nOddMax=No,')
else:
    print(f'OddMin={odd_min_num:.2f},')
    print(f'OddMax={odd_max_num:.2f},')

print(f'EvenSum={even_sum:.2f},')
if is_num_only_one or is_no_nums:
    print('EvenMin=No,\nEvenMax=No')
else:
    print(f'EvenMin={even_min_num:.2f},')
    print(f'EvenMax={even_max_num:.2f}')
