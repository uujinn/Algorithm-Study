from collections import deque
from sys import stdin

def printer(documents, M):
    biggest = max(documents)
    count = 0 #몇번째인지
    while True:
        if documents[0] >= biggest: #현재 doc의 중요도가 더 높을때
            count += 1
            if M == 0: return count
            documents.popleft()
            biggest = max(documents)
        else: #현재 doc이 중요도가 더 낮을떄
            documents.rotate(-1)
        
        M = M - 1 if M > 0 else len(documents) - 1

tests = int(stdin.readline())
for _ in range(tests):
    N, M = map(int, stdin.readline().split())
    documents = deque(map(int, stdin.readline().split()))
    print(printer(documents, M))