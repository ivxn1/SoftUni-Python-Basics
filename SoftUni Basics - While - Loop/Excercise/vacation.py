money_for_trip = float(input())
balance = float(input())
final_money = 0
day = 0
spending = 0

while balance < money_for_trip:

    action = input()
    day += 1
    if action == 'spend':
        spent_money = float(input())
        if spent_money > balance:
            balance = 0
            continue
        balance -= spent_money
        spending += 1
        if spending == 5:
            print(f'You can\'t save the money.\n{day}')

    elif action == 'save':
        saved_money = float(input())
        balance += saved_money
        spending = 0

else:
    print(f'You saved the money for {day} days.')
