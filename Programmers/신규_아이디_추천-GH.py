import re

def solution(new_id):
    answer = ''
    
    # 1. Upper Case -> Lower Case
    # 2. 소문자, 숫자, -, _, . 제외 모두 제거 
    
    answer = re.sub('[^a-z\d\-\_\.]', '', new_id.lower())
    """
    소문자(a-z), 숫자(\d), 하이픈(\-), 언더바(\_), 마침표(\.)
    대괄호 앞에는 ^ 붙여줌
    정규표현식이 일치할 경우 '' <- 빈 문자로 바꿔서 제거함
    """
    
    # 3. 마침표가 2번 이상이면 하나로 치환
    #마침표가 2번 이상 (\.\.+)
    answer = re.sub('\.\.+', ',', answer)
    
    
    # 4. 마침표가 처음이나 끝이라면 제거
    # 마침표가 처음(^\.)이나 끝(\.$)
    answer = re.sub('^\.\.$', '', answer)
    
    # 5. 빈 문자열이라면, a를 대입
    if answer == '':
        answer = 'a'
    
    # 6. 16자 이상이면 뒤에서부터 제거, 제거 후 마침표가 마지막 문자면 마침표 제거
    answer = re.sub('\.$', '', answer[0:15])
          
    # 7. 2자 이하면 마지막 문자 반복
    while len(answer) < 3:
        answer += answer[-1:]
        
    return answer