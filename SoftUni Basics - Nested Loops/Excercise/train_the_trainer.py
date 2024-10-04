judges_count = int(input())
command = input()
all_grades = 0
grades_count = 0
while command != 'Finish':
    total_grades = 0
    presentation = command
    for _ in range(judges_count):
        current_grade = float(input())
        total_grades += current_grade
        all_grades += current_grade
        grades_count += 1
    average_grade = total_grades / judges_count
    print(f'{presentation} - {average_grade:.2f}.')
    command = input()

total_average_grade = all_grades / grades_count
print(f'Student\'s final assessment is {total_average_grade:.2f}.')
