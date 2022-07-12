def solution(name):
    alpha = [min(ord(i) - ord('A'), ord('Z') - ord(i) + 1) for i in name]
    i, answer = 0, 0

    while True:
        answer += alpha[i]
        alpha[i] = 0

        if sum(alpha) == 0:
            return answer

        left, right = 1, 1

        while alpha[i - left] == 0:
            left += 1
        while alpha[i + right] == 0:
            right += 1

        if right > left:
            answer += left
            i -= left
        else:
            answer += right
            i += right
