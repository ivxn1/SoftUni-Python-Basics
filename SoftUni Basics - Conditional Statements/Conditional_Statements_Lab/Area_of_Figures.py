shape = input()
area = 0
if shape == 'square':
    a = float(input())
    area = a*a

elif shape == 'rectangle':
    a = float(input())
    b = float(input())
    area = a * b

elif shape == 'circle':
    from math import pi
    a = float(input())
    area = pi * (a ** 2)


elif shape == 'triangle':
    a = float(input())
    b = float(input())
    area = (a * b) / 2

print(f'{area: .3f}')

