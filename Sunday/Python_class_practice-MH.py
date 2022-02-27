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
    
    def __init__(self) -> None:
        self.show = "My language is " + self.default_language
    
    @classmethod
    def class_my_language(cls):
        return cls()
    
    @staticmethod
    def static_my_language():
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