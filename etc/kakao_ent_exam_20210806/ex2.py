import sys
import string


def kth_sn(A, B, K):
    i, j = 0, 0
    result = 0
    A_fin, B_fin = False, False
    while K > 0:
        if A[i] <= B[j] or B_fin:
            result = A[i]
            if i < len(A) - 1:
                i += 1
            else:
                A_fin = True
            K -= 1
        elif A[i] >= B[j] or A_fin:
            result = B[j]
            if j < len(B) - 1:
                j += 1
            else:
                B_fin = True
            K -= 1

    return result


if __name__ == '__main__':
    A = [int(x) for x in '3 28 99 108 112 123 291 543 934 1221 '.split()]
    B = [int(x) for x in '5 104 111 12,356'.split()]
    K = 9
    print(kth_sn(A, B, K))
