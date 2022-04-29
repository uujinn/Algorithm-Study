from sys import stdin

a, b = map(int, stdin.readline().split())

for i in range(b, 0, -1):
    if a % i == 0 and b % i == 0:
        print(i)
        break

i = a    
while True:
    if i % a == 0 and i % b == 0:
        print(i)
        break
    i += 1