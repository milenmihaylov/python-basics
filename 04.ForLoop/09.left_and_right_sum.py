n = int(input())

first_sum = 0
second_sum = 0

for i in range(1, n + 1):
    number = int(input())
    first_sum += number

for i in range(1, n + 1):
    number = int(input())
    second_sum += number

if first_sum == second_sum:
    print(f"Yes, sum = {first_sum}")
else:
    print(f"No, diff = {abs(first_sum - second_sum)}")
