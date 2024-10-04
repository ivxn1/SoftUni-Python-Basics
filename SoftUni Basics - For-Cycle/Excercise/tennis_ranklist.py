from math import floor
total_tournaments = int(input())
start_points = int(input())
gained_points = 0
count_wins = 0

for _ in range(total_tournaments):
    stage = input()
    if stage == 'W':
        gained_points += 2000
        count_wins += 1
    elif stage == 'F':
        gained_points += 1200
    elif stage == "SF":
        gained_points += 720

final_points = start_points + gained_points

average_points = gained_points / total_tournaments

wins_percent = count_wins / total_tournaments

print(f'Final points: {final_points}')
print(f'Average points: {floor(average_points)}')
print(f'{wins_percent:.2%}')
