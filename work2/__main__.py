if __name__ == '__main__':
    input_a = (input()).split()
    input_b = (input()).split()
    line_a = list(set(input_a) ^ set(input_b))
    line_b = list(set(input_a) & set(input_b))
    line_a = list(map(int, line_a))
    line_a.sort()
    line_a = list(map(str, line_a))
    line_b = list(map(int, line_b))
    line_b.sort()
    line_b = list(map(str, line_b))
    if len(line_a) != 0:
        print(" ".join(line_a), end=" ")
    print(flush=True)
    if len(line_b) != 0:
        print(" ".join(line_b), end=" ")
    print(flush=True)
