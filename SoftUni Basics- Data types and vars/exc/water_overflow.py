actions = int(input())
capacity = 255
for i in range(0, actions):
    current_litres = int(input())
    if capacity - current_litres < 0:
        print('Insufficient capacity!')
        continue
    capacity -= current_litres

print(255 - capacity)
