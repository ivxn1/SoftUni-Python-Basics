from math import floor, ceil
X_area_land = int(input())
Y_grapes_for_one_m2 = float(input())
Z_needed_litres_wine = int(input())
workers = int(input())

area_for_wine = 0.4 * X_area_land
kilos_grapes_from_that_area = area_for_wine * Y_grapes_for_one_m2
litres_produced_wine = kilos_grapes_from_that_area / 2.5

if litres_produced_wine >= Z_needed_litres_wine:
    print(f'Good harvest this year! Total wine: {floor(litres_produced_wine)} litres.')
    wine_remainder = litres_produced_wine - Z_needed_litres_wine
    print(f'{ceil(wine_remainder)} liters left ->'
          f' {ceil(wine_remainder // workers)} liters per person.')
else:
    print(f'It will be a tough winter!'
          f' More {floor(Z_needed_litres_wine - litres_produced_wine)} liters wine needed.')
