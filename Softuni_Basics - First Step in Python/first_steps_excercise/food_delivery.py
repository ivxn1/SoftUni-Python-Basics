chicken = int(input())
fish = int(input())
vegetarian = int(input())
price_chicken = 10.35 * chicken
price_fish = 12.4 * fish
price_vegetarian = 8.15 * vegetarian
total_price_no_delivery = price_fish + price_vegetarian + price_chicken
dessert = 0.2 * total_price_no_delivery
total_price_dessert_delivery = total_price_no_delivery + dessert + 2.5
print(total_price_dessert_delivery)