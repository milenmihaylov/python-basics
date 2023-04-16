premiere = 12
normal = 7.5
discount = 5

film_type = input()
rows = int(input())
columns = int(input())

total_places = rows * columns
ticket_price = 0

if film_type == "Premiere":
    ticket_price = premiere
elif film_type == "Normal":
    ticket_price = normal
elif film_type == 'Discount':
    ticket_price = discount

revenue = total_places * ticket_price
print(f"{revenue:.2f}")
