product = input()
town = input()
count = float(input())
product_single_price = 0

if town == 'Sofia':
    if product == 'coffee':
        product_single_price = 0.50
    if product == 'water':
        product_single_price = 0.80
    if product == 'beer':
        product_single_price = 1.20
    if product == 'sweets':
        product_single_price = 1.45
    if product == 'peanuts':
        product_single_price = 1.60
elif town == 'Plovdiv':
    if product == 'coffee':
        product_single_price = 0.40
    if product == 'water':
        product_single_price = 0.70
    if product == 'beer':
        product_single_price = 1.15
    if product == 'sweets':
        product_single_price = 1.30
    if product == 'peanuts':
        product_single_price = 1.50
elif town == 'Varna':
    if product == 'coffee':
        product_single_price = 0.45
    if product == 'water':
        product_single_price = 0.70
    if product == 'beer':
        product_single_price = 1.10
    if product == 'sweets':
        product_single_price = 1.35
    if product == 'peanuts':
        product_single_price = 1.55

final_price = product_single_price * count
print(final_price)
