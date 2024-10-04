lily_age = int(input())
washing_machine_price = float(input())
price_per_toy = int(input())

toys = 0
birthday_money = 0
budget = 0

for year in range(1, lily_age + 1):
    if year % 2 != 0:
        toys += 1
    else:
        birthday_money = year * 5
        budget += birthday_money
        budget -= 1

sold_toys = toys * price_per_toy
budget += sold_toys

if budget >= washing_machine_price:
    remainder = budget - washing_machine_price
    print(f'Yes! {remainder:.2f}')
else:
    needed_money = washing_machine_price - budget
    print(f'No! {needed_money:.2f}')
