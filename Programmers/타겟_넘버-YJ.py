def solution(numbers, target):
    result = [0]  # [0, 0-a, 0+a, 0-a-b]

    for i in range(len(numbers)):
        tmp = []

        for j in range(len(result)):  # 한칸씩 밀려서 더한 값 append
            tmp.append(result[j] - numbers[i])
            tmp.append(result[j] + numbers[i])
        result = tmp

    return result.count(target)
