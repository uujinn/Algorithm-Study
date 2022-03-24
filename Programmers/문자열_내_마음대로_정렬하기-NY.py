def solution(strings, n):
    return list(s for s in sorted(sorted(strings), key=lambda x: x[n]))