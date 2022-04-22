A, B, C, M = map(int, input().split(' '))

fatigue = 0  # 피로도
work = 0  # 일

for _ in range(24):
    if fatigue + A <= M:
        fatigue += A
        work += B
    else:
        if fatigue - C >= 0:
            fatigue -= C
        else:
            fatigue = 0
print(work)
