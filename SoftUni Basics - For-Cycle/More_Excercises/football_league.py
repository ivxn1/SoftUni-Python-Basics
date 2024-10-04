stadium_capacity = int(input())
total_fans = int(input())
A_fans = 0
B_fans = 0
V_fans = 0
G_fans = 0
for _ in range(total_fans):
    current_sector = input()
    if current_sector == 'A':
        A_fans += 1
    elif current_sector == 'B':
        B_fans += 1
    elif current_sector == 'V':
        V_fans += 1
    elif current_sector == 'G':
        G_fans += 1

A_percent = A_fans / total_fans
B_percent = B_fans / total_fans
V_percent = V_fans / total_fans
G_percent = G_fans / total_fans
total_fans_percent = total_fans / stadium_capacity

print(f'{A_percent:.2%}')
print(f'{B_percent:.2%}')
print(f'{V_percent:.2%}')
print(f'{G_percent:.2%}')
print(f'{total_fans_percent:.2%}')
