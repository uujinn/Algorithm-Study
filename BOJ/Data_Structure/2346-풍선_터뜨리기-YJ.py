from sys import stdin
from collections import deque

N = int(stdin.readline())
q = deque(enumerate(map(int, stdin.readline().split()))) 

answer = ""

while q:
    index, paper = q.popleft()
    answer += str(index + 1) + " " # 인덱스이므로 + 1

    if paper > 0 :
        q.rotate(-paper + 1)
    else:
        q.rotate(-paper)

print(answer)