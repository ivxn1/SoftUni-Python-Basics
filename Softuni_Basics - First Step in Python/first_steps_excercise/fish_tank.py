length_cm = int(input())
width_cm = int(input())
height_cm = int(input())
procent_taken = float(input())
procent_taken_as_procent = procent_taken / 100

volume_tank_litres = length_cm * width_cm * height_cm / 1000
water_volume = volume_tank_litres * (1 - procent_taken_as_procent)
print(water_volume)