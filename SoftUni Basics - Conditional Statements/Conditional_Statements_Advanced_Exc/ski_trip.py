days_of_stay = int(input())
type_room = input()
rate = input()

nights_spend = days_of_stay - 1
total_price_stay = 0
price_per_night = 0
discount = 0

if type_room == 'room for one person':
    price_per_night = 18
elif type_room == 'apartment':
    price_per_night = 25
    if days_of_stay < 10:
        discount = 0.30
    elif 10 < days_of_stay < 15:
        discount = 0.35
    elif days_of_stay > 15:
        discount = 0.50
elif type_room == 'president apartment':
    price_per_night = 35
    if days_of_stay < 10:
        discount = 0.10
    elif 10 < days_of_stay < 15:
        discount = 0.15
    elif days_of_stay > 15:
        discount = 0.20

total_price_stay = nights_spend * price_per_night * (1 - discount)

if rate == 'positive':
    total_price_stay *= 1.25
else:
    total_price_stay *= 0.90

print(f'{total_price_stay:.2f}')
