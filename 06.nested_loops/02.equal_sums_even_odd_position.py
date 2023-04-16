first_number = int(input())
second_number = int(input())

for number in range(first_number, second_number + 1):
    even_sum = 0
    odd_sum = 0
    number = str(number)
    for index, digit in enumerate(number):
        digit = int(digit)
        if index % 2 == 0:
            odd_sum += digit
        else:
            even_sum += digit

    if even_sum == odd_sum:
        print(number, end=' ')
