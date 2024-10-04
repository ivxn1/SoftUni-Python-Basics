balls_count = int(input())
max_weight = 0
max_time = 0
max_quality = 0
max_score = 0
for ball in range(1, balls_count + 1):
    weight = int(input())
    time_to_reach = int(input())
    quality = int(input())
    score = (weight / time_to_reach) ** quality
    if score > max_score:
        max_score = score
        max_weight = weight
        max_time = time_to_reach
        max_quality = quality

print(f'{max_weight} : {max_time} = {max_score} ({max_quality})')
