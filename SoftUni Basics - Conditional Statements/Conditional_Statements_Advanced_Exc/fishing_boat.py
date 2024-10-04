budget_group = int(input())
season = input()
fishermen_count = int(input())
boat_rent = 0
final_price = 0
discount = 0
extra_discount = 0

if season == 'Spring':
    boat_rent = 3000
elif season == 'Summer' or season == 'Autumn':
    boat_rent = 4200
elif season == 'Winter':
    boat_rent = 2600

if fishermen_count <= 6:
    discount = 0.10
elif 7 <= fishermen_count <= 11:
    discount = 0.15
elif fishermen_count >= 12:
    discount = 0.25

if fishermen_count % 2 == 0 and season != 'Autumn':
    extra_discount = 0.05

final_price = boat_rent * (1 - discount) * (1 - extra_discount)

if budget_group >= final_price:
    money_left = budget_group - final_price
    print(f'Yes! You have {money_left:.2f} leva left.')
else:
    money_needed = final_price - budget_group
    print(f'Not enough money! You need {money_needed:.2f} leva.')
