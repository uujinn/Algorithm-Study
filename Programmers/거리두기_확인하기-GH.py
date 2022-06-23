from collections import deque

dy = [-1, 1, 0, 0] # top, bottom, left, right
dx = [0, 0, -1, 1]

def MenhatenDistance(y1, x1, y2, x2):
    dist = abs(y1-y2) + abs(x1-x2)
    return dist

def bfs(place, y1, x1, y2, x2):
    visit = [[False]*5 for _ in range(5)]
    q = deque()
    q.append((y1, x1, 0))

    while q:
        cur_y, cur_x, cur_dist = q.popleft()

        if cur_y == y2 and cur_x == x2:
            return cur_dist

        for i in range(4):
            nxt_y, nxt_x = cur_y + dy[i], cur_x + dx[i]
            if 0 <= nxt_y < 5 and 0 <= nxt_x < 5:
                nxt = place[nxt_y][nxt_x]
                if nxt != 'X' and visit[nxt_y][nxt_x] == False:
                    q.append((nxt_y, nxt_x, cur_dist + 1))
                    visit[nxt_y][nxt_x] = True
    return 3

def solution(places):
    answer = []
    for pl in places:

        participants = []
        for i in range(5):
            for j in range(5):
                if pl[i][j] == 'P':
                    participants.append((i,j))
        if len(participants) == 0 or len(participants) == 1:
            answer.append(1)
            continue
        flag = 0
        for i in range(5):
            for j in range(5):
                if pl[i][j] == 'P':

                    for par in participants:
                        y, x = par[0], par[1]
                        if i==y and x==j:
                            continue
                        if MenhatenDistance(i, j, y, x) > 2:
                            continue

                        dist = bfs(pl, i, j, y, x)
                        if dist <= 2:
                            flag = 1
                            break
        if flag == 1:
            answer.append(0)
        else:
            answer.append(1)

    return answer