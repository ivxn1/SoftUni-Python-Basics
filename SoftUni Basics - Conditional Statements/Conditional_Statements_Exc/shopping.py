petars_budget = float(input())
videocards_count = int(input())
processors_count = int(input())
ram_count = int(input())
discount = 0

total_videocard_price = videocards_count * 250
processor_single_price = 0.35 * total_videocard_price
ram_single_price = 0.10 * total_videocard_price

total_price = total_videocard_price\
               + processor_single_price\
               * processors_count\
               + ram_single_price\
               * ram_count

if videocards_count > processors_count:
    discount = 0.15
    total_price *= 0.85

if petars_budget >= total_price:
    remainder = petars_budget - total_price
    print(f'You have {remainder:.2f} leva left!')
else:
    needed_money = total_price - petars_budget
    print(f'Not enough money! You need {needed_money:.2f} leva more!')
