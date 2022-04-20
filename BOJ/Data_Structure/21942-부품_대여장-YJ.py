from collections import defaultdict
from datetime import datetime, timedelta
from sys import stdin
from collections import defaultdict
import math


def getDateTime(day, time):
    year, month, day = map(int, day.split('-'))
    hour, min = map(int, time.split(':'))
    return datetime.datetime(year, month, day, hour, min)


N, L, F = stdin.readline().rstrip().split()


period = timedelta(days=int(L[:3]), hours=int(L[4:6]), minutes=int(L[7:]))
dic, answer = defaultdict(dict), defaultdict(int)


def check_item(user, item):
    for key in dic[user].keys():
        if key == item and dic[user][item] != 0:
            return True
    return False


for _ in range(int(N)):
    string = stdin.readline().rstrip().split()
    day = string[0]
    time = string[1]
    item = string[2]
    user = string[3]

    if not check_item(user, item):
        dic[user][item] = (day, time)
        continue
    # print(dic)

    # 기록 있으면 이제 계산하기
    # 반납 - 대여 datetime
    difference = getDateTime(day, time) - \
        getDateTime(dic[user][item][0], dic[user][item][1])
    min = (difference.total_seconds() - period.total_seconds()) / 60

    # 벌금 계산
    if min > 0:
        answer[user] += math.ceil(min * int(F))
    dic[user][item] = 0

if answer:
    for user in sorted(answer.keys()):  # 사전 순
        print(user, answer[user])
else:
    print(-1)
