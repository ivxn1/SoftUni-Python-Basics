n = int(input())
print(2*n*'*', n*' ', 2*n*'*')
for row in range(n - 2):
    print('*', (2*n-2)*'/', '*', n*' ', '*', (2*n-2)*'/', '*')
    if row == (n-1)/2 - 1:
        print('*', (2 * n - 2) * '/', '*', n * '|', '*', (2 * n - 2) * '/', '*')

print(2*n*'*', n*' ', 2*n*'*')