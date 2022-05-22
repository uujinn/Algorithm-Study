from collections import defaultdict, Counter


def solution(id_list, report, k):
    answer = []
    answer_dict = defaultdict()

    report_dict = defaultdict()
    report_list = []

    for r in report:
        r = r.split()
        report_list.append((r[0], r[1]))
        report_dict[r[0]] = r[1]

    counter = Counter(report_dict.values())
    print(counter)
    for id in id_list:
        if counter[id] >= k:
            answer.append(id)

    for r in report_list:
        if r[1] in answer:
            answer_dict[r[0]] = r[1]

    return answer


print(solution(["muzi", "frodo", "apeach", "neo"], [
      "muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))
