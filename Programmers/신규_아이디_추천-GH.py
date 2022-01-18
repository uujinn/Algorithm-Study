import re

def solution(new_id):
    answer = ''
    
    # 1. Upper Case -> Lower Case
    # 2. 소문자, 숫자, -, _, . 제외 모두 제거
    """
    for num in set(answer):
        if (ord(num) > 96 and ord(num) < 123) or\
            (ord(num) > 47 and ord(num) < 58) or\
                ord(num) == 95 or ord(num) == 45 or ord(num) == 46:
                    pass
        else:
            answer = answer.replace(answer[answer.index(num), ""])
    """
    
    answer = re.sub('[^a-z\d\-\_\.]', '', new_id.lower())
    """
    소문자(a-z), 숫자(\d), 하이픈(\-), 언더바(\_), 마침표(\.)
    대괄호 앞에는 ^ 붙여줌
    정규표현식이 일치할 경우 '' <- 빈 문자로 바꿔서 제거함
    """
    
    # 3. 마침표가 2번 이상이면 하나로 치환
    while('..' in answer):
        answer = answer.replace("..", ".")
    """
    마침표가 2번 이상 (\.\.+)
    answer = re.sub('\.\.+', ',', answer)
    """
    
    # 4. 마침표가 처음이나 끝이라면 제거
    answer = answer.strip('.')  
    # .strip([chars]): 인자로 전달된 문자를 String의 좌우에서 제거
    """
    마침표가 처음(^\.)이나 끝(\.$)
    answer = re.sub('^\.\.$', '', answer)
    """
    
    # 5. 빈 문자열이라면, a를 대입
    if answer == '':
        answer = 'a'
    
    # 6. 16자 이상이면 뒤에서부터 제거, 제거 후 마침표가 마지막 문자면 마침표 제거
    if len(answer) > 15:
        answer = answer[:15]
        answer = answer.rstrip('.')
    """
    answer = re.sub('\.$', '', answer[0:15])
    """
        
    # 7. 2자 이하면 마지막 문자 반복
    while len(answer) < 3:
        answer += answer[-1:]
        
    return answer

"""
정규표현식 공부하다가 기 빨려서 포기...
근데 특히 step 2에서 정규표현식 말고 어떻게 했나 궁금해서
다른 답안 참고해서 아스키 코드로 구현한 코드는 또 런타임 에러 남...
뭔가 잘못된 거겠지...
"""