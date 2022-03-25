import string


def solution(strings, n):
    return sorted(sorted(strings), key=lambda x: x[n])


print(solution(["abce", "abcd", "cdx"], 2))
