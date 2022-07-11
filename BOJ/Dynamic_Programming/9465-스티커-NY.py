from sys import stdin

def max_score(stickers, n):
    answer = 0
    for i in range(1, 3):
        for j in range(1, n+1):
            if not stickers[i][j]: continue
            else:
                if max(stickers[i][j-1], stickers[i][j], stickers[i-1][j], stickers[i][j+1], stickers[i+1][j]) == stickers[i][j]:
                    answer += stickers[i][j]
                    stickers[i][j] = stickers[i][j-1] = stickers[i-1][j] = stickers[i][j+1] = stickers[i+1][j] = 0
                else: continue
    for i in range(1, 3):
        for j in range(1, n+1):
            if not stickers[i][j]: answer += stickers[i][j]
    return answer

T = int(stdin.readline())
for _ in range(T):
    n = int(stdin.readline())
    stickers = [[0]*(n+2)]
    for __ in range(2):
        tmp = [0]
        tmp += list(map(int, stdin.readline().split()))
        tmp.append(0)
        stickers.append(tmp)
    stickers += [[0]*(n+2)]
    print(max_score(stickers, n))
