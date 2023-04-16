lily_age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

gift_savings = 0
toy_number = 0
money_gift = 0
brother_money = 0

for year in range(1, lily_age + 1):

    if year % 2 == 0:
        money_gift += 10
        brother_money += 1
        gift_savings += money_gift
    else:
        toy_number += 1

toy_money = toy_number * toy_price
total_savings = gift_savings + toy_money - brother_money
money_left = total_savings - washing_machine_price

if total_savings >= washing_machine_price:
    print(f"Yes! {money_left:.2f}")
else:
    print(f"No! {abs(money_left):.2f}")
