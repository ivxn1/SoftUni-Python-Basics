type_fuel = input()
litres_fuel = float(input())
club_card = input()

price_per_liter = 0

if type_fuel == 'Gas':
    price_per_liter = 0.93
    if club_card == 'Yes':
        price_per_liter = price_per_liter - 0.08
elif type_fuel == 'Gasoline':
    price_per_liter = 2.22
    if club_card == 'Yes':
        price_per_liter = price_per_liter - 0.18
elif type_fuel == 'Diesel':
    price_per_liter = 2.33
    if club_card == 'Yes':
        price_per_liter = price_per_liter - 0.12

final_price = litres_fuel * price_per_liter
if 20 <= litres_fuel <= 25:
    final_price *= 0.92
elif litres_fuel > 25:
    final_price *= 0.90

print(f'{final_price:.2f} lv.')
