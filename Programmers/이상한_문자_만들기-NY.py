def solution(string):
    answer = ""
    idx = 0
    for s in string:
        if s == " ": idx = 0
        else:
            if idx % 2 == 0: s = s.upper()
            else: s = s.lower()
            idx += 1
        answer += s
    return answer