all_floors = int(input())
rooms = int(input())

for floor in range(all_floors, 0, -1):
    for room in range(rooms):

        if floor == all_floors:
            print(f"L{floor}{room}", end=' ')
        elif floor % 2 == 0:
            print(f"O{floor}{room}", end=' ')
        else:
            print(f"A{floor}{room}", end=' ')
    print()
