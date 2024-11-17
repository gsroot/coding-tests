def match(A):
    word, p = A.split()
    for i in range(len(word) - len(p) + 1):
        for j in range(len(p)):
            if word[i + j] != p[j]:
                break
        else:
            return True
    return False


if __name__ == '__main__':
    A = 'apple app*'
    print(match(A))
    A = 'apple at'
    print(match(A))
