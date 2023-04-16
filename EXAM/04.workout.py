from math import ceil

running_days = int(input())
first_run = float(input())
goal_km = 1000

percentage_increase = 0
mileage = first_run
current_run = first_run
for day in range(running_days):
    percentage_increase = int(input())
    current_run *= (1 + (percentage_increase * 0.01))
    mileage += current_run

km_difference = mileage - goal_km

if mileage >= goal_km:
    print(f"You've done a great job running"
          f" {ceil(km_difference)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run"
          f" {ceil(abs(km_difference))} more kilometers")
