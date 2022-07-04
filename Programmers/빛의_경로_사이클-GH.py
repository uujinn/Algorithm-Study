import sys

sys.setrecursionlimit(10 ** 6)


def out(x, y, d, grid, dic):
    nx = x + dic[d][0]
    ny = y + dic[d][1]

    if nx >= len(grid):
        nx = 0
    elif nx < 0:
        nx = len(grid) - 1

    if ny >= len(grid[0]):
        ny = 0
    elif ny < 0:
        ny = len(grid[0]) - 1

    return nx, ny


def dfs(state, org, route, grid):
    dic = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]}
    x = state[0]
    y = state[1]
    d = state[2]
    visited[d][x][y] = 1

    nx, ny = out(x, y, d, grid, dic)
    value = grid[nx][ny]

    if value == 'R':
        d = (d + 5) % 4

    elif value == 'L':
        d = (d + 7) % 4

    if org[0] == nx and org[1] == ny and org[2] == d:
        answer.append(route)
        return

    if not visited[d][nx][ny]:
        dfs([nx, ny, d], org, route + 1, grid)


def solution(grid):
    global answer, visited

    answer = []
    visited = [[[0] * len(grid[0]) for _ in range(len(grid))] for _ in range(4)]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for d in range(4):
                dfs([i, j, d], [i, j, d], 1, grid)

    return sorted(answer)