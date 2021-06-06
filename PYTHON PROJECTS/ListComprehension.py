if __name__ == '__main__':

    k = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        k.append([name,score])
    k = tuple(k)
    dic = dict(k)
    s = [sorted(dic.items())]
    print(s)
