def solution(rows, columns, queries):
    answer = []
    matrix = [[0 for _ in range(columns+1)] for _ in range(rows+1)]
    num = 1
    for row in range(1, rows + 1):  # matrix setting
        for column in range(1, columns + 1):
            matrix[row][column] = num
            num += 1

    for x1, y1, x2, y2 in queries:
        result = []
        original_point = matrix[x1][y1]
        result.append(matrix[x1][y1])

        for i in range(x1, x2):
            result.append(matrix[i+1][y1])  # 변경한 좌표 추가
            matrix[i][y1] = matrix[i+1][y1]

        for i in range(y1, y2):
            result.append(matrix[x2][i+1])  # 변경한 좌표 추가
            matrix[x2][i] = matrix[x2][i+1]

        for i in range(x2, x1, -1):
            result.append(matrix[i-1][y2])  # 변경한 좌표 추가
            matrix[i][y2] = matrix[i-1][y2]

        for i in range(y2, y1, -1):
            result.append(matrix[x1][i-1])  # 변경한 좌표 추가
            matrix[x1][i] = matrix[x1][i-1]

        matrix[x1][y1+1] = original_point
        answer.append(min(result))
    return answer


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
