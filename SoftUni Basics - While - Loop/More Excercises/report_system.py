final_sum = int(input())
command = input()
paying = 0
cash_sold = 0
card_sold = 0
cash_payment = 0
card_payment = 0
collected_money = 0
is_money_enough = False
while command != 'End':
    item_price = int(command)
    paying += 1
    if paying % 2 != 0:     # cash
        if item_price > 100:
            print('Error in transaction!')
        else:
            print('Product sold!')
            cash_payment += 1
            cash_sold += item_price
            collected_money += item_price
            if collected_money >= final_sum:
                is_money_enough = True
                break
    elif paying % 2 == 0:
        if item_price < 10:
            print('Error in transaction!')
        else:
            print('Product sold!')
            card_payment += 1
            card_sold += item_price
            collected_money += item_price
            if collected_money >= final_sum:
                is_money_enough = True
                break
    command = input()

if command == 'End':
    print('Failed to collect required money for charity.')
elif is_money_enough:
    average_cash_pay = cash_sold / cash_payment
    average_card_pay = card_sold / card_payment
    print(f'Average CS: {average_cash_pay:.2f}')
    print(f'Average CC: {average_card_pay:.2f}')
