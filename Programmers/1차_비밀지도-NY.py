def solution(n, arr1, arr2):
    answer = []
    for A1, A2 in zip(arr1, arr2):
        A1 = '0'*(n-len(format(A1, 'b'))) + format(A1, 'b')
        A2 = '0'*(n-len(format(A2, 'b'))) + format(A2, 'b')
        new = ""
        for a1, a2 in zip(A1, A2): 
            if a1=="1" or a2=="1": new += "#"
            elif a1=="0" and a2=="0": new += " "
        answer.append(new)
    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))