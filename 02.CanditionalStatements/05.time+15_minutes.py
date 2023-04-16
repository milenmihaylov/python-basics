hours = int(input())
minutes = int(input())

# print the time after 15 minutes
if minutes < 45:
    print(f"{hours}:{minutes + 15}")
elif minutes < 55:
    if hours < 23:
        print(f"{hours + 1}:0{minutes - 45}")
    elif hours == 23:
        print(f"{hours + 1 - 24}:0{minutes - 45}")
elif minutes >= 55:
    if hours < 23:
        print(f"{hours + 1}:{minutes - 45}")
    elif hours == 23:
        print(f"{hours + 1 - 24}:{minutes - 45}")
