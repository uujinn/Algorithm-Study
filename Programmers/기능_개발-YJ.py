def solution(progresses, speeds):
    answer = [0 for _ in range(len(speeds))]
    days = []

    for progress, speed in zip(progresses, speeds):
        day = (100 - progress) // speed if ((100-progress) %
                                            speed) == 0 else ((100 - progress) // speed) + 1
        days.append(day)
    print(days)
    idx = 0
    while idx < len(days):
        target_idx = idx
        for d in days[idx:]:
            if days[target_idx] < d:
                break
            else:
                answer[target_idx] += 1
                idx += 1

    answer = [item for item in answer if item != 0]
    return answer
