homework_time = int(input("Enter your homework time(min): "))
if homework_time > 60:
    print("That is a long homework session.")
    print("Start homework now.")
    plan = "Start homework now"
else:
    print("That is a short homework session.")
    print("Finish homework as soon as possible.")
    plan = "Finish homework as soon as possible"

time_afterwards = input("Is there spare time after you finish your homework(yes/no): ")
if time_afterwards == "yes":
    print("Reminder: Pick up a hobby for your free time!")
else:
    print("")

print("\n==== Daily Plan ====")
print("\nHomework minutes: ", homework_time)
print("Plan: ", plan)
print("Spare time: ", time_afterwards)
