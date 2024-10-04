gained_money = float(input())
past_year = int(input())
current_age = 18
spent_money = 0

for year in range(1800, past_year + 1):
    if year == 1800:
        spent_money += 12000
        current_age += 1
    elif year % 2 != 0:
        spent_money += 12000 + 50 * current_age
        current_age += 1
    else:
        spent_money += 12000
        current_age += 1

if gained_money >= spent_money:
    remainder = gained_money - spent_money
    print(f'Yes! He will live a carefree life and will have {remainder:.2f} dollars left.')
else:
    needed_money = spent_money - gained_money
    print(f'He will need {needed_money:.2f} dollars to survive.')
