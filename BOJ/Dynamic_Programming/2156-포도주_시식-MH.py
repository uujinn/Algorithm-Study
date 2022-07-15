from sys import stdin

n = int(stdin.readline())
podoju = [0]
for _ in range(n):
    podoju.append(int(stdin.readline()))
print(podoju)

if n <= 2:
    print(sum(podoju))
else:
    