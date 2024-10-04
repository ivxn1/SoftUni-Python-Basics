lenght_meters = float(input())
width_meters = float(input())

lenght_cm = lenght_meters * 100
width_cm = width_meters * 100

corridor_width_cm = 100
width_without_corridor = width_cm - corridor_width_cm
seats_in_a_row = width_without_corridor // 70

rows_seats = lenght_cm // 120

seats_total = rows_seats * seats_in_a_row

final_amount_seats = seats_total - 3
print(final_amount_seats)
