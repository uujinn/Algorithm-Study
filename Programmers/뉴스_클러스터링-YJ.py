import math


def solution(str1, str2):
    answer = 0
    A = []
    B = []

    for i in range(0, len(str1) - 1):
        element = str1[i:i+2]
        if element.isalpha():
            A.append(element.lower())

    for i in range(0, len(str2) - 1):
        element = str2[i:i+2]
        if element.isalpha():
            B.append(element.lower())

    if len(A) == 0 and len(B) == 0:  # 공집합
        answer = 1
    else:
        cnt = 0
        for i in A:
            if i in B:
                cnt += 1
                B.remove(i)
        answer = cnt/(len(A)+len(B))

    return math.floor(answer*65536)
