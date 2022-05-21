from collections import defaultdict

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    singo = defaultdict(list)       # 각 유저가 신고한 유저 리스트
    singoed = defaultdict(int)      # 각 유저가 신고당한 횟수
    
    for r in set(report):
        a, b = map(str, r.split())
        singo[a].append(b)
        singoed[b] += 1
        
    # singo : {'apeach': ['frodo', 'muzi'], 'muzi': ['frodo', 'neo'], 'frodo': ['neo']})
    # singoed : {'frodo': 2, 'neo': 2, 'muzi': 1})
    
    for idx, i in enumerate(id_list):        
        for j in singo[i]:
            if singoed[j] >= k:
                answer[idx] += 1
            
    return answer

# print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))