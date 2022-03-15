def solution(a, b):
    week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    answer = sum(days[:a - 1]) + b - 1
    answer %= 7

    return week[answer]