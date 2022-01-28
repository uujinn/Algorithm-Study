#zip 버전
def solution(absolutes, signs):
    answer = 0
    for num, sign in zip(absolutes, signs):
        answer += num if sign else (-num)
    return answer
  
  #enumerate 버전
  def solution(absolutes, signs):
    answer = 0
    for i, num in enumerate(absolutes):
      answer += num if signs[i] else (-num)
    return answer
