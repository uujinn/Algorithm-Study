from sys import stdin

A, B = map(str, stdin.readline().split())
results = []

for i in range(2, 37):
    for j in range(2, 37):
        try:            
            if int(A, i) == int(B, j) and i != j:
                results.append((int(A, i), i, j))
        except:
            continue

if not results:
    print('Impossible')
elif len(results) == 1:
    print(results[0][0], results[0][1], results[0][2])
else:
    print('Multiple')