import sys
import string


def make_result(origin):
    s_tokens = []
    s_char_bef = False
    for c in origin:
        if c == '\n':
            break
        if c in list(string.ascii_lowercase + string.ascii_uppercase) or c.isdecimal():
            s_char_bef = False
        else:
            if s_tokens and s_char_bef:
                s_tokens[-1] += c
            else:
                s_tokens.append(c)
            s_char_bef = True
    for s_token in s_tokens:
        origin = origin.replace(s_token, ' ')
    return origin


if __name__ == '__main__':
    line = sys.stdin.readline()
    for i in range(int(line)):
        origin = sys.stdin.readline()
        print(make_result(origin))
