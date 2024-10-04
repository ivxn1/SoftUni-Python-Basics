lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_sword_break = lost_fights // 3
total_helmet_break = lost_fights // 2
total_shield_break = lost_fights // 6
total_armor_break = total_shield_break // 2
expenses = total_sword_break * sword_price \
    + total_helmet_break * helmet_price \
    + total_shield_break * shield_price \
    + total_armor_break * armor_price

print(f'Gladiator expenses: {expenses:.2f} aureus')

#   or vvvv
# for fight in range(1, lost_fights + 1):
#     if fight % 3 == 0:
#         cost += sword_price
#     if fight % 2 == 0:
#         cost += helmet_price
#     if fight % 2 == 0 and fight % 3 == 0:
#         cost += shield_price
#         shield_break += 1
#         if shield_break % 2 == 0:
#             cost += armor_price
#
