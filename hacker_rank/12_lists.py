# Solución avanzada
if __name__ == '__main__':
    N = int(input())
    lst = []

    for _ in range(N):
        parts = input().split()
        cmd = parts[0]
        args = list(map(int, parts[1:]))

        if cmd == "print":
            print(lst)
        else:
            getattr(lst, cmd)(*args)

# Solución básica
if __name__ == '__main__':
    N = int(input())
    lst = []

    for _ in range(N):
        cmd = input().split()

        if cmd[0] == "insert":
            lst.insert(int(cmd[1]), int(cmd[2]))
        elif(cmd[0] == "print"):
            print(lst)
        elif(cmd[0] == "remove"):
            lst.remove(int(cmd[1]))
        elif(cmd[0] == "append"):
            lst.append(int(cmd[1]))
        elif(cmd[0] == "pop"):
            lst.pop()
        elif(cmd[0] == "reverse"):
            lst.reverse()
        elif(cmd[0] == "sort"):
            lst.sort()

# Solución intermedia
if __name__ == '__main__':
    N = int(input())
    lst = []
    
    operations = {
        'append': lambda x: lst.append(x),
        'print': lambda: print(lst),
        'remove': lambda x: lst.remove(x),
        'insert': lambda i, x: lst.insert(i, x),
        'sort': lambda: lst.sort(),
        'pop': lambda: lst.pop(),
        'reverse': lambda: lst.reverse()
    }
    
    inputs = [input().split() for _ in range(N)]
    for command in inputs:
        operations[command[0]](*[int(x) for x in command[1:]])