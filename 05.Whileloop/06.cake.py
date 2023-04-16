cake_length = int(input())
cake_width = int(input())

cake_size = cake_width * cake_length

eating = True
while eating:
    pieces_number = input()
    if pieces_number == 'STOP':
        eating = False
    else:
        pieces_number = int(pieces_number)
        cake_size -= pieces_number

    if cake_size < 0:
        print(f"No more cake left! You need {abs(cake_size)} pieces more.")
        break
    elif not eating:
        print(f"{abs(cake_size)} pieces are left.")
