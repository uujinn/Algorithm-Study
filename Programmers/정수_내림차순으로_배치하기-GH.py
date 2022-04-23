def solution(n):
    answer = list(sorted(map(int, str(n)), reverse=True))
    return int("".join(map(str, answer)))