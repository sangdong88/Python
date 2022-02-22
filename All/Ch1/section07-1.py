# Section07-1
# 파이썬 클래스 상세 이해
# self, 클래스, 인스턴스 변수

# 객체 지향 언어들
# 클래스 사용이유는 덩치가 커지면 클래스 방식을 이용하여 구조화를 시키고,
# 그 때 일일히 변수 함수 선언을 하면 그 때 마다 일일히 수정하기가 힘들다.
# 복잡한 처리 과정 및 데이터에서 조금 편하게 사용하고자 클래스 코딩을 한다.

# 선언
# class class_name :
#     def xxx():
#         return


# 예제1
class UserInfo:  # 클래스는 첫 글자는 항상 대문자, 단어의 시작은 대문자 # 사용자들 끼리의 규칙
    # 속성, 메소드 2가지가 올수 있다.
    def __init__(self, name):  # 클래스를 최초 구동 할때 초기화 할때 구동 되는 매직메소드 # 초기값 지정의 의미
        self.name = name  # self라는 UserInfo의 인스턴스에  self.name이라는 변수 = name을 입력

    def print_user_info(self):
        print("name", self.name)


# 클래스는 붕어 빵 틀만 만든것
user1 = UserInfo("lee")  # 초기화
user1.print_user_info()
print(user1.name)  # lee
# name lee
user2 = UserInfo("park")
user2.print_user_info()
print(user2.name)  # park
# name park
# user1과 user2는 서로 다르다. name 속성 값도 다르다.
# 네임스페이스 : 인스턴스가 갖고 있는 고유의 저장 공간
# 인스턴스(클래스와 연결된 객체로 할당 하는 것)는 각자의 주소를 갖고 있다.

print(id(user1))
print(id(user2))
# 2603875434448
# 2603875434256

# 클래스를 하나 생성 해서 클래스로 인스턴스화 시켜서 사용하고 있고,
# 인스턴스화 된 객체들은 각자의 네임스페이스를 사용하여 서로 다른 공간에 저장하고 있다.

# 네임 스페이스를 호출하는 매직 메서드 __dict__
print(user1.__dict__)  # {'name': 'lee'}
print(user2.__dict__)  # {'name': 'park'}

# 클래스, 인스턴스 차이 중요
# 클래스를 인스턴스화
# 네임 스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 사용 가능, 객체보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용.
# 클래스는 건물의 설계도라면, 인스턴스는 설계도를 이용하여 지어진 건물이다. 즉, 실제가 있는 것
# 클래스가 지정된 객체가 인스턴스라고 할 수 있다.


# 예제2
# self의 이해
class SelfTest:
    def function1():
        print('function1 called!')

    def function2(self):
        print(id(self))  # 1881979620896
        print('function2 called!')


self_test = SelfTest()
# self_test.fucntion1() # 인스턴스가 function1을 호출하려 하니까 self 인자가 없기 때문에 누구의 function1 함수인지 모름
# 클래스의 메소드가 된다. 클래스로 호출해줘야 한다.SelfTest.function1()
# 인스턴스의 메소드로는 사용할 수 없다. 왜냐면 self가 지정이 안되있어서
SelfTest.function1()  # function1 called! # 클래스 메서드
self_test.function2()  # function1 called! # 인스턴스 메서드

print(id(self_test))  # 1881979620896
# 인스턴스의 고유한 주소는 동일
SelfTest.function2(self_test)  # 클래스 메서드를 사용하고 인자를 인스턴스로
# 1881979620896

# self 가 없으면 클래스 메서드로 사용 된다는 것만 알고 있자.

# 예제3
# 클래스 변수, 인스턴스 변수


class WareHouse:
    # 클래스 변수
    stock_num = 0  # 모든 인스턴스 들이 공유, 중복되는 코드를 줄일 수 있다.

    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1  # user 추가 될때마다 1개씩 추가 왜 ? 공통 클래스 변수 이니까

    def __del__(self):  # 지울 때 호출 되는 매직 메서드 del 인스턴스
        WareHouse.stock_num -= 1


user1 = WareHouse("Kim")
user2 = WareHouse("Park")
user3 = WareHouse("Lee")

print(user1.__dict__)  # {'name': 'Kim'}
print(user2.__dict__)  # {'name': 'Park'}
print(user3.__dict__)  # {'name': 'Lee'}
print(WareHouse.__dict__)  # 클래스 네임 스페이스, 클래스 변수(공유)  stock_num
# {'__module__': '__main__', 'stock_num': 3, '__init__': <function WareHouse.__init__ at 0x000001D42FAFCE50>, '_WareHouse__del': <function WareHouse.__del at 0x000001D42FAFCEE0>, '__dict__': <attribute '__dict__' of 'WareHouse' objects>, '__weakref__': <attribute '__weakref__' of 'WareHouse' objects>, '__doc__': None}


print(user1.name)
print(user2.name)
print(user3.name)

print(user1.stock_num)  # 3
print(user2.stock_num)  # 3
print(user3.stock_num)  # 3
# 자기(인스턴스) 네임스페이스에 없으면 클래스 네임스페이스에 가서 변수를 찾는다. 그래도 없으면 error 중요한 개념.

del user1  # 인스턴스 삭제 # 메모리에서 삭제

print(user2.stock_num)  # 2
print(user3.stock_num)  # 2
