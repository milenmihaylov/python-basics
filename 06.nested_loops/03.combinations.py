n = int(input())
i = 0

for x in range(n + 1):
    # n -= x
    for y in range(n + 1):
        # n -= y
        for z in range(n + 1):
            if x + y + z == n:
                i += 1

print(i)
