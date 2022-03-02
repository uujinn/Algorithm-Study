def solution(a, b):
    months = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    days = ("SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT")
    standard = 4
    for m in range(a-1):
        standard = months[m] % 7 + standard 
        standard -= 7 if standard >= 7 else 0
    b %= 7
    return days[b + standard if b + standard < 7 else b + standard - 7]
    
print(solution(5, 24))