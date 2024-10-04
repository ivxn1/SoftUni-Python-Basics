import sys

n = int(input())
num_sum = 0
half_sum = 0
max_num = -sys.maxsize

for _ in range(0, n):
    current_num = int(input())
    if current_num > max_num:
        max_num = current_num
    num_sum += current_num

if max_num == num_sum - max_num:
    print(f'Yes\nSum = {max_num}')
else:
    difference = max_num - (num_sum - max_num)
    print(f'No\nDiff = {abs(difference)}')
