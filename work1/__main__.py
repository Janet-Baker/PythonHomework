def commit_space(__old):
    __new = __old.replace("  ", " ")
    while not (__old == __new):
        __old = __new
        __new = __old.replace("  ", " ")
    return __new


if __name__ == '__main__':
    input_file = open("fcopy.in", mode="r", encoding="utf-8", errors="ignore")
    process_string = input_file.read()
    # process_string = " ".join(process_string.split())
    process_string = process_string.replace("\t", " ")
    process_string = commit_space(process_string)
    output_file = open("fcopy.out", mode="w", encoding="utf-8", errors="ignore")
    # print(process_string, file=output_file, end="")
    output_file.write(process_string)
    input_file.close()
    output_file.close()
