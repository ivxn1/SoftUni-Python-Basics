pens = int(input())
markers = int(input())
litres_spray = int(input())
discount = int(input())
total_pens = pens * 5.8
total_markers = markers * 7.2
total_spray = litres_spray * 1.2
total_sum = total_spray + total_pens + total_markers
final_price = total_sum * (1 - discount / 100)
print(final_price)