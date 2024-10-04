nylon = int(input())
paint = int(input())
razreditel = int(input())
work_hours = int(input())
price_paint = (paint + (0.1*paint)) * 14.5
price_razreditel = 5 * razreditel
price_total_nylon = (nylon + 2) * 1.5
bags = 0.4
total_price_materials = price_paint + price_total_nylon + price_razreditel + bags
work_per_hour = 0.3 * total_price_materials
total_price_for_everything = total_price_materials + (work_hours * work_per_hour)
print(total_price_for_everything)