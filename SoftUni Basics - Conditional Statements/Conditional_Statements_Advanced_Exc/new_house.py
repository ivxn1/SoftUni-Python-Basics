type_flowers = input()
flowers_count = int(input())
budget = int(input())
single_price = 0
discount = 0

if type_flowers == 'Roses':
    single_price = 5
    if flowers_count > 80:
        discount = 0.10
elif type_flowers == 'Dahlias':
    single_price = 3.80
    if flowers_count > 90:
        discount = 0.15
elif type_flowers == 'Tulips':
    single_price = 2.80
    if flowers_count > 80:
        discount = 0.15
elif type_flowers == 'Narcissus':
    single_price = 3
    if flowers_count < 120:
        discount = -0.15
elif type_flowers == 'Gladiolus':
    single_price = 2.50
    if flowers_count < 80:
        discount = -0.20

final_price = (flowers_count * single_price) * (1 - discount)

if budget >= final_price:
    money_left = budget - final_price
    print(f'Hey, you have a great garden with {flowers_count} {type_flowers} and {money_left:.2f} leva left.')
else:
    needed_money = final_price - budget
    print(f'Not enough money, you need {needed_money:.2f} leva more.')
