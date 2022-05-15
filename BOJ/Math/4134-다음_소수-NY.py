from sys import stdin
def next_prime(n):
    prime = [True] * (2*n+1)
    prime[0] = prime[1] = False
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
    answers.append(next_prime(n))
for a in answers:
    print(a)