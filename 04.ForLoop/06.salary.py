n = int(input())
salary = int(input())

fb_fine = 150
insta_fine = 100
reddit_fine = 50

for i in range(n):
    tabs = input()
    if tabs == "Facebook":
        salary -= fb_fine
    elif tabs == "Instagram":
        salary -= insta_fine
    elif tabs == "Reddit":
        salary -= reddit_fine

if salary <= 0:
    print("You have lost your salary.")
else:
    print(f"{salary}")
