from math import ceil
name_series = input()
episode_length = int(input())
break_length = int(input())

lunch_length = 1/8 * break_length
rest_length = 1/4 * break_length

time_for_episode = break_length - (lunch_length + rest_length)

if time_for_episode >= episode_length:
    print(f'You have enough time to watch {name_series} and left with {ceil(time_for_episode - episode_length)}'
          f' minutes free time.')
else:
    print(f'You don\'t have enough time to watch {name_series}, you need'
          f' {ceil(episode_length - time_for_episode)} more minutes.')
