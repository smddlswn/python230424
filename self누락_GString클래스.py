#전역변수
str = "Not Class Member"

#클래스정의
class GString:
    def __init__(self):
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        #버그포인트
        print(self.str)

#인스턴스생성
g = GString()
g.set("First Message")
g.print()
