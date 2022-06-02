N = int(input())
answer = 1

for i in range(2, N+1):
    answer *= i

answer = reversed(str(answer))
for i in answer:
    if i != '0':
        print(i)
        break
