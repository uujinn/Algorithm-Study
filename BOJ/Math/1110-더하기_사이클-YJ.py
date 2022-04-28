N = input()
cnt = 0

if int(N) < 10:
    N = '0' + N

original = N  # 이 부분 때문에 계속 틀렸었음

while True:
    if len(N) == 1:
        N = '0' + N
    new = str(int(N[0]) + int(N[1]))
    N = N[-1] + new[-1]
    cnt += 1
    if original == N:
        print(cnt)
        break
