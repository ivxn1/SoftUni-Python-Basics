x1_rectangle = float(input())
y1_rectangle = float(input())
x2_rectangle = float(input())
y2_rectangle = float(input())
x_random = float(input())
y_random = float(input())

# border:

if x_random == x1_rectangle or x_random == x2_rectangle:
    if y1_rectangle <= y_random <= y2_rectangle:
        print('Border')
    else:
        print('Inside / Outside')
elif x1_rectangle < x_random < x2_rectangle:
    if y_random == y1_rectangle or y_random == y2_rectangle:
        print('Border')
    elif y1_rectangle < y_random < y2_rectangle:
        print('Inside / Outside')
    else:
        print('Inside / Outside')
else:
    print('Inside / Outside')
