everest_height = 8848
base_camp_height = 5364

days_climbing = 1
resting = ''
meters_climbed = 0
total_meters = base_camp_height
success = False

climbing = True
while climbing:
    resting = input()
    if resting == 'Yes':
        days_climbing += 1
    elif resting == 'END':
        break

    if days_climbing > 5:
        break

    meters_climbed = int(input())
    total_meters += meters_climbed
    if total_meters >= everest_height:
        success = True
        break

if success:
    print(f"Goal reached for {days_climbing} days!")
else:
    print("Failed!")
    print(f"{total_meters}")
