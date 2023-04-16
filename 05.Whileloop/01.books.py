favorite_book = input()
checked_book = input()
checks = 0

while not checked_book == 'No More Books':
    if checked_book == favorite_book:
        print(f"You checked {checks} books and found it.")
        break
    else:
        checked_book = input()
        checks += 1
if checked_book == 'No More Books':
    print(f"The book you search is not here! \nYou checked {checks} books.")
