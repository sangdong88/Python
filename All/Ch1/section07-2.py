# Section07-2
# 파이썬 클래스 상세 이해
# 상속, 다중상속

# 상속기본
# 부모클래스 = 슈퍼클래스, 서브클래스 = 자식클래스 -> 모든 속성, 메소드 사용 가능

# 상속의 이유
# 상속을 통해서 코딩을 하면 코드를 재사용 할 수 있고 중복을 방지 할 수 있다.
# 이는 가독성을 높여 준다.

# 라면 -> 속성(종류, 회사, 맛, 면종류, 이름) : 부모클래스에서 생성 공통 속성이니까
# 나머지는 자식클래스에서 구현한다면 라면마다 클래스를 생성하는 것보다는
# 하나의 클래스에서 공통 속성을 제공하고 서브클래스에서 사용하면 코드를 줄일 수 있따.

# 예제1

class Car:
    """parent Class"""  # 주석 처럼 쓰이는 건가? PEP 원칙 엄밀히 말하면 주석은아니고 문자열, 클래스 이름 정의

    def __init__(self, tp, color):
        self.type = tp
        self.color = color

    def show(self):
        return 'Car Class "Show" Method!'


a1 = Car("SUV", "Red")
print(a1)  # <__main__.Car object at 0x000001CDB03A0EB0>
print(a1.show())  # Car Class "Show" Method! 이건 a1 인스턴스의 인스턴스 함수를 호출
print(a1.color)  # 인스턴스 변수를 호출 할때는 뒤에 괄호는 생략
print(a1.type)  # 변수니까 변수이름만 입력 하면 되는 걸로 간단히 이해
print(a1.__dict__)  # {'type': 'SUV', 'color': 'Red'}
print()


class BmwCar(Car):  # 제조사마다 차 이름이 다르기 때문에 car_name 속성 추가
    """Sub class"""

    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)  # tp와 color는 부모 클래스를 호출해서 사용해야 하기 때문에
        # super() 부모클래스를 사용하여 호출한다.
        self.car_name = car_name

    def show_model(self):
        return 'your Car name : %s' % self.car_name


b1 = BmwCar("AMG", "Sedan", "White")
print(b1.show())  # Car Class "Show" Method! 부모클래스의 메소드 show도 출력 확인
print(b1.car_name)  # AMG
print(b1.type)  # Sedan
print(b1.color)  # White
print(b1.show_model())  # your Car name : AMG 자식클래스 Bmw의 show_model 메소드도 출력 확인
print(b1.__dict__)  # {'type': 'Sedan', 'color': 'White', 'car_name': 'AMG'}
# b1 인스턴스 네임스페이스 안에 내용이 들어 있는지도 확인


class BenzCar(Car):
    """Sub Class"""

    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name

    def show(self):
        print(super().show())  # 부모의 것도 호출하고 싶을 때_
        return "Car Info: %s %s %s" % (self.car_name, self.color, self.type)

    def show_model(self):
        return 'Your Car name : %s' % self.car_name


print()
# 일반 사용
model1 = BmwCar('520d', 'sedan', 'red')

print(model1.color)  # red # Super # 부모 클래스 상속
print(model1.type)  # sedan # Super # 부모 클래스 상속
print(model1.car_name)  # 520d # Sub # 자식 클래스의 인스턴스 변수
print(model1.show())  # Car Class "Show" Method! # Super # 부모클래스 상속
print(model1.show_model())  # your Car name : 520d # Sub # 자식클래스 메소드


# Method Overriding
model2 = BenzCar("220d", "suv", "black")
print(model2.show())  # Car Info: 220d black suv
print(model2.show_model())  # Your Car name : 220d
# 부모클래스의 show()메소드는
#  def show(self):
#      return 'Car Class "Show" Method!' 이지만
# 자식클래스 BenCar에서
# def show(self):
# super().show()
# return "Car Info: %s %s %s" %(self.car_name, self.color, self.type)
# super() 함수로 기존의 show()메소드를 상속받은 후에
# return 결과값을 변경하였다. Overriding 덮어 쓰기
print()

# parent Method 호출 : super().메서드 print
model3 = BenzCar("350s", "sedan", 'silver')
print(model3.show())
# Car Class "Show" Method! # 부모의 show()
# Car Info: 350s silver sedan # 자식의 show() 가 함께 호출


# Inheritance Info
print('Inheritance Info : ', BmwCar.mro())
# [<class '__main__.BmwCar'>, <class '__main__.Car'>, <class 'object'>]
# 왼쪽에서 오른 쪽으로 보면 상속관계 오른쪽으로 갈수록 부모, 모든클래스는 object 클래스
# object가 모든 class의 부모다.
print('Inheritance Info : ', BenzCar.mro())
# [<class '__main__.BenzCar'>, <class '__main__.Car'>, <class 'object'>]


# 예제2
# 다중 상속
# 복잡한 다중 상속은 해석이 어려울 수 있다.
# 보통 2개 정도 까지만 사용
# A는 전자, B는 화학 계통의 클래스를 상속받아서 새로운 것을 만들 수 있는데
# 상속이 너무 많다 보면, class를 찾기가 어렵다.
class X(object):  # 모든 클래스는 object를 상속 받는다 괄호는 있어도 되고 없어도 되고
    pass


class Y():
    pass


class Z():
    pass


class A(X, Y):
    pass


class B(Y, Z):
    pass


class M(B, A, Z):
    pass


print(A.mro())
# [<class '__main__.A'>, <class '__main__.X'>, <class '__main__.Y'>, <class 'object'>]
print(M.mro())
# [<class '__main__.M'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.X'>, <class '__main__.Y'>, <class '__main__.Z'>, <class 'object'>]


# 연습
class Sid:
    def __init__(self, name, num, score):  # 무슨 항목을 입력 받을지를 선택
        self.name = name
        self.num = num
        self.score = score

    def grade(self):
        if self.score >= 80:
            grade = "A학점"
            print(f'{self.num}번 학생의 학점은 : >>>', grade)
        elif self.score >= 60:
            grade = "B학점"
            print(grade)
        elif self.score >= 40:
            grade = "C학점"
            print(grade)
        elif self.score >= 20:
            grade = "D학점"
            print(grade)


stu1 = Sid("LEE", 18, 85)
stu1.grade()  # A학점
# 18번 학생의 학점은 : >>> A학점

print(Sid.mro())  # <built-in method mro of type object at 0x000001E771C2A9D0>
# 상속되지 않음
