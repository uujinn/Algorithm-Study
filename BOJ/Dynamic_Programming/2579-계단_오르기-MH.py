from sys import stdin

n = int(stdin.readline())
w, score = [0] * 301, [0] * 301

for i in range(1, n + 1):
    w[i] = int(stdin.readline())

score[1] = w[1]
score[2] = w[1] + w[2]
for i in range(3, n + 1):
    score[i] = w[i] + max(score[i - 3] + w[i - 1], score[i - 2])
    # 마지막 계단 무조건 밟는다는 가정하에 두 가지 경우만 존재
    # O X O O (max 왼)
    # O O X O (max 오)
    
print(score[n])