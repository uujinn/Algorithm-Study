def solution(sizes):
    max_sqr = sizes[0]
    for size in sizes: #그리디로 구상. 맥스 값이랑 비교하면서 계속 최대값을 고쳐나가고 마지막 값을 리턴
        if size[0] < size[1]:
            temp = size[0]
            size[0] = size[1]
            size[1] = temp
        if size[0] > max_sqr[0]: max_sqr[0] = size[0]
        if size[1] > max_sqr[1]: max_sqr[1] = size[1]
            
    return max_sqr[0] * max_sqr[1]

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))