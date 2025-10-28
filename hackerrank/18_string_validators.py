if __name__ == '__main__':
    s = input()
    s = list(s)
    score = [0,0,0,0,0]

    for i in s:
        if i.isalnum():
            score[0] = 1
            break
    for i in s:
        if i.isalpha():
            score[1] = 1
            break
    for i in s:
        if i.isdigit():
            score[2] = 1
            break
    for i in s:
        if i.islower():
            score[3] = 1
            break
    for i in s:
        if i.isupper():
            score[4] = 1
            break

    for d in score:
        if d == 1:
            print(True)
        else:
            print(False)