from math import floor, ceil

ordered_magnolias = int(input())
ordered_zumbuli = int(input())
ordered_roses = int(input())
ordered_cacti = int(input())
price_gift = float(input())

magnolia_single = 3.25
zumbuli_single = 4
roses_single = 3.50
cacti_single = 8

price_for_magnolias = ordered_magnolias * magnolia_single
price_for_zumbuli = ordered_zumbuli * zumbuli_single
price_for_roses = roses_single * ordered_roses
price_for_cacti = cacti_single * ordered_cacti
total_price_bouqette = (price_for_cacti + price_for_roses
                        + price_for_zumbuli + price_for_magnolias)
tax = 0.05 * total_price_bouqette
money_gain_after_tax = total_price_bouqette - tax
if money_gain_after_tax >= price_gift:
    print(f'She is left with {floor(money_gain_after_tax - price_gift)} leva.')
else:
    print(f'She will have to borrow {ceil(price_gift - money_gain_after_tax)} leva.')
    