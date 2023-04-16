sofia_prices = {"coffee": 0.50, "water": 0.80, "beer": 1.20, "sweets": 1.45, "peanuts": 1.60}
plovdiv_prices = {"coffee": 0.40, "water": 0.70, "beer": 1.15, "sweets": 1.30, "peanuts": 1.50}
varna_prices = {"coffee": 0.45, "water": 0.70, "beer": 1.10, "sweets": 1.35, "peanuts": 1.55}

product = input()
city = input()
quantity = float(input())

product_price = 0

if city == "Sofia":
    product_price = sofia_prices[product]
elif city == 'Plovdiv':
    product_price = plovdiv_prices[product]
elif city == 'Varna':
    product_price = varna_prices[product]

cost = product_price * quantity
print(cost)
