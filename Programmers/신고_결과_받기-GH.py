from collections import defaultdict

def solution(id_list, report, k):
    answer = list()
    count = defaultdict(int)
    user = defaultdict(set)

    for i in report:
        a, b = i.split()
        if b not in user[a]:
            user[a].add(b)
            count[b] += 1

    for id_num in id_list:
        result = 0
        for u in user[id_num]:
            if count[u] >= k:
                result += 1
        answer.append(result)
    return answer