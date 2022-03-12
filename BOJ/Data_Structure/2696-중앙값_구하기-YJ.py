import enum
from sys import stdin
from heapq import heappop, heappush

T = int(stdin.readline())

for _ in range(T):
    M = int(stdin.readline())
    a, b = divmod(M, 10) # 몫, 나머지
    
    arr = []
    medians = []
    n = a if not b else a + 1 # M이 10으로 나누어떨어지는 여부 => 차이 O

    for _ in range(n):
        arr.extend(list(map(int, stdin.readline().rstrip().split())))

    left_h = [] # 중앙값 기준 왼쪽 (최대힙)
    right_h = [] # 중앙값 기준 오른쪽 (최소힙)
    # => 왼쪽 오른쪽 길이 비교해서 heappop , 왼쪽에서는 큰수, 오른쪽에서는 작은수 

    print((len(arr) // 2 ) + 1) # 중앙값 개수
    median = arr[0] # 첫번째 중앙값은 무조건 첫번째 값 

    for idx, value in enumerate(arr[1:]):
        if value > median: # 중앙값보다 큰 값은 오른쪽
            heappush(right_h, value)
        else: # 중앙값보다 작은 값은 왼쪽
            heappush(left_h, -value)
        