n = int(input())
number = 1
'''
while number <= n:
    print(number)
    number = 2 * number + 1
'''

for number in range(1, n + 1, number * 2 + 1):
    print(number)

