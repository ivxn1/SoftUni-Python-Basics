season = input()
type_group = input()
students_count = int(input())
nights_count = int(input())

price_per_night = 0
sport = ''
discount = 0

if season == 'Winter':
    if type_group == 'girls' or type_group == 'boys':
        price_per_night = 9.60
        if type_group == 'girls':
            sport = 'Gymnastics'
        elif type_group == 'boys':
            sport = 'Judo'
    elif type_group == 'mixed':
        price_per_night = 10
        sport = 'Ski'
    if students_count >= 50:
        discount = 0.50
    elif 20 <= students_count < 50:
        discount = 0.15
    elif 10 <= students_count < 20:
        discount = 0.05
elif season == 'Spring':
    if type_group == 'girls' or type_group == 'boys':
        price_per_night = 7.20
        if type_group == 'girls':
            sport = 'Athletics'
        elif type_group == 'boys':
            sport = 'Tennis'
    elif type_group == 'mixed':
        price_per_night = 9.50
        sport = 'Cycling'
    if students_count >= 50:
        discount = 0.50
    elif 20 <= students_count < 50:
        discount = 0.15
    elif 10 <= students_count < 20:
        discount = 0.05
elif season == 'Summer':
    if type_group == 'girls' or type_group == 'boys':
        price_per_night = 15
        if type_group == 'girls':
            sport = 'Volleyball'
        elif type_group == 'boys':
            sport = 'Football'
    elif type_group == 'mixed':
        sport = 'Swimming'
        price_per_night = 20
    if students_count >= 50:
        discount = 0.50
    elif 20 <= students_count < 50:
        discount = 0.15
    elif 10 <= students_count < 20:
        discount = 0.05

final_price = nights_count * price_per_night * students_count * (1 - discount)

print(f'{sport} {final_price:.2f} lv.')
