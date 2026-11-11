print("< SWIMMING POOL ENTRY CHECKER >")

age = int(input("\nHow old are you (years): "))
height = int(input("What is your height(cm): "))
accompany = input("Are you accompanied by an adult (yes/no): ")

print("\n< ENTRY DECISION >")
print("__________________")

if age <= 5:
    print("\nAge group: Toddler")
elif age >= 6 and age < 13:
  print("\nAge group: Child")
elif age >= 13 and age < 20:
  print("\nAge group: Teenager")
elif age >= 20 and age < 25:
  print("\nAge group: Pre-Adult")
elif age >= 25 and age < 60:
  print("\nAge group: Adult ")
else:
  print("\nAge group: Senior")

if height <= 40:
  print("Sorry! Can't swim today. Maybe next time when you are a bit taller.")
elif height >=41 and height < 90 and accompany == yes:
  print("Remember to swim at the shallow end only.\nEnjoy your swim and keep safe")
elif height >=41 and height < 90 and accompany == no:
  print("Ask for an adult to accompany you before swimming.")
elif height >= 90 and height < 120 and accompany == yes:
  print("Don't go too far deep. Stay in the 1 metre pool depth.\nEnjoy your swim and keep safe")
elif height >= 90 and height < 120 and accompany == no:
  print("Ask for an adult to accompany you before you go to swim.")
elif height >= 120 and height < 150 and accompany == yes:
  print("Don't go too far deep. Stay in the 1 metre pool depth.\nEnjoy your swim and keep safe")
elif height >= 120 and height < 150 and accompany == no:
  print("Ask for an adult to accompany you before you go to swim.")
elif height >= 150 and height < 170:
  print("You are free to swim at any depth you like but remember not to go into the 2 metre end.\nEnjoy your swim and keep safe")
else: 
  print("You are free to swim at any depth you like.\nEnjoy your swim and keep safe")