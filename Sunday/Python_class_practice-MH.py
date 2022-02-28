class Human:
    def __init__(self, name, age, sex):
        self.name, self.age, self.sex = name, age, sex
    
    def __del__(self):
        print("Bye")

    def who(self):
        print("이름 : {}, 나이 : {}, 성별 : {}".format(self.name, self.age, self.sex))

    def setInfo(self, name, age, sex):       
        self.name, self.age, self.sex = name, age, sex
        
    def sayHi(self):
        print("Hi")
        
        
class Language:
    default_language = "English"
    
    def __init__(self):     # 인스턴스 메소드 생성 : 인자로 self 키워드 사용
        self.show = "My language is " + self.default_language
    
    @classmethod            # 클래스 메소드 생성 : 인스턴스(객체)화 하지 않고 메소드 호출 가능, but 다른 메소드 및 클래스 속성에 접근할 수 있음
    def class_my_language(cls):     # 인스턴스 메소드(일반적인 함수)가 인자로 self 키워드 사용하는 반면, 클래스 메소드는 cls 키워드 사용
        return cls()                
    
    @staticmethod           # 정적 메소드 생성 : 객체화 하지 않고 메소드 호출 가능, 인스턴스를 통해서도 호출 가능
    def static_my_language():       # 인스턴스나 클래스를 인자로 받지 않음
        return Language()
    
    def print_language(self):
        print(self.show)
        
        
class KoreanLanguage(Language):
    default_language = "Korean"
        

# minhee = Human("minhee", 15, "female")
# minhee.setInfo("minhee", 20, "male")
# minhee.who()
# minhee.sayHi()

# del(minhee)

cl = KoreanLanguage.class_my_language()
st = KoreanLanguage.static_my_language()

cl.print_language()
st.print_language()