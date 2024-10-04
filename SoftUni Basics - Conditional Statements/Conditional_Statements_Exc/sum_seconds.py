seconds_first = int(input())
seconds_second = int(input())
seconds_third = int(input())

seconds_sum = seconds_first + seconds_second + seconds_third

total_minutes = seconds_sum // 60
total_seconds = seconds_sum % 60

if total_seconds >= 10:
    print(f'{total_minutes}:{total_seconds}')
else:
    print(f'{total_minutes}:0{total_seconds}')

# print(f'{total_minutes}:{total_seconds:02d}')