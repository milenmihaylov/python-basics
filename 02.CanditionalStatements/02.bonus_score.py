startup_points = int(input())

if startup_points <= 100:
    bonus_points = 5
elif startup_points <= 1000:
    bonus_points = startup_points * 0.2
else:
    bonus_points = startup_points * 0.1

extra_bonus = 0
if startup_points % 2 == 0:
    extra_bonus = 1
elif startup_points % 5 == 0:
    extra_bonus = 2

total_bonus = bonus_points + extra_bonus
final_score = startup_points + bonus_points + extra_bonus

print(total_bonus)
print(final_score)
