money_in_account = 0

while True:
    text = input()
    if text == 'NoMoreMoney':
        break
    deposit = float(text)
    if deposit > 0:
        money_in_account += deposit
        print(f'Increase: {float(deposit):.2f}')
    else:
        print('Invalid operation!')
        break

print(f'Total: {money_in_account:.2f}')
