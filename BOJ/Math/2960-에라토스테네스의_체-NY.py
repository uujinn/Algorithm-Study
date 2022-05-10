from sys import stdin
def exit_func(cnt, j):
    if cnt == K: 
        print(j)
        exit(0)

N, K = map(int, stdin.readline().split())
prime = [True] * (N+1)
prime[0] = prime[1] = False
cnt = 0

for i in range(2, N+1):
    if prime[i]:
        cnt += 1
        exit_func(cnt, i)
        for j in range(i*2, N+1, i):
            if prime[j]: cnt += 1
            prime[j] = False
            exit_func(cnt, j)