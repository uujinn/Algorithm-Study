n = int(input())
arr = list(map(int, input().split()))

cnt = 0
for num in arr:
    check = 1
    for i in range(2, num):
        if num % i == 0:
            check = 0
            break
    if check and num != 1:
        cnt += 1

print(cnt)
