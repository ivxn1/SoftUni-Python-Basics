n = int(input())
print('+', (n-2)*'-', '+')
for row in range(2, n):
    for col in range(1, row):
        print('|', (n-2)*'-', '|')
print('+', (n-2)*'-', '+')
