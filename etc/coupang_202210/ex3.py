class Grade(str):
    def __lt__(self, other):
        lt = self[0] > other[0]
        if self[0] == other[0] and len(self) == 2:
            lt_val = {'-': 0, '0': 1, '+': 2, }
            lt = lt_val[self[1]] < lt_val[other[1]]
        return lt

    def __gt__(self, other):
        gt = self[0] < other[0]
        if self[0] == other[0] and len(self) == 2:
            gt_val = {'-': 0, '0': 1, '+': 2, }
            gt = gt_val[self[1]] > gt_val[other[1]]
        return gt


def solution(grades):
    gdict = dict()
    for g in grades:
        gn, gg = g.split()
        if gn not in gdict or Grade(gg) > Grade(gdict[gn]):
            if gn in gdict:
                del gdict[gn]
            gdict[gn] = Grade(gg)
    answer = [f"{k} {v}" for k, v in sorted(gdict.items(), key=lambda x: x[1], reverse=True)]
    return answer


if __name__ == '__main__':
    grades = [
        "DS7651 A0", "CA0055 D+", "AI5543 C0", "OS1808 B-", "DS7651 B+", "AI0001 F", "DB0001 B-", "AI5543 D+",
        "DS7651 A+", "OS1808 B-"
    ]
    print(solution(grades))
    grades = ["DM0106 D-", "PL6677 B+", "DM0106 B+", "DM0106 B+", "PL6677 C0", "GP0000 A0"]
    print(solution(grades))
