num = int(input())
even_sum = 0
odd_sum = 0

for i in range(1, num + 1):
    current_num = int(input())

    if i % 2 == 0:
        even_sum += current_num
    else:
        odd_sum += current_num

if even_sum == odd_sum:
    print(f'Yes\nSum = {even_sum}')
else:
    difference = even_sum - odd_sum
    print(f'No\nDiff = {abs(difference)}')
