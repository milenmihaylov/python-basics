destination = input()

while destination != "End":
    travel_costs = float(input())
    budget = 0
    while budget < travel_costs:
        savings = float(input())
        budget += savings
    else:
        print(f"Going to {destination}!")

    destination = input()
