month_of_visit = input()
nights_count = int(input())
apartment_price_per_night = 0
studio_price_per_night = 0

if month_of_visit == 'May' or month_of_visit == 'October':
    studio_price_per_night = 50
    apartment_price_per_night = 65
    if 7 < nights_count < 14:
        studio_price_per_night *= 0.95
    elif nights_count > 14:
        studio_price_per_night *= 0.70
elif month_of_visit == 'June' or month_of_visit == 'September':
    studio_price_per_night = 75.20
    apartment_price_per_night = 68.70
    if nights_count > 14:
        studio_price_per_night *= 0.80
elif month_of_visit == 'July' or month_of_visit == 'August':
    studio_price_per_night = 76
    apartment_price_per_night = 77

if nights_count > 14:
    apartment_price_per_night *= 0.90

total_price_apartment = apartment_price_per_night * nights_count
total_price_studio = studio_price_per_night * nights_count

print(f'Apartment: {total_price_apartment:.2f} lv.')
print(f'Studio: {total_price_studio:.2f} lv.')
