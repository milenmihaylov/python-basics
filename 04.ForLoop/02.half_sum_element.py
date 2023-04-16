import sys

n = int(input())
sum_of_all_elements = 0
max_element = - sys.maxsize

for i in range(n):
    number = int(input())
    if number > max_element:
        max_element = number

    sum_of_all_elements += number

sum_of_all_elements = sum_of_all_elements - max_element
if sum_of_all_elements == max_element:
    print(f"Yes \nSum = {sum_of_all_elements}")
else:
    print(f"No \nDiff = {abs(sum_of_all_elements - max_element)}")
