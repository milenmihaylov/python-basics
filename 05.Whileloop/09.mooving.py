width_space = int(input())
length_space = int(input())
height_space = int(input())

space = width_space * length_space * height_space

boxes = input()
while not boxes == 'Done':
    boxes = int(boxes)
    space -= boxes
    if space > 0:
        boxes = input()
        continue
    else:
        print(f"No more free space! You need {abs(space)} Cubic meters more.")
        break

if boxes == 'Done':
    print(f"{space} Cubic meters left.")
