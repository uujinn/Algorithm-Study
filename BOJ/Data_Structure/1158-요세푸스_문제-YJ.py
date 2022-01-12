import sys
from collections import deque

s = sys.stdin.readline()
N, K = map(int, s.split())

# 원형 큐 사용
queue = deque([])
answer = []

for i in range(1, N+1):
    queue.append(i)

for i in range(1, N+1):
    # 원형으로 앉아있으면 K+1씩 땡겨서 앉음 (0번째 자리로 kill 해야하는 숫자가 올 수 있게)
    queue.rotate(-K+1)
    # 0번째 자리 숫자 kill
    answer.append(str(queue.popleft()))

print('<'+", ".join(answer)+'>')