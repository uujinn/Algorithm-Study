def solution(numbers):
    sol = [i for i in range(0, 10)]
    subtract = [a for a in sol if a not in numbers]
    return sum(subtract)
