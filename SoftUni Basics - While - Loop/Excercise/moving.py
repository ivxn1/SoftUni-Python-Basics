width = int(input())
length = int(input())
height = int(input())
total_boxes_capacity = width * length * height
command = input()
while command != 'Done':
    current_boxes = int(command)
    total_boxes_capacity -= current_boxes
    if total_boxes_capacity < current_boxes:
        print(f'No more free space! You need {-total_boxes_capacity} Cubic meters more.')
        break
    command = input()

if command == 'Done':
    print(f'{total_boxes_capacity} Cubic meters left.')
