the_integer = int(input())

is_special = False

for number in range (1111,10000):
    special_number = str(number)
    for digit in special_number:
        digit = int(digit)
        if digit == 0:
            is_special = False
            break
        elif the_integer % digit == 0:
            is_special = True
        else:
            is_special = False
            break

    if is_special:
        print(special_number, end=' ')
