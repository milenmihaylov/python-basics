price_over_20kg = float(input())
bag_weight = float(input())
days_to_trip = int(input())
number_of_bags = int(input())

bag_price = 0

if bag_weight < 10:
    bag_price = price_over_20kg * 0.2
elif bag_weight <= 20:
    bag_price = price_over_20kg * 0.5
else:
    bag_price = price_over_20kg

if days_to_trip > 30:
    bag_price *= 1.1
elif days_to_trip >= 7:
    bag_price *= 1.15
else:
    bag_price *= 1.4

total_cost = number_of_bags * bag_price

print(f"The total price of bags is: {total_cost:.2f} lv. ")
