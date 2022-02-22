# 05-1 클래스

# global 변수 는 변수를 전역 변수로 쓰겟다는 의미임.
# 예시
a=0
def tkdehd ():
    global a # global 함수 사용 전에 외부에서 이미 변수가 지정 되어있는것이 스탠다드
    a = 10
    return a

print(tkdehd()) # 10
print(a) # 10
print("*"*30) # 줄바꿈
result = 0

def add(num):
    global result # result라는 변수는 외부에서 지정 된 변수를 함수 내에서도 전역 변수로 사용 하겠다
    result += num
    return result

print(add(3)) # result는 0+3 = 3
print(add(4)) # result는 3+4 = 7
print("*"*30) # 줄바꿈
# 만일 계산기가 2대 필요한 상황이라면 ??
result1 = 0
result2 = 0

def add1(num):
    global result1
    result1 += num
    return print(result1)

def add2(num):
    global result2
    result2 += num
    return print(result2)

add1(3)
add1(4)
add2(3)
add2(7)
print("*"*30) # 줄바꿈

# # 하지만 계산기가 점점 더 많이 필요해진다면 어떻게 해야 될 까 ?
# 그 때마다 전역 변수와 함수를 추가 할 것인가 ? 여기에 빼기나 곱하기 등의 기능을 추가해야 한다면
# 상황은 점점 더 어려워 질 것이다. 클래스를 사용하면 위와 같은 경우를 간단히 해결 할 수 있다.

class Calculator:
    def __init__(self):
        self.result = 0
        
    def add(self,num):
        self.result += num
        return print(self.result)
    #만일 빼기 기능을 추가하고 싶다면
    def sub(self,num):
        self.result-= num
        return print(self.result)


cal1 = Calculator() # 객체 1
cal2 = Calculator() # 객체 2

cal1.add(3)
cal1.add(4)
cal1.sub(2)
cal2.add(3)
cal2.add(7)
cal2.sub(3)
print("*"*30) # 줄바꿈
# 클래스는 과자 틀
# 과자 틀에 의해 만들어진 과자 객체 
# 클래스로 만든 객체에는 중요한 특징 ! 바로 객체마다 고유한 성격을 가진다는 것.
# 동일한 클래스로 만든 객체들은 서로 전혀 영향을 주지 않는다.

# 다음은 파이썬 클래스의 가장 간단한 예이다.
class Cookie:
    pass
aa= Cookie()
bb= Cookie()

print(aa) #<__main__.Cookie object at 0x000001AB1D1549D0>
print(bb) #<__main__.Cookie object at 0x000001AB1D1549A0>
# 이런 결과가 나왔는데 pass 되었고, 출력 할 것이 없으니 Cookie의 객체이며 위치는 어디다라고 알려주는 출력인듯

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

# 제일 먼저 할 일은 a = FourCal()처럼 객체를 만들 수 있게 하는 일.
class FourCal:
    pass # 임시로 코드를 작성 할 때 주로 사용한다.
# 클래스가 생성 되었으니 우리는 객체를 만들 수 있다.
a = FourCal()
print(type(a)) # <class '__main__.FourCal'>
# 객체 a는 FourCal의 객체임을 알 수 있다.




