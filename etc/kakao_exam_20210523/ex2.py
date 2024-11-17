from math import factorial


def solution(n):
    powers = [n]
    prev = n
    while True:
        power = 0
        for c in str(prev):
            power += factorial(int(c))
        if power in powers:
            break
        powers.append(power)
        prev = power
    reader = max(powers)
    return len(powers) * reader


if __name__ == '__main__':
    print(solution(5))
    print(solution(540))
