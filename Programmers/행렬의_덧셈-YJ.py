def solution(arr1, arr2):
    answer = []
    len_column, len_row = len(arr1[0]), len(arr1)

    for i in range(len_row):
        arr = []
        for j in range(len_column):
            arr.append(arr1[i][j] + arr2[i][j])
        answer.append(arr)
    return answer
