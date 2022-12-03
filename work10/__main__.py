if __name__ == '__main__':
    count = input()
    series = input().split()
    series = list(map(int, series))
    series.sort()
    dict = {}
    for i in series:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    maxcount = max(dict.values())
    for k, v in dict.items():
        if v == maxcount:
            print(k, end=" ")
            print(v)
