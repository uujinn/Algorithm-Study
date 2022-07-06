from collections import deque

def solution(priorities, location):
    deq = deque()    
    for idx, p in enumerate(priorities):
        deq.append((idx, p))
    
    count = 1
    prior = max(priorities)
    while deq:
        if deq[0][1] == prior:
            if deq[0][0] == location:
                return count          
            
            count += 1
            deq.popleft()
            prior = max(deq, key=lambda x : x[1])[1]
                        
        else:
            deq.rotate(-1)
    
print(solution([1, 1, 9, 1, 1, 1],	0))