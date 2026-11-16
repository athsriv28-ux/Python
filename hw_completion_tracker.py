total_homework = 4
original_count = total_homework
print(f"You have {original_count} homework to finish today.\n")

completed_count = 0
homework_num = 1

while homework_num <= total_homework:
    
    if homework_num == 1:
        next_homework = "Mathematics practice paper"
    elif homework_num == 2:
        next_homework = "English reading"
    elif homework_num == 3:
        next_homework = "Science practical experiment"
    else:
        next_homework = "coding project"

    answer = input(f"Have you completed {next_homework}(yes/no): ")
    
    if answer == "yes" :
        completed_count += 1
        homework_num += 1
        print(f"Great job! Homework {next_homework}, completed.")
    else:
        print("Alright, finish it and check again.")

    print("Homework remaining: ", total_homework - completed_count)

print("\nAll homework complete!")
print("Great work finishing all your homework today!")
print("\n< Homework Completion Summary >")
print("Homework assigned: 4")
print("Homework completed: 4")
print("Homework remaining: 0")
print("\nKeep up the good work!!")


