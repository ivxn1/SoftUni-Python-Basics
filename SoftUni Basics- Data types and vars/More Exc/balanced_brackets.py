lines = int(input())
last_string = ''
is_it_unbalanced = False
for line in range(lines):
    string = input()
    if string not in ['(', ')']:
        continue

    if last_string == '' and string == ')' or string == last_string:
        is_it_unbalanced = True
        break

    last_string = string

if is_it_unbalanced:
    print('UNBALANCED')
else:
    print('BALANCED')
