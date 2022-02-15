import sys
circles = []
N = int(sys.stdin.readline())

for _ in range(N):
    x, r = map(int, sys.stdin.readline().split())
    circles.append((x - r, x + r))

circles.sort(key = lambda x: x[0]) # 왼쪽 끝 좌표 기준으로 정렬

for i in range(N-1):
    x1_left, x1_right = circles[i]
    x2_left, x2_right = circles[i+1]
    if x1_left == x2_left or x1_right == x2_right or x2_left < x1_right < x2_right: # 교점 1개거나 2개일 경우
        print('NO')
        sys.exit(0)

print('YES')