import math

figure = input()

if figure == "square":
    side = float(input())
    area = math.pow(side, 2)
    print(f"{area:.3f}")

elif figure == "rectangle":
    length = float(input())
    width = float(input())
    area = width * length
    print(f"{area:.3f}")

elif figure == "circle":
    radius = float(input())
    area = math.pi * math.pow(radius, 2)
    print(f"{area:.3f}")

elif figure == "triangle":
    side = float(input())
    height = float(input())
    area = (height * side) / 2
    print(f"{area:.3f}")

else:
    print("проблем")
