# 클래스를 만들기 전 어떻게 만들지 먼저 구상하자
# 클래스는 무작정 만드는 것보다 클래스로 만든 객체를 중심으로 어떤 식으로 동작하게 할 것인지 미리 구상을 한 후에
# 생각한 것들을 하나씩 해결해 완성해 나가는 것이 좋다.

# 사칙연산 가능하게 하는 FourCal 클래스가 다음 처럼 동작한다고 가정해보자
# a = FourCal() 으로 a라는 개체를 먼저 생성한다.
# a.setdata(4, 2)로 숫자 를 a 객체 안에 지정해준다.
# a.add()를 실행하면 4 + 2 를 돌려주고
# a.sub()를 실행하면 4 - 2 를 돌려주고
# a.mul()를 실행하면 4 * 2 를 돌려주고
# a.div()를 실행하면 4 / 2 를 돌려 주게한다.
# 이렇게 동작하는 클래스를 만드는 것이 목표!!!!!!!!!!!!!!!! 구상 끝
print("*"*30) # 줄바꿈
# 제일 먼저 할 일은 a = FourCal()처럼 객체를 만들 수 있게 하는 일.
# class FourCal:
#     pass # 임시로 코드를 작성 할 때 주로 사용한다.
# 클래스가 생성 되었으니 우리는 객체를 만들 수 있다.
# a = FourCal()
# print(type(a)) # <class '__main__.FourCal'>
# 객체 a는 FourCal의 객체임을 알 수 있다.

# 객체에 숫자 지정할 수 있게 만들기
# 하지만 생성 된 객체 a는 아직 아무런 기능도 하지 못한다. 이제 더하기 나누기, 곱하기 ,빼기 
# 등의 기능을 하는 객체를만들어야 한다.
# 이런 기능을 갖춘 객체를 만들려면 우선 a 객체에 사칙연산을 할 때 사용 할 때 사용할 2개의 숫자를 먼저 알려주어야한다.
# 다음과 같이 연산을 수행할 대상 (4 ,2)를 객체에 지정할수 있게 만들어보자
# a.setdata(4, 2)
# 위 문장을 수행하려면 다음과 같이 소스 코드를 작성해야 한다.

class FourCal:
    def setdata(self, first, second): # 메서드의 매개변수
        self.first = first            # 메서드의 수행문 1  
        self.second = second          # 메서드의 수행문 2
# 앞서 만든 FourCal 클래스에 pass 문장을 삭제하고 그 대신 setdata 함수를 만들었다.
# 클래스 안에 구현 된 함수는 다른 말로 메서드라고도 부른다.
# 앞으로 클래스 내부의 함수는 항상 메서드라고 표현.

# 일반적 함수의 형식

# def 함수명 (매개변수):
    # 수행할 문장
    # ...
    
# 메서드도 클래스에 포함되어 있다는 점만 제외하면 일반 함수와 별 다를 것이 없다.
# setdata 메서드를 다시 보면 다음과 같다.

# setdata 메서드의 매개변수
# setdata 메서드는 매개변수로 self, first, second 3개의 입력값을 받는다. 그런데 일반 함수와는 달리,
# 메서드의 첫 번째 매개변수 self는 특별한 의미를 가진다.

# 다음과 같이 a 객체를 만들고 a 객체를 통해 setdata 메서드를 호출해보자

a = FourCal()
a.setdata(4, 2)
print(a.first) # 4
print(a.second) # 2
# 객체를 통해 클래스의 메서드를 호출하려면 도트(.) 연산자를 사용해야 한다.
# self를 첫 번째 매개변수로 쓰는 이유는 setdata 메서드의 첫번째 매개변수 self 에는 setdata메서드를 호출한
# 객체 a가 자동으로 전달 되기 때문이다.

# def setdata(a, 4, 2) 이런식으로 
# 파이썬메서드의 첫 번째 매개변수 이름은 관례적으로 self를 사용한다. 객체를 호출할 때 호출한 객체 자신이 
# 전달 되기 때문에 self 를 사용한 것이다.
# 그러니까 클래스의 메서드에는 객체 자기 자신이 먼저 전달 되어야 하는데, 이를 위해 self 매개변수를 1번으로 입력해주는 것.

# # 메서드의 또 다른 호출 방법 : 잘 사용되지는 않음
# a = FourCal()
# FourCal.setdata(a, 4, 2) 이렇게 클래스이름.메서드로 호출 할때는 객체 a를 self에 꼭 전달해줘야 한다.

# setdata 메서드의 수행문
# 이제 메서드의 수행문에 대해 알아보자

# def setdata(self, first, second):
#   self.first = first
#   self.second = second

# a.setdata(4, 2)를 호출하면 setdata 메서드의 매개변수 first, second에는 각각 값 4와 2가 전달되어 
# setdata 메서드의 수행문은 다음과 같이 해석된다.
# self.first = 4
# self.second = 2
# 그럼 self는 전달 된 객체 a 이므로, 다음과 같이 해석
# a.first = 4
# a.second = 2
# a.first = 4 문장이 수행되면 a 객체에 "객체변수" first가 생성되고, 값 4가 저장된다.
# 그러니까 객체.객체변수 = 매개변수로 입력된 값.
# * 객체에 생성되는 객체만의 변수를 객체변수라고 부른다.
print("*"*30) # 줄바꿈
# 이번에는 같은 클래스를 사용하는 객체 2개를 생성해본다.
# a = FourCal()은 이미 지정되어있으니까

b=FourCal()
c=FourCal()
# b와 c 2개의 객체를 지정.

b.setdata(4, 2)
c.setdata(3, 7)
print(b.first)  # b.first에는 4가 저장되어 출력
print(c.first)  # c.first에는 3이 저장되어 출력

# 클래스로 만든 객체의 객체 변수는 다른 객체의 객체 변수에 상관없이 독립적인 값을 유지한다.

# id 함수를 사용하면 객체 변수가 독립적인 값을 유지하는 것을 명확히 알수 있다.

print(id(b.first)) # 주소값 1944249395600
print(id(c.first)) # 주소값 1944249395568 서로 다름 확인

# 다시 한번 객체 변수는 그 객체의 고유 값을 저장할 수 있는 공간. 다른 객체들에 영향을 받지 않고,
# 독립적으로 그 값을 유지한다는 점을 꼭 기억하자
print("*"*30) # 줄바꿈
# 더하기 기능 추가하기

#이미 class FourCal을 위의 예제에서 사용 중이므로 새로운 클래스 생성.

class FourCal1: # 클래스는 클래스 이름만 선언
    def setdata(self,first,second):
        self.first = first
        self.second = second

    def add(self): # 여기서는 self 뒤에 매개변수를 지정할 필요 없음 이미 setdata메서드에서 지정 됨
        result = self.first + self.second
        return result
# 이제 클래스의 구조를 이해했으니, 나머지 4칙연산도 추가
    def sub(self):
        result =self.first - self.second
        return result
    def mul(self):
        result =self.first * self.second
        return result
    def div(self):
        result =self.first / self.second
        return result
# 사칙연산 클래스가 모두 완성.

# 객체를 먼저 생성해주고,
aa = FourCal1()
bb = FourCal1()
# 객체에 객체 변수를 setdata 메서드를 이용하여 지정
aa.setdata(3,5)
bb.setdata(4,6)
# 자이제 각각의 계산결과 출력
print(aa.add(),aa.sub(),aa.mul(),aa.div())
print(bb.add(),bb.sub(),bb.mul(),bb.div())


