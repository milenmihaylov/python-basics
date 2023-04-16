import sys
max_number = - sys.maxsize

insert = input()
while insert != "Stop":
    insert = int(insert)
    if insert > max_number:
        max_number = insert
    insert = input()

print(max_number)
