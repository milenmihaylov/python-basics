sofia_commission = {"s1": 0.05, "s2": 0.07, "s3": 0.08, "s4": 0.12}
varna_commission = {"s1": 0.045, "s2": 0.075, "s3": 0.10, "s4": 0.13}
plovdiv_commission = {"s1": 0.055, "s2": 0.08, "s3": 0.12, "s4": 0.145}

town = input()
sales = float(input())

commission = 0

if town == "Sofia":
    if 0 <= sales <= 500:
        commission = sales * sofia_commission["s1"]
        print(f"{commission:.2f}")
    elif 500 < sales <= 1000:
        commission = sales * sofia_commission["s2"]
        print(f"{commission:.2f}")
    elif 1000 < sales <= 10000:
        commission = sales * sofia_commission["s3"]
        print(f"{commission:.2f}")
    elif sales > 10000:
        commission = sales * sofia_commission["s4"]
        print(f"{commission:.2f}")
    else:
        print("error")

elif town == "Varna":
    if 0 <= sales <= 500:
        commission = sales * varna_commission["s1"]
        print(f"{commission:.2f}")
    elif 500 < sales <= 1000:
        commission = sales * varna_commission["s2"]
        print(f"{commission:.2f}")
    elif 1000 < sales <= 10000:
        commission = sales * varna_commission["s3"]
        print(f"{commission:.2f}")
    elif sales > 10000:
        commission = sales * varna_commission["s4"]
        print(f"{commission:.2f}")
    else:
        print("error")
elif town == "Plovdiv":
    if 0 <= sales <= 500:
        commission = sales * plovdiv_commission["s1"]
        print(f"{commission:.2f}")
    elif 500 < sales <= 1000:
        commission = sales * plovdiv_commission["s2"]
        print(f"{commission:.2f}")
    elif 1000 < sales <= 10000:
        commission = sales * plovdiv_commission["s3"]
        print(f"{commission:.2f}")
    elif sales > 10000:
        commission = sales * plovdiv_commission["s4"]
        print(f"{commission:.2f}")
    else:
        print("error")
else:
    print("error")
