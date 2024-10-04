days_off = int(input())
days_at_work = 365 - days_off

normal_play_inmins_per_year = 30000
normal_play_hours_per_year = normal_play_inmins_per_year // 60
normal_play_mins_per_year = normal_play_inmins_per_year % 60

play_duration_work_days = days_at_work * 63
play_duration_days_off = 127 * days_off

total_duration_play_year_inminutes = play_duration_days_off + play_duration_work_days

total_duration_hours_play_thisyear = total_duration_play_year_inminutes // 60
total_duration_minutes_play_thisyear = total_duration_play_year_inminutes % 60

if total_duration_play_year_inminutes > normal_play_inmins_per_year:
    print('Tom will run away')
    print(f'{total_duration_hours_play_thisyear - normal_play_hours_per_year} hours'
          f' and {total_duration_minutes_play_thisyear - normal_play_mins_per_year} minutes'
          f' more for play')
else:
    print('Tom sleeps well')
    print(f'{normal_play_hours_per_year - total_duration_hours_play_thisyear} hours'
          f' and {normal_play_mins_per_year - total_duration_minutes_play_thisyear} minutes'
          f' less for play')
