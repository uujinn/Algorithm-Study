def solution(sizes):
    for size in sizes: # 모든 size가 w > h 하게 정렬
        size.sort(reverse = True)

    w = max(s[0] for s in sizes) # w 중 최댓값
    h = max(s[1] for s in sizes) # h 중 최댓값

    return w * h

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]

print(solution(sizes))