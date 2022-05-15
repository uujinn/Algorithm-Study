from sys import stdin
def next_prime(n):
    prime = [True] * (2*n+1) #n의 2배 값의 소수를 구한다
    try:
        prime[0] = prime[1] = False
    except:
        return 2 #n==0 일때 예외처리
    for i in range(2, int((2*n)**0.5)+1):
        if prime[i]:
            for j in range(i*2, 2*n+1, i):
                prime[j] = False
    for i in range(n, 2*n+1):
        if prime[i]:
            return i

T = int(stdin.readline())
answers = []
for _ in range(T):
    n = int(stdin.readline())
    print(next_prime(n))