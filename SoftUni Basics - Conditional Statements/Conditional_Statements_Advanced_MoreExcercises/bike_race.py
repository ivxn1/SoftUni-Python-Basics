juniors = int(input())
seniors = int(input())
type_race = input()
price_junior = 0
price_senior = 0
total_competitors = juniors + seniors

if type_race == 'trail':
    price_senior = 7
    price_junior = 5.50
    if total_competitors >= 50:
        price_senior *= 0.75
        price_junior *= 0.75
elif type_race == 'cross-country':
    price_senior = 9.50
    price_junior = 8
    if total_competitors >= 50:
        price_senior *= 0.75
        price_junior *= 0.75
elif type_race == 'downhill':
    price_senior = 13.75
    price_junior = 12.25
    if total_competitors >= 50:
        price_senior *= 0.75
        price_junior *= 0.75
elif type_race == 'road':
    price_senior = 21.50
    price_junior = 20
    if total_competitors >= 50:
        price_senior *= 0.75
        price_junior *= 0.75

total_profit = price_junior * juniors + price_senior * seniors

expenses = 0.05
total_profit_after_expenses = total_profit * (1 - expenses)

print(f'{total_profit_after_expenses:.2f}')
