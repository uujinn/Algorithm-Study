from itertools import combinations

def isPrime(size):
    ari = [True] * (size + 1)
    ari[0], ari[1] = False, False
    
    # 1 ~ 1000까지의 아리스토텔레스의 체
    for i in range(2, int(size ** 0.5) + 1):
        if ari[i] == True:
            for j in range(i + i, size + 1, i):
                ari[j] = False
                
    return ari


def solution(nums):
    answer = 0
    # 아리스토 체 생성
    aristo = isPrime(3000)
    
    # 숫자 3개를 조합해서 나오는 것을 출력
    combi = list(combinations(nums, 3))
    
    for case in combi:
        if aristo[sum(case)]:
            answer += 1

    return answer