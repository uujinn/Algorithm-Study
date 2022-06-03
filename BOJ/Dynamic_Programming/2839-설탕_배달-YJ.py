N = int(input())

x = 3
y = 5

max_i = N // 3
answer = []
cnt = 0

for i in range(max_i):
    left_value = N - i * 3
    if (left_value % y == 0):
        j = left_value / y
        cnt = i + j
    elif (left_value == x):
        cnt = i + 1

    if cnt != 0:
        answer.append(int(cnt))


if len(answer) == 0:
    print(-1)
else:
    print(min(answer))
