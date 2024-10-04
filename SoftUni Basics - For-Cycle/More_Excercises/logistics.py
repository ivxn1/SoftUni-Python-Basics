cargo_count = int(input())
c1_tons = 0
c2_tons = 0
c3_tons = 0

for cargo in range(cargo_count):
    weight_cargo = int(input())
    if weight_cargo <= 3:
        c1_tons += weight_cargo
    elif 4 <= weight_cargo <= 11:
        c2_tons += weight_cargo
    elif weight_cargo >= 12:
        c3_tons += weight_cargo

total_tons = c1_tons + c2_tons + c3_tons

total_cargo_cost = c1_tons * 200 + c2_tons * 175\
    + c3_tons * 120

average_price_cargo = total_cargo_cost / total_tons

c1_percent = c1_tons / total_tons
c2_percent = c2_tons / total_tons
c3_percent = c3_tons / total_tons

print(f'{average_price_cargo:.2f}')
print(f'{c1_percent:.2%}')
print(f'{c2_percent:.2%}')
print(f'{c3_percent:.2%}')
