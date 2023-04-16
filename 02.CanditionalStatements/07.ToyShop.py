# Prices of the toys in lv:
puzzle_price = 2.6
talking_doll_price = 3
teddy_brear_price = 4.1
minion_price = 8.2
truck_price = 2

# If 50 ot more toys are ordered, the store makes a 25% discount on the total price
# 10% from profit goes for rent
# Calculate whether the money will be enough for a trip

trip_price = float(input())

puzzle_numbers = int(input())
talking_doll_numbers = int(input())
teddy_brear_numbers = int(input())
minion_numbers = int(input())
truck_numbers = int(input())

total_numbers = puzzle_numbers + talking_doll_numbers + teddy_brear_numbers + minion_numbers + truck_numbers

total_puzzles = puzzle_numbers * puzzle_price
total_dolls = talking_doll_numbers * talking_doll_price
total_bears = teddy_brear_numbers * teddy_brear_price
total_minions = minion_numbers * minion_price
total_trucks = truck_numbers * truck_price

total_price = total_puzzles + total_dolls + + total_bears + total_minions + total_trucks

discount = 0.25
if total_numbers >= 50:
    total_price = total_price * (1 - discount)

rent = 0.1 * total_price

profit = total_price - rent

if profit >= trip_price:
    print(f"Yes! {profit - trip_price:.2f} lv left.")
else:
    print(f"Not enough money! {trip_price - profit:.2f} lv needed.")
