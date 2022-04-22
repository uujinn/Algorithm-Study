from sys import stdin
A, B, C, M = map(int, stdin.readline().split())
time = tired = worked = 0
while time < 24 and tired <= M:
    if tired + A > M:
        tired -= C
        if tired < 0: tired = 0
    else:
        tired += A
        worked += B
    time += 1
print(worked)