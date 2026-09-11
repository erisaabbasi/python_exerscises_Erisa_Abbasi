students = {
    "Ali" : [18,17,20] ,
    "Sara" : [15,19,18] ,
    "Reza" : [12,14,10] ,
    "Mina" : [20,20,19]
}
best_avg = 0
best_student = ""
for name in students:
    grades = students[name]
    average = sum(grades) / len(grades)
    highest = max(grades)
    print(name)
    print("Average: ",average)
    if average >= 15:
        print("Status: Passed")
    else:
        print("Status: Failed")
    print("highest grade: ",highest)
    print()
    if average > best_avg:
        best_avg = average
        best_student = name
print("Best student: ",best_student)
print("highest average: ",best_avg)

