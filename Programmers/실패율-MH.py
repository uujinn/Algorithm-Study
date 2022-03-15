def solution(N, stages):
    rate = {}
    answer = []
    
    users = len(stages)
    for i in range(1, N + 1):
        loser = stages.count(i)
        rate[i] = loser / users if loser != 0 else 0
        users -= loser
    
    dict = sorted(rate.items(), reverse=True, key=lambda x : x[1])
    for d in dict:
        answer.append(d[0])

    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))