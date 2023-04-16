f_number = int(input())
s_number = int(input())
magic_number = int(input())
i = 0
match = False

for x in range(f_number, s_number + 1):
    for y in range(f_number, s_number + 1):
        i += 1
        if x + y == magic_number:
            print(f"Combination N:{i} ({x} + {y} = {magic_number})")
            match = True
            break

    if match:
        break

if not match:
    print(f"{i} combinations - neither equals {magic_number}")
