town = input()
sales_volume = float(input())
commissions = 0
error_condition = False
if town == 'Sofia':
    if 0 <= sales_volume <= 500:
        commissions = 0.05 * sales_volume
    elif 500 < sales_volume <= 1000:
        commissions = 0.07 * sales_volume
    elif 1000 < sales_volume <= 10000:
        commissions = 0.08 * sales_volume
    elif sales_volume > 10000:
        commissions = 0.12 * sales_volume
    else:
        error_condition = True
elif town == 'Varna':
    if 0 <= sales_volume <= 500:
        commissions = 0.045 * sales_volume
    elif 500 < sales_volume <= 1000:
        commissions = 0.075 * sales_volume
    elif 1000 < sales_volume <= 10000:
        commissions = 0.1 * sales_volume
    elif sales_volume > 10000:
        commissions = 0.13 * sales_volume
    else:
        error_condition = True
elif town == 'Plovdiv':
    if 0 <= sales_volume <= 500:
        commissions = 0.055 * sales_volume
    elif 500 < sales_volume <= 1000:
        commissions = 0.08 * sales_volume
    elif 1000 < sales_volume <= 10000:
        commissions = 0.12 * sales_volume
    elif sales_volume > 10000:
        commissions = 0.145 * sales_volume
    else:
        error_condition = True
else:
    error_condition = True

if error_condition:
    print('error')
else:
    print(f'{commissions:.2f}')
