if __name__ == '__main__':
    n = input()
    n = int(n)
    lists = input().split()
    lists = list(map(int, lists))
    lists.sort()
    lists = list(map(str, lists))
    print(" ".join(lists))
