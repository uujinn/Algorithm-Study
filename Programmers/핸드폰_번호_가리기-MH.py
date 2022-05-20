def solution(phone_number):
    boho = len(phone_number) - 4
    return '*' * boho + phone_number[boho:]

print(solution("01033334444"))