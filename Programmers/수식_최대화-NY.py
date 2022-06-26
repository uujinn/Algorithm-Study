from collections import deque
from itertools import permutations

def solution(expression):
    maxiumum = 0
    #1. 연산자 개수를 찾는다 & 숫자를 분리한다
    oper = deque()
    for e in expression:
        if not e.isalnum(): oper.append(e)
    set_oper = set(oper)

    s = expression
    for o in set_oper:
        s = s.replace(o, ',')
    nums = deque(s.split(','))
    
    #2. 개수에 맞는 모든 경우의 수를 찾아서 배열에 담는다.
    priority = list(permutations(set_oper, len(set_oper)))
    
    #3. 모든 경우의 수를 탐색하면서 최대값을 찾는다.(스택 2개 이용. 하나는 숫자. 하나는 연산자)
    for p in priority:
        operators = []
        numbers = []
        while not oper and not nums:
            o = oper.popleft()
            n = nums.popleft()
            
    
    return maxiumum

print(solution("100-200*300-500+20"))