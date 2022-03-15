import sys

input = sys.stdin.readline
dict = dict()
cnt = 0

while True:
    str = input().rstrip()
    if not str:
        break
    dict[str] = dict.get(str, 0) +1
    cnt += 1

for i, j in sorted(dict.items()):
    ratio = round(j / cnt * 100, 4)
    print('%s %.4f' % (i, ratio))