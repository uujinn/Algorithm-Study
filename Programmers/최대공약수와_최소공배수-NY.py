def GCD(a,b):
    if b == 0: return a
    else: return GCD(b, a%b)

def solution(n, m):
    gcd = GCD(n, m)
    lcm = gcd * (n // gcd) * (m // gcd)
    return [gcd, lcm]