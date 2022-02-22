# 생성자
# 앞서 만든 FourCal1 클래스는 항상 setdata 메서드를 호출하여 초기값을 설정하여야 한다.
# 이렇게 객체에 초깃값을 설정해야 할 필요가 있을 때는 setdata 같은 메서드를 호출하는
# 방법보다 생성자를 구현하는 것이 안전한 방법
# 생성자 (Constructor)란 객체가 생성 도리때 자동으로 호출되는 메서드를 의미한다. 자동 호출의 의미를 파악하자

# Python 메서드 이름으로 __init__ 을 사용하면 이 메서드는 생성자가 된다.

class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result =self.first + self.second
        return result        
    def sub(self):
        result =self.first - self.second
        return result
    def mul(self):
        result =self.first * self.second
        return result
    def div(self):
        result =self.first / self.second
        return result

a=FourCal(4, 2)
print (a.add(),a.sub(),a.mul(),a.div())
# 확실히 편하다.
# __init__ 생성자를 사용하기 전에는
# a = FourCal() 객체를 지정
# a.setdata(4,2) 메서드를 따로 생성해서 객체 변수 지정
# a.add 메서드 호출
# 그러나 생성자를 사용하면
# a = FourCal(4,2) 역시나 self 는 객체 a 자기 자신으로 생략.
# a.add 메서드 호출. 훨씬 더 간단 간편. Good~

# 클래스의 상속 (Ingeritance).
# 어떤 클래스를 만들 때 다른 클래스의 기능을 물려받을 수 있게 만드는 것.
# FourCal 클래스에 a^b 기능을 추가한 MoreFourCal 클래스
print("*"*30) #줄바꿈
# 상속 받을 class 를 정의 해준다.
class MoreFourCal(FourCal):
    def div(self):
        if self.second == 0 :
            return 0
        else :
            return self.first / self.second
    def pow(self): # 기존 FourCal 클래스를 상속 받고 추가로 pow 메서드까지 추가했다.
        result = self.first ** self.second
        return result
b = MoreFourCal (6, 0)
print(b.add(),b.sub(),b.mul(),b.div(),b.pow())

# MoreFourCal 클래스가 FourCal 클래스를 상속 한것을 확인.

# 왜 상속을 해야할까 ?
# 보통 상속은 기존 클래스를 변경하지 않고 기능을 추가하거나 기존 기능을 변경하려고 할 때 사용.
# 그럼 왜 기존 클래스를 수정하지 않나 ? 기존 클래스가 라이브러리 형태로 제공되거나 수정이 허용되지 않는 상황에는 상속.

# 클래스 오버라이딩
# a = FourCal(4, 0)을 입력 했다면, 4 / 0 이 연산되어 오류가 발생한다.
# 따라서 상속한 MoreFourCal 클래스 에서는 div 메서드를 수정 할 수 있다. 
# 동일 한 div 메서드를 호출 시키면 부모 클래스의 메서 대신 오버라이딩한 메서드가 호출된다.
# 즉 부모클래스에 속한 메서드를 수정 변경 하여 사용할때 사용 한다.
print("*"*30) #줄바꿈
# 클래스 변수
# 객체변수는 다른 객체들에 영향을 받지 않고 독립적으로 그 값을 유지다는 점을 이미 알아보았다.
# 이번에는 객체변수와는 성격이 다른 클래스 변수에 대해 알아 본다.

class Family:
    lastname = "김"

# Family 클래스에서 선언한 lastname이 바로 클래스 변수이다. 클래스 변수는 클래스 안에 함수를 선언하는 것과
# 마찬 가지로 클래스 안에 선언하여 생성한다. 
# 그냥 클래스 안에 변수 선언.
print (Family.lastname) # 클래스 변수는 클래스이름.클래스 변수로 사용 가능하다
# 객체를 통해서 클래스 변수를 사용할 수 있다.

aaa = Family()
bbb = Family()
# 각각의 객체에 Family 클래스 정정.
print(aaa.lastname)
print(bbb.lastname)
# 결과 값은 클래스이름. 클래스 변수로 호출 한 값과 동일.
# 그럼 여기서 객체 변수를 변경한다면 ?
Family.lastname = "박"
print (Family.lastname)
print(aaa.lastname)
print(bbb.lastname)
# 김에서 박으로 변경된 값이 출력되는 것을 확인. 
# 이로써 클래스 변수는 같은 클래스를 사용하는 모든 객체에서 동일한 값을 갖는다.
# id 함수를 사용하여 더 명확히 보면
print (id(Family.lastname))
print(id(aaa.lastname))
print(id(bbb.lastname))
# 같은 id 번호 값을 갖는것을 확인. 모두 같은 메모리를 가리키고 있다.
# 클래스 변수를 가장 늦게 설명하는 이유는 클래스에서 클래스 변수보다는 객체 변수가 훨씬 중요하기 때문.
