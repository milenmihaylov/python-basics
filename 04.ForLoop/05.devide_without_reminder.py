n = int(input())

total = 0
p1 = 0
p2 = 0
p3 = 0

for i in range(n):
    number = int(input())
    total += 1
    if number % 2 == 0:
        p1 += 1
    if number % 3 == 0:
        p2 += 1
    if number % 4 == 0:
        p3 += 1

p1 = p1 / total * 100
p2 = p2 / total * 100
p3 = p3 / total * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
