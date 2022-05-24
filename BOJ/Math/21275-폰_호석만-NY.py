from sys import stdin
A, B = map(str, stdin.readline().split())
A_arr = []
B_arr = []

for i in range(2, 37):
    try: A_arr.append([int(A, i), i])
    except:
        try: B_arr.append([int(B, i), i])
        except: continue

cnt = 0
for a in range(len(A_arr)):
    for b in range(len(B_arr)):
        if A_arr[a][0] == B_arr[b][0] and A_arr[a][0] < 2**63: 
            cnt += 1
            x = [a, A_arr[a][1], B_arr[b][1]]

if cnt == 0: print('Impossible')
elif cnt > 1: print('Multiple')
else: print(A_arr[x[0]][0], x[1], x[2])