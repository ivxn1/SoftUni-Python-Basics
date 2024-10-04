degrees_weather = int(input())
part_of_day = input()
Outfit = ''
Shoes = ''
if part_of_day == 'Morning':
    if 10 <= degrees_weather <= 18:
        Outfit = 'Sweatshirt'
        Shoes = 'Sneakers'
    elif 18 < degrees_weather <= 24:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
    elif degrees_weather >= 25:
        Outfit = 'T-Shirt'
        Shoes = 'Sandals'
elif part_of_day == 'Afternoon':
    if 10 <= degrees_weather <= 18:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
    elif 18 < degrees_weather <= 24:
        Outfit = 'T-Shirt'
        Shoes = 'Sandals'
    elif degrees_weather >= 25:
        Outfit = 'Swim Suit'
        Shoes = 'Barefoot'
elif part_of_day == 'Evening':
    if 10 <= degrees_weather <= 18:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
    elif 18 < degrees_weather <= 24:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
    elif degrees_weather >= 25:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
print(f'It\'s {degrees_weather} degrees, get your {Outfit} and {Shoes}.')
