from sys import stdin
from datetime import datetime
N, L, F = map(str, stdin.readline().split())
rents = {}
fined = {}
N, F = int(N), int(F)
days = int(L.split("/")[0])
hours, minutes = map(int, L.split("/")[1].split(":"))
total_sec = days * 24 * 60 * 60 + hours * 60 * 60 + minutes * 60
for _ in range(N):
    date, time, P, M = map(str, stdin.readline().split())
    if (P, M) in rents:
        return_t = datetime.strptime(date + " " + time, "%Y-%m-%d %H:%M")
        borrow_t = rents[(P,M)]
        
        cnt = int(((return_t - borrow_t).total_seconds() - total_sec)/60 * F)
        
        if cnt > 0:
            if M in fined: fined[M] += cnt
            else: fined[M] = cnt
    else:
        rents[(P, M)] = datetime.strptime(date + " " + time, "%Y-%m-%d %H:%M")
        
if not fined: print(-1)
else:
    for f in sorted(fined.items(), key=lambda x : x[1]):
        print(f[0], f[1])