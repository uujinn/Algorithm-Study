
def calc(priority, n, expression):

    if n == 2:  # 가장 높은 우선순위
        return str(eval(expression))
    if priority[n] == '*':  # 먼저 쪼갠 애들부터 계산한다.
        res = eval('*'.join([calc(priority, n+1, e)
                   for e in expression.split('*')]))
    if priority[n] == '+':
        res = eval('+'.join([calc(priority, n+1, e)
                   for e in expression.split('+')]))
    if priority[n] == '-':
        res = eval('-'.join([calc(priority, n+1, e)
                   for e in expression.split('-')]))
    return str(res)


def solution(expression):
    answer = 0
    priorities = [
        ('*', '-', '+'),
        ('*', '+', '-'),
        ('+', '*', '-'),
        ('+', '-', '*'),
        ('-', '*', '+'),
        ('-', '+', '*')
    ]

    for priority in priorities:
        res = int(calc(priority, 0, expression))
        answer = max(answer, abs(res))

    return answer
