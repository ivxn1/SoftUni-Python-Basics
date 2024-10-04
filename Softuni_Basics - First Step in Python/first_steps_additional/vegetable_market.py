price_kilo_veg = float(input())
price_kilo_fruit = float(input())
total_kilo_veg = int(input())
total_kilo_fruit = int(input())

total_price_veg = price_kilo_veg * total_kilo_veg
total_price_fruit = price_kilo_fruit * total_kilo_fruit

total_price_everything_leva = total_price_fruit + total_price_veg
total_price_everything_euro = total_price_everything_leva / 1.94
print(f'{total_price_everything_euro: .2f}')
