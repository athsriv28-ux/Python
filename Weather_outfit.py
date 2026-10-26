temperature = int(input("Enter today's temperature in Celcius: "))
if temperature < 20:
    outfit = "jacket"
    print("It is cold today.")
    print("Wear a ", outfit)
else:
    outfit = "t-shirt"
    print("It is warm today.")
    print("Wear a ", outfit)

raining = input("Is it raining today(yes/no): ")
if raining == "yes":
    print("Bring an umbrella!")

wind_speed = int(input("Enter the wind speed in km/h: "))
if wind_speed > 30:
    needs_windbreaker = "yes"
    print("It is windy today")
    print("Wear a windbreaker over your ", outfit)
else:
    needs_windbreaker = "no"
    print("The wind is calm today.")
    print("No windbreaker over your ", outfit)

puddles = input("Are there puddles on the ground(yes/no): ")
if puddles == "yes":
    shoes = "boots"
    print("The ground is wet.")
    print("Wear ", shoes)
else:
    shoes = "sneakers"
    print("The ground is dry.")
    print("Wear ", shoes)

print("\nWeather check complete...")
print("\nWEATHER OUTFIT PICKER:")
print("Temperature: ", temperature)
print("Outfit chosen: ", outfit)
print("Raining: ", raining)
print("Windbreaker needed: ", needs_windbreaker)
print("Shoes chosen: ", shoes)
print("==========================================================")





