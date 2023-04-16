paper_rolls = int(input())
fabric_rolls = int(input())
glue_litters = float(input())
discount = int(input())

paper_cost = 5.8
fabric_cost = 7.2
glue_cost = 1.2

discount *= 0.01
total_costs = paper_cost * paper_rolls + fabric_cost * fabric_rolls + glue_cost * glue_litters
total_costs *= (1 - discount)
print(f"{total_costs:.3f}")
