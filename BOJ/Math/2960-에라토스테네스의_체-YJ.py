N, K = map(int, input().split())
check = [False for _ in range(N+1)]
answer = 0

for i in range(2, N+1):
    tmp = i
    while tmp < N+1:
        if check[tmp] == False:
            check[tmp] = True
            K -= 1
            if not K:
                answer = tmp
                break
        tmp += i  # 배수
    if answer:
        break
print(answer)
