from collections import deque
import bisect
import sys

input = sys.stdin.readline

if __name__ == "__main__":
    T = int(input())

    result = []

    for _ in range(0, T):
        k = int(input())
        deq = deque()
        dict = {}
        for _ in range(0, k):
            tmp = input().strip().split()
            command = tmp[0]
            value = int(tmp[1])

            if command == 'I':
                if dict.get(value, -1) == -1:
                    dict[value] = 1
                    bisect.insort_left(deq, value)
                else:
                    dict[value] += 1
            elif command == 'D':
                if not deq:
                    pass
                else:
                    if value == 1:
                        if dict.get(deq[-1], -1) == 1:
                            dict.pop(deq[-1])
                            deq.pop()
                        else:
                            dict[deq[-1]] -= 1
                    elif value == -1:
                        if dict.get(deq[0], -1) == 1:
                            dict.pop(deq[0])
                            deq.popleft()
                        else:
                            dict[deq[0]] -= 1
        if len(dict) == 0:
            result.append("EMPTY")
        else:
            result.append(str(deq[-1]) + ' ' + str(deq[0]))

    for i in result:
        print(i)