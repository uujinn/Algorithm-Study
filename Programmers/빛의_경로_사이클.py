def solution(grid):
    answer = []
    visited = [[[False] * 4 for _ in range(len(grid[0]))]
               for _ in range(len(grid))]
    moving = {0: (1, 0), 1: (-1, 0), 2: (0, -1), 3: (0, 1)}
    return answer
