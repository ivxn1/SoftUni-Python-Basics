num = int(input())
left_sum = 0
right_sum = 0

for _ in range(num):
    current_num = int(input())
    left_sum += current_num

for _ in range(num):
    current_num = int(input())
    right_sum += current_num

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    difference = left_sum - right_sum
    print(f'No, diff = {abs(difference)}')
