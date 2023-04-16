deposit = input()
account = 0

while deposit != "NoMoreMoney":
    deposit = float(deposit)
    if deposit < 0:
        print("Invalid operation!")
        break
    else:
        print(f"Increase: {deposit:.2f}")
        account += deposit
        deposit = input()

print(f"Total: {account:.2f}")
