# 예외 처리

# 프포그램을 만들다 보면 수없이 많은 오류를 만나게 된다. 물론 오류가 발생하는 이유는 프로그램이 잘못 동작하는 것을
# 막기 위한 파이썬의 배려이다 . 하지만 때때로 이러한 오류를 무시하고 싶을 때도 있다. 
# 이를 위해 파이썬은 try, except를 사용해서 예외적으로 오류를 처리할 수 있게 해준다.

# 오류는 어떤 때 발생하는가 ?
# 오류를 처리하는 방법을 알기 전에 어떤 상황에서 오류가 발생하는지 알아보자.
# 오타를 입력했을때를 제외한 실제프로그램에서 자주 발생하는 오류를 중심으로 살펴본다.

# 먼저 디렉터리안에 없는 파일을 열러고 시도했을 때 발생하는 오류이다.

# - FileNotFoundError
# f = open ("없는파일.txt","r")
# Traceback (most recent call last):
#   File "D:\coding\Pract\0314 ch5-4.py", line 13, in <module>
#     f = open ("없는파일.txt","r")
# FileNotFoundError: [Errno 2] No such file or directory: '없는파일.txt'

# - ZeroDivisionError
# >>> 4/0
# Traceback (most recent call last):   
#   File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero  

# - IndexError
# >>> a = [1,2,3]
# >>> a[4]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: list index out of range

# 오류 예외 처리 기법

# try, except문
# 다음은 오류 처리를 위한 try, except문의 기본 구조이다.

# try:
#     ....
# except [발생오류 [as 오류 메시지 변수]]:
#     ....

# try 블록 수행 중 오류가 발생하면 except 블록이 수행된다. 하지만 try 블록에서 오류가 발생하지 않는다면
# except 블록은 수행되지 않는다.
# except 구문을 자세히 살펴 보면 [] 괄호 기호를 사용하는데, 이 기호는 괄호 안의 내용을 생략할 수 있다는
# 관례적 표기 법이다.

# Case 1 : try, except만 쓰는 방법

# try:
#     ....
# except:
#     ....
# 이 경우에는 오류 종류에 관계없이 오류가 밸상하면 except 블록을 수행한다.

# Case 2 : 발생 오류만 포함한 except문

# try:
#     ....
# except 발생 오류 :
#     ....
# 이 경우는 오류가 발생했을 때 except문을 미리 정해 놓은 오류 이름과 일치할 때만 except 블록 수행.

# Case 3 : 발생 오류와 오류 메시지 변수 까지 포함한 except 문
# try:
#     ....
# except 발생오류 as e: # 발생 오류에 대한 메시지를 변수 e로 지정
#     ....

# try :
#     4/0
# except ZeroDivisionError as e:
#     print(e)
# #  division by zero 라고 오류 메시지가 출력 된다.

# # try finally
# # try 문에는 finally 절을 사용할 수 있다. finally 절은 try문 수행 도중 예외 발생여부에 상관 없이 항상 수행된다.

# f1 = open("test12.txt","r")
# try:
#     f1.readlines()
# finally:
#     f1.close
# 예외 발생여부와 상관없이 finally 절에서 f1.close()로 열린 파일을 닫을 수 있다. 오류 방지

# 여러개의 오류 처리하기
# try:
#     ...   
# except 발생오류 1 :
#     ...
# except 발생오류 2 :
#     ...

# try:
#     a = [1,2]
#     print (a[4])
#     print(4 / 0)
# except ZeroDivisionError:
#     print("0으로 나눌 수 없습니다.")
# except IndexError:
#     print("인덱싱 할 수 없습니다.")

# 인덱싱 할 수 없습니다. 라는 문구가 출력 된다.
# try 문에서 print(a[4]) 출력문이 먼저 수행 되기 때문에, IndexError만 발생하고 종료 된다.
# 그럼 except 문을 함께 출력 할 수 없을까 ?

# try:
#     print(4 / 0)
#     a = [1,2]
#     print (a[4])
    
# except (ZeroDivisionError, IndexError) as ee:
#     print(ee)
# 2개 이상의 오류를 동일하게 처리하기 위해서는 위와 같이 괄호를 사용하여 함께 묶어 처리하면 된다
# But, 동일하게 처리한다는 것이 동시에 출력 된다는 것은 아닌 것 같다.
# 그냥 except 문을 1개만 쓴다는 뜻의 내용인듯.
# except에서 1개의 오류가 먼저 검출 되면 try문은 종료된다.

# try문에 else 절 사용하기
# else 절은 무엇인가 ? try문에서 오류가 없을 때 실행 할 수 있는 절

# try:
#     ...
# except [발생오류 [as 오류 메시지를 저장할 변수]]:
#     ...
# else: # 오류가 없을 시에 수행된다.
#     ...

