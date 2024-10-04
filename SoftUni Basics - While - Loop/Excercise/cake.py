cake_length = int(input())
cake_width = int(input())
total_pieces = cake_length * cake_width
command = input()
eaten_pieces = 0

while command != 'STOP':
    current_pieces = int(command)
    total_pieces -= current_pieces

    if total_pieces < eaten_pieces:
        print(f'No more cake left! You need {-total_pieces} pieces more.')
        break

    command = input()

if command == 'STOP':
    print(f"{total_pieces} pieces are left.")
