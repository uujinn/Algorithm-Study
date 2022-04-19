from sys import stdin
from collections import defaultdict


def main():
    n, w = map(int, stdin.readline().split())
    degree = defaultdict(int)
    leaf = n - 1
    for _ in range(n - 1):
        u, v = map(int, stdin.readline().split())
        degree[u] += 1
        degree[v] += 1

        if u != 1 and degree[u] == 2:
            leaf -= 1
        if v != 1 and degree[v] == 2:
            leaf -= 1

    print(w / leaf)


if __name__ == "__main__":
    main()