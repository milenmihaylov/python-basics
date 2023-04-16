n = int(input())

sum_a_b_c_d = 0
product = 0
n_eq = 0
number = 0
found = False
for a in range(1, 10):
    if found:
        break
    for b in range(9, a - 1, -1):
        if found:
            break
        for c in range(10):
            if found:
                break
            for d in range(9, c - 1, -1):
                sum_a_b_c_d = a + b + c + d
                product = a * b * c * d
                n_eq = n % 10
                if n_eq % 5 == 0 and sum_a_b_c_d == product and n != 0 and n_eq != 0:
                    number = a * 1000 + b * 100 + c * 10 + d
                    found = True
                    break
                elif int(product / sum_a_b_c_d) == 3 and n % 3 == 0:
                    number = d * 1000 + c * 100 + b * 10 + a
                    found = True
                    break

if found:
    print(number)
else:
    print("Nothing found")
