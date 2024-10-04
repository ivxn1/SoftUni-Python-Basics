given_num = int(input())
is_num_prime = True
for num in range(2, given_num):
    if given_num % num == 0:
        is_num_prime = False
        break
print(is_num_prime)
