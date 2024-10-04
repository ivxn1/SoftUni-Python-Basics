from math import floor, ceil
days_away = int(input())
total_kilos_food_left = int(input())
dog_food_per_day_kilos = float(input())
cat_food_per_day_kilos = float(input())
turtle_food_per_day_grams = float(input())
turtle_food_per_day_kilos = turtle_food_per_day_grams / 1000

total_dog_food = days_away * dog_food_per_day_kilos
total_cat_food = days_away * cat_food_per_day_kilos
total_turtle_food = days_away * turtle_food_per_day_kilos

total_food_all_animals = total_turtle_food + total_cat_food + total_dog_food

if total_kilos_food_left >= total_food_all_animals:
    print(f'{floor(total_kilos_food_left - total_food_all_animals)}'
          f' kilos of food left.')
else:
    print(f'{ceil(total_food_all_animals - total_kilos_food_left)} '
          f'more kilos of food are needed.')
