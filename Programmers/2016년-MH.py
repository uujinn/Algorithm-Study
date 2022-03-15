def solution(a, b):
    days = 0
    month = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']

    for i in range(a - 1):
        days += month[i + 1]
    days += b

    return week[days % 7 - 1]

print(solution(1, 1))
print(solution(5, 24))