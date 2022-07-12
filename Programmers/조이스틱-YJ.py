def solution(name):
    answer = 0
    alpha = [min(ord(i) - ord('A'), ord('Z') - ord(i) + 1) for i in name]

    i = 0

    while True:
        answer += alpha[i]

        if sum(alpha) == 0:  # 남아있는 이동거리의 합
            break

    return answer


print(solution("JEROEN"))
