movie_budget = float(input())
number_of_extras = int(input())
price_clothing_extra = float(input())

if number_of_extras > 150:
    price_clothing_extra *= 0.9

decor = movie_budget * 0.1
expenses = decor + price_clothing_extra * number_of_extras
remaining_difference = movie_budget - expenses

if movie_budget >= expenses:
    print("Action!")
    print(f"Wingard starts filming with {remaining_difference:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {abs(remaining_difference):.2f} leva more.")
