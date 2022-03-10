
def solution(n, arr1, arr2):
    answer = []

    for one, two in zip(arr1, arr2):
        value = str(bin(one|two)[2:]) # 앞에 0b 슬라이싱
        value = value.zfill(n) # zfill: 문자열 앞 0으로 채우는 함수
        value = value.replace('1', '#')
        value = value.replace('0', ' ')
        answer.append(value)

    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))