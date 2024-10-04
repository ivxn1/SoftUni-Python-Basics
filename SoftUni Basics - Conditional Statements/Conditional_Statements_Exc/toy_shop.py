trip_price = float(input())
bought_puzzles = int(input())
bought_dolls = int(input())
bought_teddy_bears = int(input())
bought_minions = int(input())
bought_trucks = int(input())

total_bought_toys = bought_trucks + bought_minions + bought_dolls + bought_puzzles + bought_teddy_bears
discount = 0

total_revenue = bought_trucks * 2.00 \
                + bought_dolls * 3.00 \
                + bought_puzzles * 2.60\
                + bought_minions * 8.20 \
                + bought_teddy_bears * 4.10

if total_bought_toys >= 50:
    discount = 0.25

total_revenue_after_disc = total_revenue * (1 - discount)

total_profit = total_revenue_after_disc * (1 - 0.1)

if total_profit >= trip_price:
    print(f'Yes!{total_profit - trip_price:.2f} lv left.')
else:
    print(f'Not enough money!{trip_price - total_profit:.2f} lv needed.')
