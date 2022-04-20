def solution(n):
    default = "수박"
    return default * int(n//2) + default[:n%2]
