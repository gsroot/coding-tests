def mystery(x, y):
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x
        print(x, y)
    print('final!')
    print(x)


if __name__ == '__main__':
    mystery(2437, 875)
