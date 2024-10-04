failure_count = int(input())
current_problem = input()
solved_counter = 0
total_grades = 0
failure_counter = 0
total_problems = 0
last_problem = ''

while current_problem != 'Enough':
    current_grade = float(input())
    total_grades += current_grade
    total_problems += 1
    last_problem = current_problem
    if current_grade <= 4:
        failure_counter += 1
        if failure_counter == failure_count:
            print('You need a break,', failure_counter, 'poor grades.')
            break
    current_problem = input()
else:
    average_score = total_grades / total_problems
    print(f'Average score: {average_score:.2f}')
    print(f'Number of problems: {total_problems}')
    print(f'Last problem: {last_problem}')
