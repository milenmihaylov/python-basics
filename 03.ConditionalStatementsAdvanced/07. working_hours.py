hour = int(input())
day = input()
''' Вариант с for цикъл 
working_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

if 10 <= hour <= 18:
    for i in working_days:
        if day == i:
            print("open")
            break
        if day == "Sunday":
            print("closed")
            break
else:
    print("closed")
'''
if 10 <= hour <= 18:
    if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday"  or day == "Saturday":
        print("open")
    else:print("closed")
else:
    print("closed")
