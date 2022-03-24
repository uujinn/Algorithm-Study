def solution(strings, n):
    strings_word = [[] for _ in range(len(strings))]
    for i in range(len(strings)):
        strings_word[i].append(strings[i])
        strings_word[i].append(strings[i][n])
    return list(s[0] for s in sorted(strings_word, key=lambda x: (x[1], x[0])))