budget = float(input())
season = input()
destination = 0
price_journey = 0
type_journey = 0

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        type_journey = 'Camp'
        price_journey = 0.3 * budget
    elif season == 'winter':
        price_journey = 0.7 * budget
        type_journey = 'Hotel'
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        type_journey = 'Camp'
        price_journey = 0.4 * budget
    elif season == 'winter':
        type_journey = 'Hotel'
        price_journey = 0.8 * budget
elif budget > 1000:
    destination = 'Europe'
    if season == 'summer' or season == 'winter':
        price_journey = 0.9 * budget
        type_journey = 'Hotel'

print(f'Somewhere in {destination}')
print(f'{type_journey} - {price_journey:.2f}')
