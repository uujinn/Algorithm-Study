N = int(input())
temp = N
count = 0

while True:
    a = temp // 10
    b = temp % 10
    c = (a + b) % 10
    temp = (b * 10) + c
    count += 1
    if (temp == N):
        break

print(count)