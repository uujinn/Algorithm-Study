from itertools import permutations


def operation(num1, num2, op):
    if op == '+':
        return str(int(num1) + int(num2))
    if op == '-':
        return str(int(num1) - int(num2))
    if op == '*':
        return str(int(num1) * int(num2))


def calculate(exp, perm):
    tmp = []
    for i in exp:
        if i not in perm:
            if len(tmp) > 0 and tmp[-1] not in perm:
                tmp[-1] = tmp[-1] + i
            else:
                tmp.append(i)

    stack = []
    result = []


def solution(exp):
    answer = 0
    operators = ['+', '-', '*']

    return answer