degrees = float(input())

if 26 <= degrees <= 35:
    print('Hot')
elif 20.1 <= degrees <= 25.9:
    print('Warm')
elif 15.00 <= degrees <= 20:
    print('Mild')
elif 12.00 <= degrees <= 14.9:
    print('Cool')
elif 5.00 <= degrees <= 11.9:
    print('Cold')
else:
    print('unknown')
