vacation_cost = float(input())
money_on_hand = float(input())
days_saving = 0
spending_days = 5

saving = True
while saving:
    transaction = input()
    amount = float(input())
    days_saving += 1
    if transaction == 'save':
        money_on_hand += amount
        spending_days = 5
    elif transaction == 'spend':
        spending_days -= 1
        if money_on_hand >= amount:
            money_on_hand -= amount
        else:
            money_on_hand = 0

    if money_on_hand >= vacation_cost:
        print(f"You saved the money for {days_saving} days.")
        break

    if spending_days == 0:
        print(f"You can't save the money.")
        print(f"{days_saving}")
        break
