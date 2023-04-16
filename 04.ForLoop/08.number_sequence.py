number_list = []
total_numbers = int(input())

for i in range(1, total_numbers + 1):
    number = int(input())
    number_list.append(number)

print(f"Max number: {max(number_list)}")
print(f"Min number: {min(number_list)}")
