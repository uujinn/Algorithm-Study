def solution(strings, n):
    return sorted(sorted(strings), key=lambda x:x[n])

# 4점 받았어요 히히
# 보자마자 그냥 sorted 기본 기능으로 할 수 있겠는데 ..하고 풀었어요
# 다른 분들도 수월하게 푸셨을거라 생각함당