number = float(input())
input_unit = input()
output_unit = input()

# m = 1
# cm = m * 100
# mm = cm * 10

if input_unit == "mm":
    if output_unit == 'cm':
        print(f"{number * 0.1:.3f}")
    elif output_unit == "m":
        print(f"{number * 0.1 * 0.01:.3f}")
    else:
        print(f"{number:.3f}")
elif input_unit == "cm":
    if output_unit == 'mm':
        print(f"{number * 10:.3f}")
    elif output_unit == "m":
        print(f"{number * 0.01:.3f}")
    else:
        print(f"{number:.3f}")
elif input_unit == "m":
    if output_unit == 'mm':
        print(f"{number * 100 * 10:.3f}")
    elif output_unit == "cm":
        print(f"{number * 100:.3f}")
    else:
        print(f"{number:.3f}")
