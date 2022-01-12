from sys import stdin
N,K = map(int, stdin.readline().split())
list_N = [i for i in range(1, N+1)]
list_result = []

i = 0 #현재 인덱스 표시
j = 1 #K번째 사람을 표시 하기 위한 인덱스

#찾은 규칙: 1부터 시작. (만약 K가 3이라면) j가 3일때가 제거해야 할 숫자.
#그래서 j를 1부터 K까지 움직이는 변수로 두었음.
#만약 백준 예시처럼 7, 3 이 들어오면 첫 번째 케이스에서 j=3일때 i=2, 즉 i번째 인덱스 제거
#그럼 다시 j는 1이 되고 i번째 인덱스는 유지된다.
#전체 길이가 0이 될때까지 반복.

while len(list_N)!=0: #길이가 0이 될때까지 반복.
    if j % K == 0: #j%k == 0일때, 즉 k가 3이면 j가 3일때.
        i = i + j - 1
        while i >= len(list_N):
            i -= len(list_N)
        list_result.append(list_N.pop(i))
        j = 1
    else:
        j += 1

print("<", end='')
for i in range(N):
    print(list_result[i], end='')
    if i != N-1:
        print(', ', end='')
print(">")

#실행 시간: 5176ms.. for문 두 번 돌아서 그런가?