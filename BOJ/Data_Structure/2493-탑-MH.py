from sys import stdin

stack = []
num = int(stdin.readline())
tops = list(map(int, stdin.readline().split()))
answer = [0 for i in range(num)]

for i in range(num):
    while stack:
        if stack[-1][1] > tops[i]:
            answer[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()         # 내 앞의 탑보다 내 높이가 더 높으면 앞의 탑 pop (앞의 탑 필요없어짐)
    stack.append([i, tops[i]])

print(*answer)

# 876ms