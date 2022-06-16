from sys import stdin

N = int(stdin.readline())
d = [0] * (N + 1)               # 1번쨰 수는 사실 d[1]이 아닌 d[2]

for i in range(2, N + 1):
    d[i] = d[i - 1] + 1         # 전의 결과를 다음 결과에 이용 (10 -> 9 -> 3 -> 1)
    
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
        # d[i] : -1
        # d[i // 3] : 나누어 떨어짐
        
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)

print(d[N])