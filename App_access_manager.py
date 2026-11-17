name = input("Enter your name: ")
grade = int(input("Enter your grade: "))
app = input("Enter your requested app: ")

print("\n< Identity Checker >")
if type(name) is str:
  print("Name is stored as text.")
  print("You are a member.")
else:
  print("Name is not stored as text.")
  print("You are not a member")

if grade >= 1 and grade < 7:
    approved_apps = ["Coding app", "Math app", "Science app", "Reading app"]
    restricted_apps = ["Gaming app", "Social media app", "Shopping app"]
elif grade >= 7 and grade < 13:
    approved_apps = ["Coding app", "Math app", "Science app", "Reading app", "Gaming app", "Social media app", "Shopping app"]
    restricted_apps = []
else:
    print("Invalid grade!")
print("\n< App Approval Check >")
if app in approved_apps not in restricted_apps:
  print("The app is an approved student app for you.")
  print("Access granted!")
else:
  print("The app is not an approved student app for you.")
  print("Access denied!")