from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []

    for c in course:
        temp = []

        for order in orders:
            com = combinations(sorted(order), c)
            temp += com
        dict_ = Counter(temp)

        if dict_:
            max_ = max(list(dict_.values()))
            if max_ >= 2:
                for key, value in dict_.items():
                    if dict_[key] == max_:
                        answer.append(''.join(key))

    return sorted(answer)