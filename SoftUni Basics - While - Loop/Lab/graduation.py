student_name = input()
failed_year = 0
successful_year = 0
total_grade = 0

while True:
    current_grade = float(input())
    if current_grade < 4:
        failed_year += 1
        if failed_year > 1:
            print(f'{student_name} has been excluded at {successful_year + 1} grade')
        else:
            continue
    else:
        total_grade += current_grade
        successful_year += 1
        if successful_year == 12:
            average_grade = total_grade / 12
            print(f'{student_name} graduated. Average grade: {average_grade:.2f}')
