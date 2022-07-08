from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

def game(y, x):
    global count
    
    # print(y, end=', ')
    # print(x, end=' : ')
    # print(gamePan[y][x])
    
    if y == N - 1 and x == N - 1:
        count += 1
        # print('count : ', end='')
        # print(count)
        return
    
    if gamePan[y][x] == 0:
        return
    
    try:
        # print('right')
        game(y, x + gamePan[y][x])
    except:
        # print('no right')
        pass

    
    try:
        # print('down')
        game(y + gamePan[y][x], x)
    except:
        # print('no down')
        pass
    
    return


N = int(stdin.readline())
gamePan = [[] for _ in range(N)]

for i in range(N):
    gamePan[i] = list(map(int, stdin.readline().split()))
# print(gamePan)

count = 0
game(0, 0)
print(count)