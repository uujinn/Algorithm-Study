N = input()
if len(N) == 1: N = "0" + N
new_1 = str(int(N[0]) + int(N[1]))
cycle = 0
new_2 = N[1]
while True:
    if N == new_2:
        print(cycle)
        exit(0)
    new_2 = new_2[-1] + new_1[-1]
    new_1 = str(int(new_2[0]) + int(new_2[1]))
    cycle += 1