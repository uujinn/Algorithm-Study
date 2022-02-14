from sys import stdin
N = int(stdin.readline())
circles = []
stack = []
for _ in range(N):
    circles.append(list(map(int, stdin.readline().split())))
    
for circle in sorted(circles, key=lambda circle: circle[1] ,reverse=True):
    if not stack: stack.append(circle)
    else:
        before = stack.pop()
        x_diff = abs(circle[0] - before[0]) 
        if circle[1] + before[1] < x_diff or abs(circle[1] - before[1]) > x_diff or x_diff == 0:
            stack.append(circle)
        else:
            print("NO")
            exit()

print("YES")