budget = int(input())
season = input()
fishermen = int(input())

spring_ship = 3000
summer_ship = 4200
autumn_ship = 4200
winter_ship = 2600

ship_price = 0
if season == "Spring":
    ship_price = spring_ship
elif season == "Summer":
    ship_price = summer_ship
elif season == "Autumn":
    ship_price = autumn_ship
elif season == "Winter":
    ship_price = winter_ship

discount = 0
if fishermen <= 6:
    discount = 0.1
elif fishermen <= 11:
    discount = 0.15
else:
    discount = 0.25

add_discount = 0
if season != "Autumn" and fishermen % 2 == 0:
    add_discount = 0.05

costs_w_discount = ship_price * (1 - discount)
final_costs = costs_w_discount * (1 - add_discount)
money_left = budget - final_costs

if budget >= final_costs:
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(money_left):.2f} leva.")
