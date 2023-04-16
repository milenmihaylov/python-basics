first_barcode = input()
last_barcode = input()
"""
str_barcode = ''
not_all_odd = False

for barcode in range(first_barcode, last_barcode + 1):
    str_barcode = str(barcode)
    for i in str_barcode:
        not_all_odd = False
        i = int(i)
        if not i % 2 == 0:
            continue
        else:
            not_all_odd = True
            break
    if not_all_odd:
        continue
    else:
        print(str_barcode, end=' ')
"""

for first_number in range(int(first_barcode[0]), int(last_barcode[0]) + 1):
    if first_number % 2 == 0:
        continue
    else:
        for second_number in range(int(first_barcode[1]), int(last_barcode[1]) + 1):
            if second_number % 2 == 0:
                continue
            else:
                for third_number in range(int(first_barcode[2]), int(last_barcode[2]) + 1):
                    if third_number % 2 == 0:
                        continue
                    else:
                        for forth_number in range(int(first_barcode[3]), int(last_barcode[3]) + 1):
                            if forth_number % 2 == 0:
                                continue
                            else:
                                print(f"{first_number}{second_number}{third_number}{forth_number}", end=' ')
