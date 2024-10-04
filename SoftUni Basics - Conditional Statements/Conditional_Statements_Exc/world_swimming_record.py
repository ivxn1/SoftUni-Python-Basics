current_record_seconds = float(input())
distance_meters = float(input())
seconds_for_a_meter = float(input())
water_resistance_seconds = 0

if distance_meters >= 15:
    water_resistance_seconds = (distance_meters // 15) * 12.5

final_time_ivan = water_resistance_seconds + distance_meters * seconds_for_a_meter

if final_time_ivan < current_record_seconds:
    print(f'Yes, he succeeded! The new world record is {final_time_ivan:.2f} seconds.')
else:
    print(f'No, he failed! He was {final_time_ivan - current_record_seconds:.2f} seconds slower.')
