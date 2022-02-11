from sys import stdin
N = int(stdin.readline())
towers = list(map(int, stdin.readline().split()))
maximum = towers[0]

for i, tower in enumerate(towers):
    if tower >= maximum:
        maximum = tower
        print(0, "", end="")
    elif tower < towers[i-1]:
        print(i, "", end="")
    elif tower < maximum:
        print(towers.index(maximum)+1, "", end="")