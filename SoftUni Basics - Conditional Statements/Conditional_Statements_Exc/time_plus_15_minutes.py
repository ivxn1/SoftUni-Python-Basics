current_hour = int(input())
current_min = int(input())

plus_15_min = current_min + 15

if plus_15_min >= 60:
    plus_15_min = plus_15_min - 60  # plus_15_min -= 60
    current_hour = current_hour + 1     # current_hour += 1

if current_hour >= 24:
    current_hour = 0

print(f'{current_hour}:{plus_15_min:02d}')
