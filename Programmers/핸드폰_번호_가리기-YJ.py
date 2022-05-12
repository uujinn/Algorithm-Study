def solution(phone_number):
    len_num = len(phone_number)

    answer = ''
    answer += (len_num - 4) * '*' + phone_number[-4:]
    return answer


print(solution("027778888"))
