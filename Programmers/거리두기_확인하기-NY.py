from collections import deque
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(person, place):
    for i, j in person:
        q = deque()
        q.append((i,j))
        visited = [[0] * 5 for _ in range(5)]
        visited[i][j] == 1
        while q:
            x, y = q.popleft()
            for m in range(4):
                nx = x + dx[m]
                ny = y + dy[m]
                if 0<=nx<=4 and 0<=ny<=4 and not visited[nx][ny]:
                    if place[nx][ny] != 'X':
                        visited[nx][ny] = visited[x][y]+1
                        q.append((nx, ny))
                    if place[nx][ny] == 'P':
                        return 0
        return 1
    
def check(place):
    person = []
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                person.append((i,j))
    if len(person) != 0: return 1
    return bfs(person, place)

def solution(places):
    answer = []
    for place in places:
        answer.append(check(place))
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))