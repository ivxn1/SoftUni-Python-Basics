mackerel_price_kilo = float(input())
sprat_price_kilo = float(input())
palamud_kilo = float(input())
safrid_kilo = float(input())
shells_kilo = float(input())

palamud_price_kilo = mackerel_price_kilo * (1 + 0.6)
safrid_price_kilo = sprat_price_kilo * (1 + 0.8)
shells_price_kilo = 7.5

total_price_palamud = palamud_price_kilo * palamud_kilo
total_price_safrid = safrid_price_kilo * safrid_kilo
total_price_shells = shells_price_kilo * shells_kilo

final_price = total_price_shells + total_price_safrid + total_price_palamud
print(f'{final_price: .2f}')

