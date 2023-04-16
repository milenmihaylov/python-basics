number_of_windows = int(input())
windows_size = input()
delivery_method = input()

windows_price = 0
if windows_size == '90X130':
    windows_price = 110
    if number_of_windows > 60:
        windows_price *= (1 - 0.08)
    elif number_of_windows > 30:
        windows_price *= (1 - 0.05)

elif windows_size == '100X150':
    windows_price = 140
    if number_of_windows > 80:
        windows_price *= (1 - 0.1)
    elif number_of_windows > 40:
        windows_price *= (1-0.06)

elif windows_size == '130X180':
    windows_price = 190
    if number_of_windows > 50:
        windows_price *= (1-0.12)
    elif number_of_windows > 20:
        windows_price *= (1-0.07)

elif windows_size == '200X300':
    windows_price = 250
    if number_of_windows > 50:
        windows_price *= (1-0.14)
    elif number_of_windows > 25:
        windows_price *= (1-0.09)


delivery_price = 0
if delivery_method == "With delivery":
    delivery_price = 60


total_cost = number_of_windows * windows_price + delivery_price

if number_of_windows > 99:
    total_cost *= (1 - 0.04)


if number_of_windows < 10:
    print("Invalid order")
else:
    print(f"{total_cost:.2f} BGN")


