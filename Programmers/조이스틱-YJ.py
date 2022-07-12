def solution(name):
    answer = 0
    alpha = [(ord(i) - ord('A'), ord('Z') - ord(i) + 1) for i in name]
    arr = [0] * len(name)

    i = 0

    currentIdx = 0
    rightIdx = 0
    leftIdx = 0

    while True:
        answer += alpha[i]
        rightIdx = 0
        leftIdx = 0

        if sum(alpha) == 0:  # 남아있는 이동거리의 합
            break

    return answer


print(solution("JEROEN"))
