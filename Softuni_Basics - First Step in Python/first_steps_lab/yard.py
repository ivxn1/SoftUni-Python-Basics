square_meters = float(input())
total_price = square_meters * 7.61
discount = 0.18 * total_price
final_price = total_price - discount
print(f' The final price is: {final_price} lv.')
print(f' The discount is: {discount} lv.')