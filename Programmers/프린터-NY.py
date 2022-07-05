from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque()
    temp = deque()
    
    for idx, priority in enumerate(priorities):
        q.append((priority, idx))
    
    max_num = 0
    while True:
        popped = q.popleft()
        max_num = max(max_num, popped[0])
        temp.append(popped)
        if not q: #popped보다 큰 게 없음
            result = temp.popleft()
            if result[1] == location: return answer+1
            q.extend(temp)
            temp = deque()
            answer += 1
        else:
            if q[0][0] > max_num:
                q.extend(temp)
                temp = deque()
                max_num = 0
                
print(solution([1,1,9,1,1,1], 0))