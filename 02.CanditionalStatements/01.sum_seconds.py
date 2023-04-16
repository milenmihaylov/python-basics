player_1 = int(input())
player_2 = int(input())
player_3 = int(input())

total_time = player_1 + player_2 + player_3

'''
моя код
if total_time > 119:
    print(f"2:{total_time - 120:2f}")
elif total_time > 59:
    print(f"1:{total_time - 60:.-2f}")
else:
    print(f"0:{total_time}")
'''

minutes = total_time // 60
seconds = total_time % 60

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")

