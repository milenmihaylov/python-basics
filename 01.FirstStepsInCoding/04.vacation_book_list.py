total_pages = int(input())
pages_per_hour = int(input())
total_days = int(input())

pages_per_day = total_pages / total_days
hours_per_day = pages_per_day / pages_per_hour

print(hours_per_day)
