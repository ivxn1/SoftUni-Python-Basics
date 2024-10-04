bought_chrysanthemums = int(input())
bought_roses = int(input())
bought_tulips = int(input())
season = input()
is_holiday = input()

single_price_chrysanthemums = 0
single_price_roses = 0
single_price_tulips = 0
price_bouqette = 0
extra_discount = 0
discount = 0
total_bought_flowers = bought_roses + bought_chrysanthemums + bought_tulips

if season == 'Spring' or season == 'Summer':
    single_price_tulips = 2.50
    single_price_roses = 4.10
    single_price_chrysanthemums = 2.00
    if is_holiday == 'Y':
        single_price_tulips *= 1.15
        single_price_roses *= 1.15
        single_price_chrysanthemums *= 1.15
    if season == 'Spring':
        if bought_tulips > 7:
            discount = 0.05
    if total_bought_flowers > 20:
        extra_discount = 0.20
elif season == 'Autumn' or season == 'Winter':
    single_price_tulips = 4.15
    single_price_roses = 4.50
    single_price_chrysanthemums = 3.75
    if is_holiday == 'Y':
        single_price_tulips *= 1.15
        single_price_roses *= 1.15
        single_price_chrysanthemums *= 1.15
    if season == 'Winter':
        if bought_roses >= 10:
            discount = 0.10
    if total_bought_flowers > 20:
        extra_discount = 0.20


price_bouqette = (bought_chrysanthemums * single_price_chrysanthemums
                  + bought_tulips * single_price_tulips
                  + bought_roses * single_price_roses)

price_with_discounts_and_arrangement = price_bouqette * (1 - discount) * (1 - extra_discount) + 2

print(f'{price_with_discounts_and_arrangement:.2f}')
