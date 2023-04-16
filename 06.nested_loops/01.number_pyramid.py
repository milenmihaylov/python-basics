final_number = int(input())
y = 0
counter = 1

while counter <= final_number:
    y += 1
    for x in range(y):
        print(counter, end=' ')
        counter += 1
        if counter > final_number:
            break
    print()
