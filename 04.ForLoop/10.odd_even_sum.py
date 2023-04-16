n = int(input())

odd_sum = 0
even_sum = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        even_number = int(input())
        even_sum += even_number
    else:
        odd_number = int(input())
        odd_sum += odd_number


if odd_sum == even_sum:
    print(f"Yes \nSum = {odd_sum}")
else:
    print(f"No \nDiff = {abs(odd_sum - even_sum)}")
