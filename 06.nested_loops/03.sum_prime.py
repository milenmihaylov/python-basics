number = input()
prime_sum = 0
non_prime_sum = 0

while not number == "stop":
    number = int(number)
    if number < 0:
        print("Number is negative.")
    else:
        prime_number = True
        for y in range(2, number):
            while number % y == 0:
                prime_number = False
                break

        if prime_number:
            prime_sum += number
        else:
            non_prime_sum += number

    number = input()

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")
