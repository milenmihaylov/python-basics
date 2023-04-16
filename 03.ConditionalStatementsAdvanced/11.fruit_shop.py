working_days_prices = {'banana': 2.5, 'apple': 1.2, 'orange': 0.85, 'grapefruit': 1.45,
                       'kiwi': 2.7, 'pineapple': 5.5, 'grapes': 3.85}
weekends_prices = {'banana': 2.7, 'apple': 1.25, 'orange': 0.9, 'grapefruit': 1.6,
                   'kiwi': 3, 'pineapple': 5.6, 'grapes': 4.2}

fruit = input()
day = input()
quantity = float(input())

if fruit == "banana" or fruit == "apple" or fruit == "kiwi" or fruit == "orange" or \
        fruit == "grapefruit" or fruit == "grapes" or fruit == 'pineapple':

    if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
        print(f"{working_days_prices[fruit] * quantity:.2f}")
    elif day == "Saturday" or day == "Sunday":
        print(f"{weekends_prices[fruit] * quantity:.2f}")
    else:
        print("error")
else:
    print('error')
