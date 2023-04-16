goal = 10000
total_steps = 0

going_home = False
walking = True
while walking:
    steps = input()
    if steps == "Going home":
        steps = int(input())
        total_steps += steps
        going_home = True
        walking = False
    else:
        steps = int(steps)
        total_steps += steps

    over_the_goal = total_steps - goal
    if over_the_goal >= 0:
        print("Goal reached! Good job!")
        print(f"{over_the_goal} steps over the goal!")
        walking = False # break

    elif going_home:
        print(f"{abs(over_the_goal)} more steps to reach goal.")
        break
