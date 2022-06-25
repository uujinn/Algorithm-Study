import re
from itertools import permutations


def solution(expression):
    answer = []
    numbers = re.split('\+|\-|\*', expression)  # 숫자
    operations = re.split('[0-9]+', expression)[1:-1]  # 연산자
    print(numbers)
    print(operations)

    for orders in permutations(["+", "-", "*"]):  # 우선순위
        first_operation = orders[0]
        second_operation = orders[1]
        third_operation = orders[2]

    return answer


print(solution("100-200*300-500+20"))
