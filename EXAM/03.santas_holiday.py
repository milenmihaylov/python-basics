room_for_one_person = 18
apartment = 25
president_apartment = 35

days = int(input())
accommodation = input()
review = input()

overnights = days - 1
costs = 0
discount = 0
total_cost = 0

if accommodation == "room for one person":
    costs = overnights * room_for_one_person
    discount = 0

elif accommodation == 'apartment':
    costs = overnights * apartment
    if days < 10:
        discount = 0.3
    elif days <= 15:
        discount = 0.35
    else:
        discount = 0.5
    costs *= (1 - discount)

elif accommodation == 'president apartment':
    costs = overnights * president_apartment
    if days < 10:
        discount = 0.1
    elif days <= 15:
        discount = 0.15
    else:
        discount = 0.2
    costs *= (1 - discount)

if review == 'positive':
    total_cost = costs * 1.25
elif review == 'negative':
    total_cost = costs * 0.9

print(f"{total_cost:.2f}")
