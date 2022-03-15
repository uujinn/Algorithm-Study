def solution(s):
    l = len(s)
    if l % 2:
        return s[l//2]
    else:
        return s[l//2-1 :l//2+1]

print(solution("qwer"))