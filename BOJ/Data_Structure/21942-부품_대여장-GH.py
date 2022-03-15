import sys
read = sys.stdin.readline

N, L, F = map(str, read().split())
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
limit = int(L[:3])*24*60 + int(L[4:6])*60 + int(L[7:])
fee = int(F)
rental = {}
overdue = {}

for _ in range(int(N)):
    date, time, item, name = map(str, read().split())
    rental[name] = rental.get(name, {})
    year, month, day = map(int, date.split('-'))
    h, m = map(int, time.split(':'))
    time_id = (sum(month_days[:month]) + day) * 24 * 60 + h * 60 + m

    if rental[name].get(item, 0) == 0:
    # 빌릴 때
    else:
    # 반납할 때

name_sort = sorted(list(overdue))