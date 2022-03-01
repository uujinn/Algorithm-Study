import sys
from collections import defaultdict

spicies = defaultdict(int)
num = 0

while True:
    temp = sys.stdin.readline().rstrip()

    if not temp:
        break
    spicies[temp] += 1
    num += 1

spicies = sorted(spicies.items())

for tree, cnt in spicies:
    print("%s %.4f" %(tree, cnt / num * 100)) 