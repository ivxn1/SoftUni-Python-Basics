examHour = int(input())
examMinute = int(input())
studentHour = int(input())
studentMinute = int(input())

exam_time = examHour * 60 + examMinute
student_time = studentMinute + studentHour * 60

difference = exam_time - student_time

minutes_difference = abs(difference) % 60
hours_difference = abs(difference) // 60

if 0 <= difference <= 30:
    print('On time')
    if difference != 0:
        print(f'{minutes_difference} minutes before the start')
elif 30 < difference < 60:
    print(f'Early\n{minutes_difference} minutes before the start')
elif difference >= 60:
    print(f'Early\n{hours_difference}:{minutes_difference:02d} hours before the start')
elif student_time > exam_time:
    print('Late')
    if hours_difference == 0:
        print(f'{minutes_difference} minutes after the start')
    else:
        print(f'{hours_difference}:{minutes_difference:02d} hours after the start')
