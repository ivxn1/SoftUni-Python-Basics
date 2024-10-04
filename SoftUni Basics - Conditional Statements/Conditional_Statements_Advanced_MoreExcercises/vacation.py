budget = float(input())
season = input()
accommodation = ''
destination = ''
price_trip = 0

if budget <= 1000:
    accommodation = 'Camp'
    if season == 'Summer':
        destination = 'Alaska'
        price_trip = 0.65 * budget
    elif season == 'Winter':
        destination = 'Morocco'
        price_trip = 0.45 * budget
elif 1000 < budget <= 3000:
    accommodation = 'Hut'
    if season == 'Summer':
        destination = 'Alaska'
        price_trip = 0.80 * budget
    elif season == 'Winter':
        destination = 'Morocco'
        price_trip = 0.60 * budget
elif budget > 3000:
    accommodation = 'Hotel'
    price_trip = 0.90 * budget
    if season == 'Summer':
        destination = 'Alaska'
    elif season == 'Winter':
        destination = 'Morocco'

print(f'{destination} - {accommodation} - {price_trip:.2f}')
