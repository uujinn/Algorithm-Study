from sys import stdin
from collections import Counter

books = []
N = int(stdin.readline())

for _ in range(N):
    books.append(stdin.readline().rstrip())
books = Counter(sorted(books))

print(books.most_common()[0][0])