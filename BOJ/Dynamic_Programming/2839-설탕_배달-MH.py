from sys import stdin

def delivery(n, kg):
    global answer
    count = 0
    
    if n >= kg:
        count += (n // kg)
        n %= kg
        
    counts.append(count)
    return n


N = int(stdin.readline())
counts, answer = [], []

a = delivery(delivery(N, 5), 3)
b = delivery(delivery(N, 3), 5)

for i in range(0, len(counts), 2):
    answer.append(counts[i] + counts[i + 1])
    
print(answer)
print(a)
print(b)

if a == 0 and answer[0] <= answer[1]:
    print(answer[0])
elif b == 0 and answer[1] <= answer[0]:
    print(answer[1])
elif a == 0:
    print(answer[0])
elif b == 0:
    print(answer[1])
else:
    print(-1)