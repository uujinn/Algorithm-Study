n = int(input())

arr = list(map(int, input().split()))

for i in range(1, min(arr)+1):
    if n == 2:
        if arr[0] % i == 0 and arr[1] % i == 0:
            print(i)
    else:
        if arr[0] % i == 0 and arr[1] % i == 0 and arr[2] % i == 0:
            print(i)
