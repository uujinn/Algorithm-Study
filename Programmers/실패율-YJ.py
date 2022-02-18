from collections import Counter

def solution(N, stages):
    
    answer = []
    players = len(stages) # 사용자 수
    counters = {}

    stages.sort()
    c = Counter(stages) # 스테이지 별 사용자 수 카운트

    for i in c:
        if i in range(1, N+1):
            counters[i] = c[i] / players
            players -= c[i]

    # 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의
    for i in range(1, N+1):
        if i not in counters:
            counters[i] = 0

    # 만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 된다
    counters = dict(sorted(counters.items(), key=lambda x: (-x[1], x[0])))
    answer = list(counters.keys())

    return answer
