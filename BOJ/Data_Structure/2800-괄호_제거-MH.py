from sys import stdin
from itertools import combinations

def solution(expression):
    bracket_num = 0             # 괄호가 몇 쌍있는지 저장
    stack = []                  # 괄호의 짝을 찾기 위한 stack
    exp_index = []              # 전체 수식의 index를 저장
    combi = []                  # 모든 조합
    answer = []
    
    for exp in expression:                  # 입력받은 수식에 하나씩 index 부여
        if exp == '(':                      # (2+(2*2)+2) 이면
            stack.append(bracket_num)       # [0, -100, -100, 1, -100, -100, -100, 1, -100, -100, 0]
            exp_index.append(bracket_num)
            bracket_num += 1
        elif exp == ')':
            exp_index.append(stack.pop())
        else:
            exp_index.append(-100)
    
    combi_list = [i for i in range(bracket_num)]        # 조합을 위한 리스트
    
    for i in range(bracket_num):                        # 괄호 1 ~ n개 제거의 조합을 담은 리스트
        for j in list(combinations(combi_list, i + 1)):
            combi.append(j)
    
    for c in combi:                         # 조합 경우의 수에 따라 나올 수 있는 식 저장
        temp = ''
        for exp, idx in zip(expression, exp_index):
            if idx not in c or idx == -100:
                temp += str(exp)
        answer.append(temp)

    return '\n'.join(sorted(set(answer)))
        
        
print(solution(stdin.readline().rstrip()))