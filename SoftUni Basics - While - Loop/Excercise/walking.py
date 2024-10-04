target = 10000
total_steps = 0
while True:
    text = input()
    if text != 'Going home':
        current_steps = int(text)
        total_steps += current_steps
    elif text == 'Going home':
        steps_home = int(input())
        total_steps += steps_home
        if total_steps < target:
            needed_steps = target - total_steps
            print(f'{needed_steps} more steps to reach goal.')

    if total_steps >= target:
        difference = total_steps - target
        print(f'Goal reached! Good job!\n{difference} steps over the goal!')
        break
