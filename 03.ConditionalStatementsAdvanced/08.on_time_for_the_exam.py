exam_hour = int(input())
exam_minutes = int(input())
arrival_hour: int = int(input())
arrival_minutes = int(input())

# if (arrival_hour == exam_hour and arrival_minutes == exam_minutes) or \
#        (arrival_hour == exam_hour and exam_minutes - 30 <= arrival_minutes < exam_minutes):
#    pass

exam_time_minutes = exam_hour * 60 + exam_minutes
arrival_time_minutes = arrival_hour * 60 + arrival_minutes

is_he_ontime = ""
time_difference = 0

if exam_time_minutes - 30 <= arrival_time_minutes <= exam_time_minutes:
    is_he_ontime = "On time"
elif arrival_time_minutes > exam_time_minutes:
    is_he_ontime = "Late"
elif arrival_time_minutes + 30 < exam_time_minutes:
    is_he_ontime = "Early"

print(is_he_ontime)

if arrival_time_minutes < exam_time_minutes:
    if exam_time_minutes - arrival_time_minutes < 60:
        time_difference = exam_time_minutes - arrival_time_minutes
        print(f"{time_difference} minutes before the start")
    elif exam_time_minutes - arrival_time_minutes >= 60:
        hours_difference = (exam_time_minutes - arrival_time_minutes) // 60
        difference_minutes = (exam_time_minutes - arrival_time_minutes) % 60
        print(f"{hours_difference}:{difference_minutes:0>2d} hours before the start")

elif arrival_time_minutes > exam_time_minutes:
    if arrival_time_minutes - exam_time_minutes < 60:
        time_difference = arrival_time_minutes - exam_time_minutes
        print(f"{time_difference} minutes after the start")
    elif arrival_time_minutes - exam_time_minutes >= 60:
        hours_difference = (arrival_time_minutes - exam_time_minutes) // 60
        difference_minutes = (arrival_time_minutes - exam_time_minutes) % 60
        print(f"{hours_difference}:{difference_minutes:0>2d} hours after the start")
