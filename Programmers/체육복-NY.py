def solution(n, lost, reserve):
    lost = sorted(lost)
    reserve = sorted(reserve)
    for r in reserve[::-1]:
        if not lost: break
        else:
            if lost[-1] == r or lost[-1] + 1 == r or lost[-1] - 1 == r:
                lost.pop()
    return n - len(lost)

print(solution(5, [1,2,4,5], [2, 3, 4]))