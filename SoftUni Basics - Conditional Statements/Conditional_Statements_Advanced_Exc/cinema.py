type_movie = input()
rows = int(input())
columns = int(input())

total_seats = rows * columns
total_income = 0

if type_movie == 'Premiere':
    total_income = total_seats * 12
elif type_movie == 'Normal':
    total_income = total_seats * 7.50
elif type_movie == 'Discount':
    total_income = total_seats * 5

print(f'{total_income:.2f} leva')
