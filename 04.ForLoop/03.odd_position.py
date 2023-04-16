import sys

n = int(input())

even_sum = 0
even_min = sys.maxsize
even_max = - sys.maxsize
odd_sum = 0
odd_min = sys.maxsize
odd_max = - sys.maxsize

for i in range(1, n + 1):
    number = float(input())
    if i % 2 == 0:
        even_sum += number
        if number > even_max:
            even_max = number
        if number < even_min:
            even_min = number

    else:
        odd_sum += number
        if number > odd_max:
            odd_max = number
        if number < odd_min:
            odd_min = number

what_to_print_odd_min = ''
what_to_print_odd_max = ''
what_to_print_even_max = ''
what_to_print_even_min = ''

if odd_min == sys.maxsize:
    what_to_print_odd_min = "No"
else:
    what_to_print_odd_min = f"{odd_min:.2f}"

if odd_max == - sys.maxsize:
    what_to_print_odd_max = 'No'
else:
    what_to_print_odd_max = f"{odd_max:.2f}"

if even_min == sys.maxsize:
    what_to_print_even_min = "No"
else:
    what_to_print_even_min = f"{even_min:.2f}"

if even_max == -sys.maxsize:
    what_to_print_even_max = 'No'
else:
    what_to_print_even_max = f'{even_max:.2f}'

print(f"OddSum={odd_sum:.2f},")
print(f"OddMin={what_to_print_odd_min},")
print(f"OddMax={what_to_print_odd_max},")
print(f"EvenSum={even_sum:.2f},")
print(f"EvenMin={what_to_print_even_min},")
print(f"EvenMax={what_to_print_even_max}")
