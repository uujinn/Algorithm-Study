from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for co in course:
        combs = []
        for i in orders:
            comb = combinations(i, co)
            for c in comb:
                combs.append(''.join(sorted(c)))

        counter = Counter(combs).most_common()
        answer += [menu for menu, cnt in counter if cnt >
                   1 and cnt == counter[0][1]]

    return sorted(answer)


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
