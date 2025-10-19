if __name__ == "__main__":
    l = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name, score])

    num_l = []
    for (name, score) in l:
        num_l.append(score)
    
    second_lowest = list(sorted(set(num_l)))[1]
    l.sort()
    for (name, score) in l:
        if score == second_lowest:
            print(name)

python_students = [
    ['Harry', 37.21], 
    ['Berry', 37.21], 
    ['Tina', 37.2], 
    ['Akriti', 41], 
    ['Harsh', 39]
]

# Otra solución
'''
if len(python_students) >= 2 and len(python_students) <= 5:
    second_lowest_score = sorted(set([score for name, score in python_students]))[1]
    second_lowest_students = sorted([name for name, score in python_students if score == second_lowest_score])
    
    for student in second_lowest_students:
        print(student)
'''