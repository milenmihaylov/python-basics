room_for_one_person = 18
apartment = 25
president_apartment = 35

days = int(input())
accommodation = input()
review = input()

overnights = days - 1
discount = 1
review_discount = 1

if accommodation == "room for one person":
    accommodation = room_for_one_person
    discount = 0
elif accommodation == "apartment":
    accommodation = apartment
    if days < 10:
        discount = 0.3
    elif 10 <= days <= 15:
        discount = 0.35
    elif days > 15:
        discount = 0.5
elif accommodation == "president apartment":
    accommodation = president_apartment
    if days < 10:
        discount = 0.1
    elif 10 <= days <= 15:
        discount = 0.15
    elif days > 15:
        discount = 0.2

if review == "positive":
    review_discount = 1.25
elif review == "negative":
    review_discount = 0.9

holiday_costs = overnights * accommodation * (1 - discount) * review_discount
print(f"{holiday_costs:.2f}")
