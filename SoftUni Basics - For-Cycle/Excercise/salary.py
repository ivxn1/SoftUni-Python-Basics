open_tabs = int(input())
salary = float(input())

fine = 0

for tabs in range(open_tabs):
    site = input()
    if site == 'Facebook':
        fine += 150
    elif site == 'Instagram':
        fine += 100
    elif site == "Reddit":
        fine += 50

salary_remainder = salary - fine

if salary_remainder <= 0:
    print('You have lost your salary.')
else:
    print(f'{round(salary_remainder)}')
