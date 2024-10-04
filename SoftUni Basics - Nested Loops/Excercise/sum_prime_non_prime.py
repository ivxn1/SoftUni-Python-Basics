command = input()
prime_sum = 0
non_prime_sum = 0

while command != 'stop':
    current_num = int(command)

    if current_num < 0:
        print('Number is negative.')
        command = input()
        continue

    is_num_prime = True
    for divisor in range(2, current_num):
        if current_num % divisor == 0:
            is_num_prime = False
            break
        else:
            is_num_prime = True
    if is_num_prime:
        prime_sum += current_num
    else:
        non_prime_sum += current_num

    command = input()

print(f'Sum of all prime numbers is: {prime_sum}')
print(f'Sum of all non prime numbers is: {non_prime_sum}')
