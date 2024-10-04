number_one = int(input())
number_two = int(input())
math_operator = input()
result = 0

if math_operator == '+':
    result = number_one + number_two
    if result % 2 == 0:
        even_or_odd = 'even'
        print(f'{number_one} + {number_two} = {result} - {even_or_odd}')
    else:
        even_or_odd = 'odd'
        print(f'{number_one} + {number_two} = {result} - {even_or_odd}')

elif math_operator == '-':
    result = number_one - number_two
    if result % 2 == 0:
        even_or_odd = 'even'
        print(f'{number_one} - {number_two} = {result} - {even_or_odd}')
    else:
        even_or_odd = 'odd'
        print(f'{number_one} - {number_two} = {result} - {even_or_odd}')

elif math_operator == '*':
    result = number_one * number_two
    if result % 2 == 0:
        even_or_odd = 'even'
        print(f'{number_one} * {number_two} = {result} - {even_or_odd}')
    else:
        even_or_odd = 'odd'
        print(f'{number_one} * {number_two} = {result} - {even_or_odd}')
elif math_operator == '/':
    if number_two == 0:
        print(f'Cannot divide {number_one} by zero')
    else:
        result = number_one / number_two
        print(f'{number_one} / {number_two} = {result:.2f}')
elif math_operator == '%':
    if number_two == 0:
        print(f'Cannot divide {number_one} by zero')
    else:
        result = number_one % number_two
        print(f'{number_one} % {number_two} = {result}')
