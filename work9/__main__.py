if __name__ == '__main__':
    instr = input()
    list = ["a", "b", "d", "c", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]
    dict = {}
    for i in instr:
        if i in list:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
    maxcount = max(dict.values())
    for k, v in dict.items():
        if v == maxcount:
            print(k, end=" ")
            print(v)
