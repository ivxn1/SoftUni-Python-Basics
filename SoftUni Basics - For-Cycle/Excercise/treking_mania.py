group_count = int(input())
m1 = 0
m2 = 0
m3 = 0
m4 = 0
m5 = 0
total_people = 0

for _ in range(group_count):
    people_in_group = int(input())
    total_people += people_in_group
    if people_in_group <= 5:
        m1 += people_in_group
    elif 6 <= people_in_group <= 12:
        m2 += people_in_group
    elif 13 <= people_in_group <= 25:
        m3 += people_in_group
    elif 26 <= people_in_group <= 40:
        m4 += people_in_group
    elif people_in_group >= 41:
        m5 += people_in_group

m1_percent = m1 / total_people
m2_percent = m2 / total_people
m3_percent = m3 / total_people
m4_percent = m4 / total_people
m5_percent = m5 / total_people

print(f'{m1_percent:.2%}')
print(f'{m2_percent:.2%}')
print(f'{m3_percent:.2%}')
print(f'{m4_percent:.2%}')
print(f'{m5_percent:.2%}')
