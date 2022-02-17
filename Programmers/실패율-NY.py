def solution(N, stages):
    answer = []
    tried = [0 for i in range(N)]
    failed = [0 for i in range(N)]
    return_answer = []
    
    for stage in stages:
        if stage <= N: failed[stage-1] += 1 #failed 하나 쁠
        for i in range(stage if stage <= N else stage-1):
            tried[i] += 1 #tried for문 돌면서 추가
    
    for i, (t, f) in enumerate(zip(tried, failed)):
        answer.append([f/t if t > 0 else 0, i+1]) #f/t 계산
    
    for a in sorted(answer, key=lambda ans: (ans[0], -ans[1]), reverse=True): #f/t기준으로 정렬, 뒤에 스테이지 숫자는 반대로 정렬
        return_answer.append(a[1])
    
    return return_answer

print(solution(4, [4,4,4,4,4]))