from string import ascii_lowercase
alphabet = list(ascii_lowercase)

november = int(input())
lima = int(input())

symbol_1 = 0
symbol_2 = 0
symbol_3 = ''
symbol_4 = ''
symbol_5 = 0
password = ""


for i in range(1, november):
    symbol_1 = str(i)

    for j in range(1, november):
        symbol_2 = str(j)

        for a in range(lima):
            symbol_3 = alphabet[a]

            for b in range(lima):
                symbol_4 = alphabet[b]

                for k in range(1, november+1):
                    if k > i and k > j:
                        symbol_5 = str(k)

                        password = symbol_1 + symbol_2 + symbol_3 + symbol_4 + symbol_5
                        print(password, end=' ')


