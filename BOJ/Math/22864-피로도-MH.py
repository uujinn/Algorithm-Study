from sys import stdin

work, fatigue = 0, 0
A, B, C, M = map(int, stdin.readline().split())

for i in range(24):
    if fatigue + A > M:
        fatigue -= C
        if fatigue < 0: fatigue = 0
        continue
        
    fatigue += A
    work += B

print(work)