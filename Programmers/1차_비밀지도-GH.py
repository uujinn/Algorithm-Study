def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        # 지도 두 개 합치기
        answer.append(bin(arr1[i] | arr2[i])[2:].zfill(n))
        # 0을 ' '로 바꿈
        answer[i] = answer[i].replace('0', ' ')
        # 1을 '#'으로 바꿈
        answer[i] = answer[i].replace('1', '#')

    return answer