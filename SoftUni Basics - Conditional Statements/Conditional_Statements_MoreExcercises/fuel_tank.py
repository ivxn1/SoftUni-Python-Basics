type_fuel = input()
fuel_in_tank_litres = float(input())

if type_fuel == ('Diesel'):
    if fuel_in_tank_litres >= 25:
        print('You have enough diesel.')
    else:
        print('Fill your tank with diesel!')
elif type_fuel == 'Gas':
    if fuel_in_tank_litres >= 25:
        print(f'You have enough gas.')
    else:
        print(f'Fill your tank with gas!')
elif type_fuel == 'Gasoline':
    if fuel_in_tank_litres >= 25:
        print(f'You have enough gasoline.')
    else:
        print(f'Fill your tank with gasoline!')
else:
    print('Invalid fuel!')
