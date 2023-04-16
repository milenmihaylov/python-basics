budget = float(input())
season = input()

accommodation = ''

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        accommodation = 'Camp'
        budget *= 0.3
    elif season == "winter":
        accommodation = 'Hotel'
        budget *= 0.7

elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        accommodation = 'Camp'
        budget *= 0.4
    elif season == "winter":
        budget *= 0.8
        accommodation = 'Hotel'
else:
    destination = "Europe"
    budget *= 0.9
    accommodation = 'Hotel'

print(f"Somewhere in {destination}")
print(f"{accommodation} - {budget:.2f}")
