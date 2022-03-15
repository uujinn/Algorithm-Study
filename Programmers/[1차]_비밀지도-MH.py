def solution(n, arr1, arr2):
    answer = []
    
    for num1, num2 in zip(arr1, arr2):
        binary = bin(num1 | num2)[2:]       # bin의 연산으로 나오는 앞의 '0b' 슬라이싱으로 제거
        binary = binary.replace('1', '#')
        binary = binary.replace('0', ' ')
        
        while len(binary) < n:
            binary = ' ' + binary
            
        answer.append(binary)
    return answer

print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))