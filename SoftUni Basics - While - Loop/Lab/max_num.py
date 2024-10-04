import sys
max_num = -sys.maxsize

while True:
    text = input()
    if text == 'Stop':
        break
    current_num = int(text)
    if current_num > max_num:
        max_num = current_num

print(max_num)
