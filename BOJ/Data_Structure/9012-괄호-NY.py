from sys import stdin
T = int(stdin.readline())
for t in range(T):
    ps = str(stdin.readline().rstrip())
    while '()' in ps:
        ps = ps.replace('()', '')
    if len(ps) == 0: print("YES")
    else: print("NO")