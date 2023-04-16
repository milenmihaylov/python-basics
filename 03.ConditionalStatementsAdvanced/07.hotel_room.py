month = input()
overnights = int(input())

studio_price = 0
apartment_price = 0
studio_discount = 0
apartment_discount = 0

if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65
    if overnights > 14:
        studio_discount = 0.3
        apartment_discount = 0.1
    elif overnights > 7:
        studio_discount = 0.05

elif month == "June" or month == "September":
    studio_price = 75.2
    apartment_price = 68.70
    if overnights > 14:
        studio_discount = 0.2
        apartment_discount = 0.1

elif month == "July" or month == "August":
    studio_price = 76
    apartment_price = 77
    if overnights > 14:
        apartment_discount = 0.1

apartment_costs = overnights * apartment_price * (1 - apartment_discount)
studio_costs = overnights * studio_price * (1 - studio_discount)

print(f"Apartment: {apartment_costs:.2f} lv.")
print(f"Studio: {studio_costs:.2f} lv.")
