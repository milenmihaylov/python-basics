text = input()

vowels_dict = {'a': 1, 'e': 2, "i": 3, 'o': 4, 'u': 5}

total = 0

for letter in text:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        total += vowels_dict[letter]

print(total)
