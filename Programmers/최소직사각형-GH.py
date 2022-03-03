def solution(sizes):
    for i in sizes: i.sort()
    a, b = sizes[0][0], sizes[0][1]

    for i in sizes:
        if a < i[0]: a = i[0]
        if b < i[1]: b = i[1]

    return a * b