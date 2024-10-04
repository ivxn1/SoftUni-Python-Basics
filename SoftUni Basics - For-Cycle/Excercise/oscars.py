name_actor = input()
academy_points = float(input())
jury_count = int(input())
final_points = academy_points

for _ in range(jury_count):
    jury_name = input()
    jury_points = float(input())
    total_jury_points = (len(jury_name) * jury_points) / 2
    final_points += total_jury_points
    if final_points > 1250.5:
        break

if final_points > 1250.5:
    print(f'Congratulations, {name_actor} got a nominee for leading role with {final_points:.1f}!')
else:
    needed_points = 1250.5 - final_points
    print(f'Sorry, {name_actor} you need {needed_points:.1f} more!')
