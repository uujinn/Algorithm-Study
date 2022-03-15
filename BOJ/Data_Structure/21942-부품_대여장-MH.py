from sys import stdin
from datetime import timedelta, datetime
from collections import defaultdict
# from dateutil.parser import parse

lend_dict = {}
fine_dict = defaultdict(int)
N, L, F = stdin.readline().rstrip().split()        # 정보의 개수, 대여기간, 벌금
lend_time = timedelta(days=int(L[:3]), hours=int(L[4:6]), minutes=int(L[7:]))   # 대여기간 일, 시간, 분

for _ in range(int(N)):
    day, time, part, member = stdin.readline().rstrip().split()
    date = datetime.strptime(day + ' ' + time, "%Y-%m-%d %H:%M")
    # date = parse(day + ' ' + time)
    
    if lend_dict and (part, member) in lend_dict and lend_dict[(part, member)] != 0:
        period = date - lend_dict[(part, member)] - lend_time
                
        if period.total_seconds() > 0:
            fine_dict[member] += int(period.total_seconds() // 60 * int(F))

        lend_dict[(part, member)] = 0               # 같은 사람이 같은 물건을 여러 번 빌릴 때를 방지
    else:
        lend_dict[(part, member)] = date
    
if fine_dict:   
    for k, v in sorted(fine_dict.items()):
        print(k, end=' ')
        print(v)
else:
    print(-1)