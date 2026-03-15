
passed_count = 0
failed_count = 0
total_students = 15
pass_mark = 45

for count in range(total_students):
   
    score = int(input(f"Enter score for student {count + 1}: "))

    
    if score >= pass_mark:
        passed_count += 1
    else:
        failed_count += 1


print(passed_count)
print(failed_count)




