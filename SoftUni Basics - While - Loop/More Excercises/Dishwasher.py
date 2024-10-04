bottles_count = int(input())
detergent = 750 * bottles_count
command = input()
washing_count = 0
washed_dishes = 0
washed_pots = 0
is_detergent_out = False
while command != 'End':
    things_count = int(command)
    washing_count += 1
    if washing_count % 3 == 0:
        needed_detergent = things_count * 15
        washed_pots += things_count
        detergent -= needed_detergent
        if detergent <= 0:
            is_detergent_out = True
            break
    elif washing_count % 10 != 3:
        needed_detergent = things_count * 5
        washed_dishes += things_count
        detergent -= needed_detergent
        if detergent <= 0:
            is_detergent_out = True
            break
    command = input()

if command == 'End':
    print('Detergent was enough!')
    print(f'{washed_dishes} dishes and {washed_pots} pots were washed.')
    print(f'Leftover detergent {detergent} ml.')
elif is_detergent_out:
    print(f'Not enough detergent, {abs(detergent)} ml. more necessary!')
