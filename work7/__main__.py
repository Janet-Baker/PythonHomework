import math


def is_prime_number(n: int) -> bool:
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1, 1):
            if n % i == 0:
                return False
        return True


def reverse_number(n: int):
    m = str(n)
    return int(m[::-1])


if __name__ == '__main__':
    input_n = int(input())
    if is_prime_number(input_n):
        reverse_n = reverse_number(input_n)
        if is_prime_number(reverse_n):
            print("yes")
        else:
            print("no")
    else:
        print("no")
