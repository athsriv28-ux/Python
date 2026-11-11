team1 = int(input("How many points did team 1 get: "))
team2 = int(input("How many points did team 2 get: "))
team3 = int(input("How many points did team 3 get: "))
team4 = int(input("How many points did team 4 get: "))
team5 = int(input("How many points did team 5 get: "))
last_week = int(input("How many stars were rewarded last week: "))

total = team1 + team2 + team3 + team4 + team5
average = total / 5

print("\n< Classroom Points Calculator >")
print("Team 1: ", team1)
print("Team 2: ", team2)
print("Team 3: ", team3)
print("Team 4: ", team4)
print("Team 5: ", team5)
print("\nTotal points: ", total)
print("Average per team: ", average)

stars_per_point = 2
stars_rewarded = 2 * total
print("\nStars rewarded: ", stars_rewarded)

boxes = stars_rewarded // 10
leftover = stars_rewarded % 10
print("Boxes filled: ", boxes)
print("Leftover stars: ", leftover)

if last_week == total:
  print("\nStars rewarded same as last week.")
  print("Keep up the good work.")
elif last_week > total:
  print("\nStars rewarded lesser than last week.")
  print("Don't give up.")
elif last_week  < total:
  print("\nStars awarded more than last week")
  print("Good job. Aim for greater heights.")
  