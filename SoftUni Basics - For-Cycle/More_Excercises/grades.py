students_count = int(input())
total_grade = 0
grades_count = 0
top_students = 0
between_4_and_4_99 = 0
between_3_and_3_99 = 0
fail = 0
for _ in range(students_count):
    current_grade = float(input())
    total_grade += current_grade
    grades_count += 1
    if current_grade >= 5.00:
        top_students += 1
    elif 4.00 <= current_grade <= 4.99:
        between_4_and_4_99 += 1
    elif 3.00 <= current_grade <= 3.99:
        between_3_and_3_99 += 1
    else:
        fail += 1

top_percent = top_students / students_count
between_4_and_4_99_percent = between_4_and_4_99 / students_count
between_3_and_3_99_percent = between_3_and_3_99 / students_count
fail_percent = fail / students_count
avg_grade = total_grade / grades_count

print(f'Top students: {top_percent:.2%}')
print(f'Between 4.00 and 4.99: {between_4_and_4_99_percent:.2%}')
print(f'Between 3.00 and 3.99: {between_3_and_3_99_percent:.2%}')
print(f'Fail: {fail_percent:.2%}')
print(f'Average: {avg_grade:.2f}')
