length_cm = int(input())
width_cm = int(input())
height_cm = int(input())
percentage_occupied_volume = float(input())
tank_volume_liters = length_cm * width_cm * height_cm / (10 ** 3)
water_needed_liters = tank_volume_liters * (1 - percentage_occupied_volume / 100)
print(water_needed_liters)


