strawberries_price = float(input())
bananas_quantity = float(input())
oranges_quantity = float(input())
raspberries_quantity = float(input())
strawberries_quantity = float(input())

raspberries_price = strawberries_price * 0.5
oranges_price = raspberries_price * 0.6
bananas_price = raspberries_price * 0.2

sum_of_bananas = bananas_price * bananas_quantity
sum_of_oranges = oranges_price * oranges_quantity
sum_of_raspberries = raspberries_quantity * raspberries_price
sum_of_strawberries = strawberries_quantity * strawberries_price

total_sum = sum_of_strawberries + sum_of_raspberries + sum_of_bananas + sum_of_oranges
print(total_sum)
