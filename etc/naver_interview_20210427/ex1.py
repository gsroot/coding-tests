def main(n_str):
    counts = []
    count = 0
    first = int(n_str[0])
    for i, n_char in enumerate(n_str):
        n = int(n_char)
        if n == first:
            count += 1
        else:
            counts.append([count, first])
            first = n
            count = 1
    counts.append([count, first])

    result = ''
    for c, n in counts:
        result += str(c)
        result += str(n)
    return result


if __name__ == '__main__':
    print(main('1211'))
