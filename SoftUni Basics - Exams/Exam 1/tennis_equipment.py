from math import floor
from math import ceil

tennis_racket_price = float(input())
rackets_count = int(input())
shoes_count = int(input())

total_price = (rackets_count * tennis_racket_price + (1/6 * tennis_racket_price * shoes_count)) * 1.2
djokovic_price = 1/8 * total_price
sponsors = 7/8 * total_price

print(f'Price to be paid by Djokovic {floor(djokovic_price)}')
print(f'Price to be paid by sponsors {ceil(sponsors)}')
