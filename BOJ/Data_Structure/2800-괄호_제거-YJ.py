from itertools import combinations
from sys import stdin

expression = stdin.readline().rstrip()

length = len(expression)
index_stack = [] # index 넣을 stack
index_pair = [] # index 쌍 넣을 리스트
answer = []

for i, e in enumerate(reversed((expression))): # 괄호 index 쌍 확인
    index = length - i - 1
    if e == ")":
        index_stack.append(index)
    elif e == "(":
        index_pair.append((index, index_stack.pop()))

for i in range(1, len(index_pair) + 1):
    comb = list(combinations(index_pair, i)) # index 쌍 조합
    for c in comb:
        tmp = list(expression)[:]
        for x, y in c:
            tmp[x] = ''
            tmp[y] = ''
        answer.append("".join(map(str, tmp)))

answer = sorted(list(set(answer))) # 중복 방지 - set
print("\n".join(answer))