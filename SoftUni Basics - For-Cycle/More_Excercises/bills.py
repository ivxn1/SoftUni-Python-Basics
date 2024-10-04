months_count = int(input())
total_electricity = 0
total_water = 0
total_net = 0
total_others = 0
for _ in range(months_count):
    electricity_month = float(input())
    total_electricity += electricity_month

    water_month = 20
    total_water += water_month

    net_month = 15
    total_net += net_month

    others_month = (water_month + electricity_month + net_month) * (1 + 0.20)
    total_others += others_month

average_monthly = (total_others + total_net + total_electricity + total_water) / months_count

print(f'Electricity: {total_electricity:.2f} lv')
print(f'Water: {total_water:.2f} lv')
print(f'Internet: {total_net:.2f} lv')
print(f'Other: {total_others:.2f} lv')
print(f'Average: {average_monthly:.2f} lv')
