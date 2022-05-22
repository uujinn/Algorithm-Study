from sys import stdin
def prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

N = int(stdin.readline())
A = list(map(int, stdin.readline().split()))
answer_arr = set()
answer = 1
for a in A:
    if prime(a): answer_arr.add(a)
for a in answer_arr:
    answer *= a
print(answer if answer > 1 else -1)