num1 = int(input())
num2 = int(input())

for nums in range(num1, num2 + 1):
    num_to_str = str(nums)
    even_sum = 0
    odd_sum = 0
    for index, digit in enumerate(num_to_str):
        if index % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    if even_sum == odd_sum:
        print(nums, end=" ")
