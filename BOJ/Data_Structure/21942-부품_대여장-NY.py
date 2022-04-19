from sys import stdin
from datetime import datetime
from collections import defaultdict

N, L, F = map(str, stdin.readline().split())
rents = {}
fined = defaultdict(int)
N, F = int(N), int(F)
total_sec = int(L[:3]) * 24 * 60 * 60 + int(L[4:6]) * 60 * 60 + int(L[7:]) * 60

for _ in range(N):
    date, time, P, M = map(str, stdin.readline().split())
    if (P, M) in rents and rents[(P, M)] != 0:
        return_t = datetime.strptime(date + " " + time, "%Y-%m-%d %H:%M")
        borrow_t = rents[(P,M)]

        cnt = int(((return_t - borrow_t).total_seconds() - total_sec)//60 * F)

        if cnt > 0:
            fined[M] += cnt

        rents[(P,M)] = 0 #처음에 생각 못 한 부분. 같은 사람이 같은 물건을 다시 빌리게 될 때를 고려해서 0으로 다시 바꿔야됨
    else:
        rents[(P, M)] = datetime.strptime(date + " " + time, "%Y-%m-%d %H:%M")

if not fined: print(-1)
else:
    for f in sorted(fined.items()):
        print(f[0], f[1]) 