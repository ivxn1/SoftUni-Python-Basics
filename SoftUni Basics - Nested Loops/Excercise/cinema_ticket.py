command = input()
total_standard = 0
total_student = 0
total_kid = 0
total_tickets = 0
while command != 'Finish':
    current_movie = command
    total_seats = int(input())
    ticket_type = input()
    taken_seats = 0
    while ticket_type != 'End':
        taken_seats += 1

        if ticket_type == 'standard':
            total_standard += 1
        elif ticket_type == 'student':
            total_student += 1
        elif ticket_type == 'kid':
            total_kid += 1

        if taken_seats == total_seats:
            break
        ticket_type = input()

    taken_seats_percent = taken_seats / total_seats * 100
    total_tickets += taken_seats
    print(f'{current_movie} - {taken_seats_percent:.2f}% full.')

    command = input()

standard_percent = total_standard / total_tickets
student_percent = total_student / total_tickets
kid_percent = total_kid / total_tickets
print(f'Total tickets: {total_tickets}')
print(f'{student_percent:.2%} student tickets.')
print(f'{standard_percent:.2%} standard tickets.')
print(f'{kid_percent:.2%} kids tickets.')
