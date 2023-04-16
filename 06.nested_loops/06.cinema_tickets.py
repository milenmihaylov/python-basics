movie_title = input()

available_seats = 0
total_tickets = 0
movie_tickets = 0
standard_tickets = 0
student_tickets = 0
kids_tickets = 0

while movie_title != "Finish":
    available_seats = int(input())
    ticket_type = input()
    movie_tickets = 0
    while ticket_type != 'End' and ticket_type != 'Finish':
        total_tickets += 1
        movie_tickets += 1
        if ticket_type == 'standard':
            standard_tickets += 1
        elif ticket_type == 'student':
            student_tickets += 1
        elif ticket_type == 'kid':
            kids_tickets += 1

        if movie_tickets == available_seats:
            break

        ticket_type = input()

    capacity = (movie_tickets / available_seats) * 100
    print(f"{movie_title} - {capacity:.2f}% full.")
    if ticket_type == 'Finish':
        break
    else:
        movie_title = input()


standard_tickets /= total_tickets
student_tickets /= total_tickets
kids_tickets /= total_tickets

print(f"Total tickets: {total_tickets}")
print(f"{student_tickets * 100:.2f}% student tickets.")
print(f"{standard_tickets * 100:.2f}% standard tickets.")
print(f"{kids_tickets * 100:.2f}% kids tickets.")
