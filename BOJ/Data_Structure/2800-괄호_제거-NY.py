from itertools import combinations
from sys import stdin

s = stdin.readline().rstrip()
l = []
stack = []
answer = set()

for idx, v in enumerate(list(s)):
    if v == '(':
        stack.append(idx) 
    elif v == ')':
        start = stack.pop()
        end = idx
        l.append([start,end])

for i in range(1,len(l)+1):
    c = combinations(l,i)
    for j in c:
        tmp = list(s)
        for k in j:
            start,end = k
            tmp[start] = ''
            tmp[end] = ''
        answer.add(''.join(tmp))


for i in sorted(list(answer)):
    print(i)