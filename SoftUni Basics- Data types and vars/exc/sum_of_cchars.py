chars = int(input())
total_sum = 0
for i in range(1, chars + 1):
    char = input()
    total_sum += ord(char)

print(f'The sum equals: {total_sum}')
