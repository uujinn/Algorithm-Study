def print_arr(arr):
    for a in arr:
        for j in a:
            print(j, end='  ')
        print()


def rotate_arr(arr, a, b, c, d):
    rotates = []

    # rotate할 숫자들 찾기
    for i in range(b - 1, d):
        rotates.append(arr[a-1][i])

    for i in range(a, c - 1):
        rotates.append(arr[i][d - 1])

    temp = []
    for i in range(b - 1, d):
        temp.append(arr[c - 1][i])
    rotates.extend((temp))

    temp = []
    for i in range(a, c - 1):
        temp.append(arr[i][b - 1])
    rotates.extend((temp))

    # 찾은 숫자를 오른쪽으로 한 칸씩 rotate
    # rotates = [rotates[-1]] + rotates[:-1]
    print(rotates)
    

    # rotate된 숫자들은 행렬에 넣기
    idx = 0
    for i in range(b - 1, d):
        arr[a - 1][i] = rotates[idx]
        idx += 1

    for i in range(a, c - 1):
        arr[i][d - 1] = rotates[idx]
        idx += 1

    for i in range(d - 1, b, -1):
        arr[c - 1][i] = rotates[idx]
        idx += 1


    for i in range(c - 1, a - 1, -1):
        arr[i][b - 1] = rotates[idx]
        idx += 1
        
        if idx > len(rotates):
            idx = 0


    print_arr(arr)




def solution(rows, columns, queries):
    answer = []
    arr = [[] for _ in range(rows)]

    # 행렬 초기화
    for i in range(rows):
        for j in range(columns):
            arr[i].append(i * rows + j + 1)
    print_arr(arr)

    if len(queries) == 1:
        return [arr[queries[0][0] - 1][queries[0][1] - 1]]




    for q in queries:
        rotate_arr(arr, q[0], q[1], q[2], q[3])

    return answer

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
# print(solution(100,	97, [[1,1,100,97]]))