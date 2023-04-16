from math import floor

record = float(input())
distance = float(input())
time_1m = float(input())

resistance = floor(distance / 15)
add_time = resistance * 12.5

ivan_time = time_1m * distance + add_time
difference = record - ivan_time
neg_difference = ivan_time - record

if difference > 0:
    print(f"Yes, he succeeded! The new world record is {ivan_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {neg_difference:.2f} seconds slower.")
