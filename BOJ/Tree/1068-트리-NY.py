import sys
sys.setrecursionlimit(int(100000))

def DFS(parents, target):
    parents[target] = None
    for idx, p in enumerate(parents):
        if p is target:
            DFS(parents, idx)

N = int(sys.stdin.readline())
parents = list(map(int, sys.stdin.readline().split()))
target = int(sys.stdin.readline())
count = 0

DFS(parents, target)

for i in range(N):
    if parents[i] != None and i not in parents:
        count += 1

print(count)