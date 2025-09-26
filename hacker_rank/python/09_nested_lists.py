python_students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

grades = []
for i in range(len(python_students)):
    grades.append(python_students[i][1])

if len(python_students) >= 2 and len(python_students) <= 5:
    print(min(grades))
    