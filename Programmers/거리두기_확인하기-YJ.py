from collections import deque


def solution(places):
    answer = []

    for place in places:
        answer.append(bfs(place))

    return answer


def bfs(place):
    start = []
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                start.append([i, j])  # P에서 시작
    for s in start:
        q = deque([s])
        visited = [[False] * 5 for _ in range(5)]
        distance = [[0] * 5 for _ in range(5)]  # P와 O 사이 거리
        visited[s[0]][s[1]] = True

        while q:
            y, x = q.popleft()
            dx = [-1, 1, 0, 0]  # 상하
            dy = [0, 0, -1, 1]  # 좌우

            for i in range(4):  # 상하좌우
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < 5 and 0 <= ny < 5 and visited[ny][nx] == 0:
                    if place[ny][nx] == 'O':
                        q.append([ny, nx])  # 0 자리 다시 시작점
                        visited[ny][nx] = True
                        distance[ny][nx] = distance[y][x] + 1

                    # P를 발견했고 시작점부터의 거리가 1보다 작거나 같을 경우
                    if place[ny][nx] == 'P' and distance[y][x] <= 1:
                        return 0
    return 1


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP",
      "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
