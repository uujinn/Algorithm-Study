from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    combs = []
    for order in orders:
        for i in course:
            comb = combinations(order, i)
            for c in comb:
                combs.append(''.join(c))

    counter = Counter(combs)

    for (key, value) in counter.items():
        if value >= 2:
            answer.append(key)

    return sorted(list(set(answer) & (set(orders))))


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
