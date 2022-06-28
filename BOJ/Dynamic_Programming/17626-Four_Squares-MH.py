from sys import stdin

n = int(stdin.readline())
minCount = 4

for i in range(int(n ** 0.5), int((n // 4) ** 0.5), -1):
    if i * i == n:
        minCount = 1
        break
    
    temp = n - i * i
    for j in range(int(temp ** 0.5), int((temp // 3) ** 0.5), -1):
        if i * i + j * j == n:
            minCount = min(minCount, 2)
            continue
        
        temp = n - i * i - j * j
        for k in range(int(temp ** 0.5), int((temp // 2) ** 0.5), -1):
            if i * i + j * j + k * k == n:
                minCount = min(minCount, 3)     
        
print(minCount)