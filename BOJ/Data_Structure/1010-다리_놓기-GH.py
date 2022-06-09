import math, sys

input = sys.stdin.readline
a = input()

s_ = []
e_ = []
for i in range(0, int(a)):
  N, M = map(int, input().split())
  s_.append(N)
  e_.append(M)

for i in range(0, len(s_)):
  print(math.comb(e_[i], s_[i]))