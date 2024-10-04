movie_budget = float(input())
statists_amount = int(input())
price_costume_per_statist = float(input())

decoration_price = 0.10 * movie_budget

if statists_amount > 150:
    price_costume_per_statist *= 0.9

total_budget_needed = statists_amount * price_costume_per_statist + decoration_price

if total_budget_needed > movie_budget:
    print('Not enough money!')
    print(f'Wingard needs {total_budget_needed - movie_budget:.2f} leva more.')
elif total_budget_needed <= movie_budget:
    print('Action!')
    print(f'Wingard starts filming with {movie_budget - total_budget_needed:.2f} leva left.')
