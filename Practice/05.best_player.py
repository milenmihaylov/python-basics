import sys

player = input()


best_player = ''
best_goals = - sys.maxsize
hat_trick = False

while not player == 'END':
    goals_scored = int(input())

    if goals_scored > best_goals:
        best_player = player
        best_goals = goals_scored
    if best_goals >= 3:
        hat_trick = True
    if goals_scored >= 10:
        break
    player = input()

print(f"{best_player} is the best player!")
if hat_trick:
    print(f"He has scored {best_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best_goals} goals.")
