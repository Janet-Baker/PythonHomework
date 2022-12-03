global square_n


def square_plus(a, b):
    answer = [[0] * square_n for i in range(square_n)]
    for t1 in range(square_n):
        for t2 in range(square_n):
            answer[t1][t2] = a[t1][t2] + b[t1][t2]
    return answer


def square_minus(a, b):
    answer = [[0] * square_n for i in range(square_n)]
    for t1 in range(square_n):
        for t2 in range(square_n):
            answer[t1][t2] = a[t1][t2] - b[t1][t2]
    return answer


def square_power(a, b):
    answer = [[0] * square_n for i in range(square_n)]
    for t1 in range(square_n):
        for t2 in range(square_n):
            for i in range(square_n):
                answer[t1][t2] += a[t1][i] * b[i][t2]
    return answer


if __name__ == '__main__':
    input_a = input()
    square_1 = []
    square_2 = []
    input_a = input_a.split()
    input_a = list(map(int, input_a))
    square_1.append(input_a)
    square_n = int(len(input_a))
    if square_n in range(2, 11, 1):
        for m in range(1, square_n, 1):
            input_a = input()
            input_a = input_a.split()
            input_a = list(map(int, input_a))
            square_1.append(input_a)
    input_operation = input()
    for m in range(square_n):
        input_b = input()
        input_b = input_b.split()
        input_b = list(map(int, input_b))
        square_2.append(input_b)
    if input_operation.__contains__("+"):
        response = square_plus(square_1, square_2)
    elif input_operation.__contains__("-"):
        response = square_minus(square_1, square_2)
    elif input_operation.__contains__("*"):
        response = square_power(square_1, square_2)
    else:
        raise TypeError("Unsupported operation")
    for line in range(square_n):
        for k in range(square_n):
            print("{:>5}".format(response[line][k]), end="")
        print()
