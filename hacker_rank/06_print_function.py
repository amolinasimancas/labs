if __name__ == '__main__':
    n = int(input())
    if n >= 1 and n <= 150:
        lista = []
        for i in range(n):
            lista.append(str(i+1))
        string = ''.join(lista)
    print(string)