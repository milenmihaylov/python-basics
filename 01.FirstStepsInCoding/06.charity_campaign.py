total_days = int(input())
number_of_bakers = int(input())
cakes_per_baker = int(input())
waffles_per_baker = int(input())
pancakes_per_baker = int(input())

cake_price = 45
waffle_price = 5.8
pancake_price = 3.2

total_cakes = total_days * number_of_bakers * cakes_per_baker
total_waffles = total_days * number_of_bakers * waffles_per_baker
total_pancakes = total_days * number_of_bakers * pancakes_per_baker

total_sum = total_cakes * cake_price + total_waffles * waffle_price + total_pancakes * pancake_price

expenses = total_sum / 8

charity_sum = total_sum - expenses
print(charity_sum)
