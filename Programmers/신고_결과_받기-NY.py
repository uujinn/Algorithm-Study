def solution(id_list, report, k):
    data = {}
    result = []
    for id in id_list: data[id] = [[], 0, 0]
    for r in report:
        a, b = map(str, r.split(' '))
        if b not in data[a][0]:
            data[a][0].append(b)
            data[b][1] += 1
    for id in id_list:
        for reported in data[id][0]:
            if data[reported][1] >= k: data[id][2] += 1
        result.append(data[id][2])
    return result