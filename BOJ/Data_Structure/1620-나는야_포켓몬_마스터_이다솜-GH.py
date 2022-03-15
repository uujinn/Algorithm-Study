from re import A
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

dict = {}

for i in range(1, N+1):
    x = input().rstrip()
    dict[i] = x
    dict[x] = i
    
for j in range(M):
    qst = input().rstrip()
    
    if qst.isdigit():
        print(dict[int(qst)])
    else:
        print(dict[qst])