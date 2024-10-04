import sys
min_num = sys.maxsize

while True:
    text = input()
    if text == 'Stop':
        break
    current_num = int(text)
    if current_num < min_num:
        min_num = current_num

print(min_num)
