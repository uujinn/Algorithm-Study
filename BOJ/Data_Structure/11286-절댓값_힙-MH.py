from sys import stdin
from queue import PriorityQueue

heap = PriorityQueue()
num = int(stdin.readline())

for _ in range(num):
    temp = int(stdin.readline())

    if heap.empty() and temp == 0:
        print(0)
    elif not heap.empty() and temp == 0:
        print(heap.get()[1])
    else:
        heap.put((abs(temp), temp))

# 488ms