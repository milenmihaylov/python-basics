from math import floor

leap_year = input()
holidays = int(input())
hometown_weekends = int(input())

# Играе само през празничните дни и уикендите
# годината има точно 48 уикенда
# играе в София всяка събота (1 ден), когато не е на работа и не пътува до родния град
# не е на работа 3/4 от уикендите, когато е в софия
# пътува hometown_weekends пъти до родния си град, където играе в неделя
# играе в 2/3 от празничните дни
# през високосните игреа с 15% повече
# колко пъти през годината е играл

weekends_yearly = 48

sofia_weekends = weekends_yearly - hometown_weekends
sofia_free_weekends = 0.75 * sofia_weekends  # когато не е на работа
sofia_games = sofia_free_weekends  # играе винаги, когато е свободен
hometown_games = hometown_weekends  # играе винаги, когато си е вкъщи
holiday_games = holidays * 2 / 3

total_games = sofia_games + hometown_games + holiday_games

# да прибавим игрите, когато е високосна година
if leap_year == "leap":
    total_games *= 1.15
elif leap_year == "normal":
    pass

print(floor(total_games))
