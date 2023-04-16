# flower_price = {"roses": 5, 'dahlias': 3.8, 'tulips': 2.8, 'narcissus': 3, 'gladiolus': 2.5}

flower_type = input()
number_of_flowers = int(input())
budget = int(input())

flower_price = 0
discount = 0

if flower_type == "Roses":
    flower_price = 5
    if number_of_flowers > 80:
        discount = 0.1

elif flower_type == "Dahlias":
    flower_price = 3.8
    if number_of_flowers > 90:
        discount = 0.15

elif flower_type == "Tulips":
    flower_price = 2.8
    if number_of_flowers > 90:
        discount = 0.15

elif flower_type == "Narcissus":
    flower_price = 3
    if number_of_flowers < 120:
        discount = -0.15

elif flower_type == "Gladiolus":
    flower_price = 2.5
    if number_of_flowers < 80:
        discount = -0.2

total_cost = flower_price * number_of_flowers * (1 - discount)
money_left = budget - total_cost

if money_left >= 0:
    print(f"Hey, you have a great garden with {number_of_flowers} {flower_type} and {money_left:.2f} leva left.")
else:
    print(f"Not enough money, you need {abs(money_left):.2f} leva more.")
