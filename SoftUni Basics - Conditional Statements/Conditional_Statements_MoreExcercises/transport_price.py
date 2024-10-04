n_kilometers_travelled = int(input())
part_of_day = input()

taxi_start_cost = 0.70
taxi_cost_per_km = 0
bus_cost_km = 0.09  # minimum 20 km
train_cost_km = 0.06    # minimum 100 km

if part_of_day == 'day':
    taxi_cost_per_km = 0.79
elif part_of_day == 'night':
    taxi_cost_per_km = 0.90

if n_kilometers_travelled < 20:
    print(f'{n_kilometers_travelled * taxi_cost_per_km + taxi_start_cost:.2f}')
elif 20 <= n_kilometers_travelled <= 100:
    print(f'{n_kilometers_travelled * bus_cost_km:.2f}')
elif n_kilometers_travelled >= 100:
    print(f'{n_kilometers_travelled * train_cost_km:.2f}')
