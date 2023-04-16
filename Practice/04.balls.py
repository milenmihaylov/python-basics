n = int(input())

color_dict = {'red': 5, 'orange': 10, 'yellow': 15, 'white': 20}
score = 0

red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
black_balls = 0
other_balls = 0

for i in range(n):
    color = input()

    if color == 'red':
        red_balls += 1
    elif color == 'orange':
        orange_balls += 1
    elif color == 'yellow':
        yellow_balls += 1
    elif color == 'white':
        white_balls += 1
    elif color == 'black':
        black_balls += 1
    else:
        other_balls += 1

    if color == 'red' or color == 'orange' or color == 'yellow' or color == 'white':
        score += color_dict[color]
    elif color == 'black':
        score = int(score * 0.5)
    else:
        continue

print(f"Total points: {score}")
print(f"Points from red balls: {red_balls}")
print(f"Points from orange balls: {orange_balls}")
print(f"Points from yellow balls: {yellow_balls}")
print(f"Points from white balls: {white_balls}")
print(f"Other colors picked: {other_balls}")
print(f"Divides from black balls: {black_balls}")
