import math
def solution(p, speeds):
    answer = []
    for i in range(len(p)):
        p[i] = math.ceil((100 - p[i])/speeds[i])
    front = p.pop(0)
    cnt = 1
    while p:
        if p[0] <= front:
            front = p.pop(0)
            cnt += 1
            if not p: answer.append(cnt)
        else:
            answer.append(cnt)
            cnt = 0
            front = p[0]
    return answer

print(solution([93, 30, 55], [1, 30, 5]))