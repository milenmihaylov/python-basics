from math import ceil

days = int(input())
food_left = int(input())
first_deer_food_per_day = float(input())
second_deer_food_per_day = float(input())
third_deer_food_per_day = float(input())
enough_food = True

total_food_needed = days * (first_deer_food_per_day + second_deer_food_per_day + third_deer_food_per_day)
kilos_left = food_left - total_food_needed

if food_left >= total_food_needed:
    enough_food = True
else:
    enough_food = False

if enough_food:
    print(f"{int(kilos_left)} kilos of food left.")
else:
    print(f"{ceil(abs(kilos_left))} more kilos of food are needed.")