# try 문 수행 중 오류가 발생하면 except 절이 수행되고 오류가 없으면 else절이 수행된다.
# 다음은 try 문에 else 절을 활용하는 간단한 예이다.

try:
    age=int(input("나이를 입력하세요 :   "))
except:
    print("입력이 정확하지 않습니다.")
else:
    if age <=18:
        print("미성년자는 출입금지입니다.")
    else: 
        print("Welcome")

# int 함수에 대하여 잠시 헷갈리는 부분. int 함수는 str으로 입력된 숫자들을 int 형으로 변경해주는 함수.
# try 문에 있는 int 함수에 숫자형 data를 제외한 다른 data가 입력되면, int 함수는 error를 출력한다. 
print("*"*30)
# 오류 회피하기
try:
    f12=open("이건없는파일.txt","r")
except FileNotFoundError:
    pass # FileNotFoundError 발생시 pass 사용하여 오류그냥 회피.
    print("@@@@@") # 에러가 발생해도 발생한 에러의 except 절의 하위 항목은 모두 수행되고 종료되는구나..

# 오류 일부러 발생 시키기
# 프로그래밍을 하다 보면 종종 오류를 일부러 발생시켜야 할 경우도 생긴다.
# 파이썬은 raise명령어를 사용해 오류를 강제로 발생시킬 수 있다.
# 예를 들어 Bird 클래스를 상속받는 자식 클래스는 반드시 fly 함수를 구현하도록 만들고 싶은 경우 (강제)

class Bird:
    def fly (self):
        raise NotImplementedError

# NotImplementedError 는 파이썬 내장오류로, 꼭 작성해야 하는 부분이 구현되지 않았을 경우 
# 일부러 오류를 일으키기 위해 사용된다.

# class Eagle(Bird):
#     pass

# eagle = Eagle()
# print(eagle.fly())

# Traceback (most recent call last):
#   File "D:\coding\Pract\0314 ch5-4.py", line 168, in <module>
#     print(eagle.fly())
#   File "D:\coding\Pract\0314 ch5-4.py", line 159, in fly
#     raise NotImplementedError
# NotImplementedError

# 부모 클래스 Bird 의 fly 메서드에서 raise 내장 함수 에러를 사용하였고,
# 자식 클래스 Eagle 에서 fly 메서드를 구현하지 않았기 때문에 NotImplementedError가 발생.
# 상속 받는 클래스에서 함수를 재구현하는 것을 메서드 오버라이딩이라고 부른다.
# raise는 다시 말해 클래스 상속할려면 꼭 메서드 오버라이딩 해서 쓰세요 라는 의미.

class Eagle(Bird):
    def fly(self):
        print("I believe I can fly")
        
eagle = Eagle()
print(eagle.fly())

# 예외 만들기
# 프로그램 수행 도중 특수한 경우에만 예외 처리를 하기 위해서 종종 예외를 만들어서 사용한다.
# 파이썬 내장 클래스인 Exception 클래스를 상속하혀 만들 수 있다.
print("*"*30)
class Myerror(Exception):
    def say_nick(self,nick):
        if nick == "바보" :
            raise Myerror()
        print(nick)
my = Myerror()
# print(my.say_nick("천사"))
# print(my.say_nick("바보"))


# Traceback (most recent call last):
#   File "D:\coding\Pract\0314 ch5-4.py", line 199, in <module>
#     print(my.say_nick("바보"))
#   File "D:\coding\Pract\0314 ch5-4.py", line 196, in say_nick
#     raise Myerror()
# __main__.Myerror

# 이제 예외 처리 기법을 사용하여 Myerro 발생을 예외처리 해보자
try:
    print(my.say_nick("천사"))
    print(my.say_nick("바보"))
except Myerror as e:
    print(e)
# ******************************
# 천사
# None
# None 이 출력되고 Myerror 내용이 출력되지 않는다.
# 오류 메시지를 출력했을 때 오류 메시지가 보이게 하려면, 오류클래스에 다음과 같은 __str__메서드를 구현해야 한다.
# __str__메서드는 print(e) 처럼 오류메시지를 print 문으로 출력 할 경우에 호출되는 메서드이다.
# 

# 기존 클래스
# class Myerror(Exception):
#     def say_nick(self,nick):
#         if nick == "바보" :
#             raise Myerror()
#         print(nick)

class Myerror(Exception):  
    def __str__(self):
        return "허용되지 않는 별명입니다."
# 클래스에 함수를 추가할 때는 원문에 추가하는 것이 아니라, 새롭게 class 함수를 다시 호출
# 그 아래 메서드를 추가 지정하는 방식도 가능하다.
#
try:
    print(my.say_nick("천사"))
    print(my.say_nick("바보"))
except Myerror as e:
    print(e)   

# 천사
# None
# 허용되지 않는 별명입니다. # __str__ 함수가 return 되는 것을 확인.
