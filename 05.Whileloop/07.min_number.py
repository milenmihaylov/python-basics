import sys
min_number = sys.maxsize

insert = input()
while insert != "Stop":
    insert = int(insert)
    if insert < min_number:
        min_number = insert
    insert = input()

print(min_number)
