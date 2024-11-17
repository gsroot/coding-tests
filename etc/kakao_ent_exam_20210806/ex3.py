import sys
import string


def get_origin(A):
    stack = []
    result = ''
    sub_result = ''
    for i, c in enumerate(A):
        if c.isdecimal():
            stack.append(c)
        elif c == '[':
            continue
        elif c == ']':
            while True:
                cc = stack.pop()
                if not cc.isdecimal():
                    sub_result += cc
                else:
                    for x in range(int(cc)):
                        for y in sub_result[::-1]:
                            stack.append(y)
                    sub_result = ''
                    break
        else:
            stack.append(c)
    while stack:
        result += stack.pop()

    return result[::-1]


if __name__ == '__main__':
    A = '2[ab]3[cd]'
    print(get_origin(A))
