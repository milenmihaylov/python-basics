change = float(input())

coins_list = [2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
total_coins = 0
integer_dev = 0

for i in range(len(coins_list)):
    integer_dev = int(change // coins_list[i])
    if integer_dev > 0:
        change -= coins_list[i] * integer_dev
        change = round(change, 2)
        total_coins += integer_dev

print(int(total_coins))
