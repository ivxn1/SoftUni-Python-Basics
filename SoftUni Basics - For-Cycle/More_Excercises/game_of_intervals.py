turns_count = int(input())
score = 0
from_0_to_9 = 0
from_10_to_19 = 0
from_20_to_29 = 0
from_30_to_39 = 0
from_40_to_50 = 0
invalid = 0
for _ in range(turns_count):
    current_num = int(input())
    if 0 <= current_num <= 9:
        score += 0.20 * current_num
        from_0_to_9 += 1
    elif 10 <= current_num <= 19:
        score += 0.30 * current_num
        from_10_to_19 += 1
    elif 20 <= current_num <= 29:
        score += 0.40 * current_num
        from_20_to_29 += 1
    elif 30 <= current_num <= 39:
        score += 50
        from_30_to_39 += 1
    elif 40 <= current_num <= 50:
        score += 100
        from_40_to_50 += 1
    elif current_num < 0 or current_num > 50:
        score /= 2
        invalid += 1
from_0_to_9_percent = from_0_to_9 / turns_count
from_10_to_19_percent = from_10_to_19 / turns_count
from_20_to_29_percent = from_20_to_29 / turns_count
from_30_to_39_percent = from_30_to_39 / turns_count
from_40_to_50_percent = from_40_to_50 / turns_count
invalid_percent = invalid / turns_count

print(f'{score:.2f}')
print(f'From 0 to 9: {from_0_to_9_percent:.2%}')
print(f'From 10 to 19: {from_10_to_19_percent:.2%}')
print(f'From 20 to 29: {from_20_to_29_percent:.2%}')
print(f'From 30 to 39: {from_30_to_39_percent:.2%}')
print(f'From 40 to 50: {from_40_to_50_percent:.2%}')
print(f'Invalid numbers: {invalid_percent:.2%}')
