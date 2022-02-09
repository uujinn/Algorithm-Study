import enum
from sys import stdin
from turtle import back
brackets = list(str(stdin.readline()))
index_cnt = []
back_cnt = -1

#괄호가 존재하는 인덱스들을 따로 먼저 저장
for i, bracket in enumerate(brackets):
    if bracket == '(': 
        index_cnt.append([i, i])
        back_cnt += 1
    elif bracket == ')': 
        index_cnt[back_cnt][1] = i
        back_cnt -= 1

#해당 인덱스들의 조합 경우의 수 계산

#계산된 경우의 수들 정렬해서 출력