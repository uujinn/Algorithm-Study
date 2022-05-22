from collections import defaultdict, Counter


def solution(id_list, report, k):
    answer = []
    report = set(report)

    mail_count = defaultdict(int)
    user_db = defaultdict(int)
    for id in id_list:
        mail_count[id] = 0
        user_db[id] = 0

    report_db = defaultdict(list)

    for r in report:
        r = r.split()
        report_db[r[1]].append(r[0])

    for u in user_db:
        user_db[u] = len(report_db[u])
        pass

    for u in user_db:
        if user_db[u] >= k:
            for v in report_db[u]:
                mail_count[v] += 1

    for mail in mail_count:
        answer.append(mail_count[mail])

    return answer


print(solution(["muzi", "frodo", "apeach", "neo"], [
      "muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))
