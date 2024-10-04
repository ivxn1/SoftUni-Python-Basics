start_score = int(input())
bonus_score = 0

if start_score <= 100:
    bonus_score = 5

elif start_score > 100:
    bonus_score = 0.2 * start_score

elif start_score > 1000:
    bonus_score = 0.1 * start_score


if start_score % 2 == 0:
    bonus_score = bonus_score + 1

elif start_score % 10 == 5:
    bonus_score = bonus_score + 2

print(bonus_score)
print(bonus_score + start_score)
