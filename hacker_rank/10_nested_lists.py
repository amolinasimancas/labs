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