from sys import stdin
from collections import Counter

input = stdin.readline
trees = []

while True:
    name = input().rstrip()
    if not name:
        break
    trees.append(name)

c = Counter(trees)
trees = sorted(c.items()) # 사전순 정렬

for i in range(len(trees)):
    print(trees[i][0], "{:.4f}".format(100 * trees[i][1]/sum(c.values())))