import sys
input = sys.stdin.readline
from itertools import combinations

def solution(expression):
    answer, stack, bracket = [], [], []

    for i, exp in enumerate(expression):
        if exp == '(':
            stack.append(i)
        elif exp == ')':
            bracket.append((stack.pop(), i))    # 괄호 페어... 저장

    for i in range(len(bracket)):
        for comb in combinations(bracket, i+1):
            cur_case = sorted([exp for each in comb for exp in each], reverse=True)     # 인덱스만 추출, 내림차순으로 정렬
            temp = list(expression)     # 인덱스로 요소 제거를 위해 리스트로 변환

            for exp in cur_case:    # 괄호를 제거함
                del temp[exp]

            answer.append(''.join(temp))

    return '\n'.join(sorted(list(set(answer))))     # 중복인 것을 제거함

if __name__ == '__main__':
    expression = input().strip()
    result = solution(expression)
    print(result)