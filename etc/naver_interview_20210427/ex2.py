def find_pair(c):
    bs1 = [['(', ')'], ['[', ']'], ['{', '}']]
    for x in bs1:
        for i, y in enumerate(x):
            if c == y:
                return x[1] if i == 0 else x[0]


def main(s):
    bs2 = [['(', '[', '{'], [')', ']', '}']]
    brace_list = []
    for c in s:
        if c in bs2[0]:
            brace_list.append(c)
        elif c in bs2[1]:
            if find_pair(c) == brace_list[-1]:
                brace_list.pop()
            else:
                return False
    return len(brace_list) == 0


if __name__ == '__main__':
    print(main('[aa(]abcd)ddaa-'))
