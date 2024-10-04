budget = float(input())
type_tickets = input()
people_count = int(input())

total_ticket_price = 0
transport_fee = 0
price_per_ticket = 0

if 1 <= people_count <= 4:
    transport_fee = 0.75 * budget
elif 5 <= people_count <= 9:
    transport_fee = 0.60 * budget
elif 10 <= people_count <= 24:
    transport_fee = 0.50 * budget
elif 25 <= people_count <= 49:
    transport_fee = 0.40 * budget
elif people_count >= 50:
    transport_fee = 0.25 * budget

money_left_for_tickets = budget - transport_fee

if type_tickets == 'VIP':
    price_per_ticket = 499.99
    total_ticket_price = price_per_ticket * people_count
    if money_left_for_tickets >= total_ticket_price:
        money_left = money_left_for_tickets - total_ticket_price
        print(f'Yes! You have {money_left:.2f} leva left.')
    else:
        money_needed = total_ticket_price - money_left_for_tickets
        print(f'Not enough money! You need {money_needed:.2f} leva.')
elif type_tickets == "Normal":
    price_per_ticket = 249.99
    total_ticket_price = price_per_ticket * people_count
    if money_left_for_tickets >= total_ticket_price:
        money_left = money_left_for_tickets - total_ticket_price
        print(f'Yes! You have {money_left:.2f} leva left.')
    else:
        money_needed = total_ticket_price - money_left_for_tickets
        print(f'Not enough money! You need {money_needed:.2f} leva.')
