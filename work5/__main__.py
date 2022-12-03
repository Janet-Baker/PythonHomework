def main_handler(n):
    if n in range(13):
        results = []
        for i in range(n + 1):
            if i == 0:
                results.append([1])
            elif i == 1:
                results.append([1, 1])
            else:
                y = []
                for j in range(i + 1):
                    if j == 0 or j == i:
                        y.append(1)
                    else:
                        y.append(results[i - 1][j - 1] + results[i - 1][j])
                results.append(y)
        return results
    else:
        raise IndexError


if __name__ == '__main__':
    n = input()
    n = int(n)
    raw_lines = main_handler(n)
    for line in range(n+1):
        print(("  "*(n-line)), end="")
        for k in raw_lines[line]:
            print("{:>4}".format(k), end="")
        print()
