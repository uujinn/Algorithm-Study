def solution(s):
    answer = []
    s = s.replace('{', '[')
    s = s.replace('}', ']')
    s = eval(s)
    s.sort(key=lambda x: len(x))

    for arr in s:
        for i in arr:
            if i not in answer:
                answer.append(i)

    return answer


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
