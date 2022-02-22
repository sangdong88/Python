# Section10
# 파이썬 예외처리의 이해
# 예외는 Error를 의미.
# 코딩 시에는 항상 예외처리를 염두해두고 코딩하자.
# 아무리 코드가 무결점이라도 하드에서 나오는 뜬금없는 오류 들을 완벽하게 처리 할 수 없기 때문


# a = 1, 3, 2, 5, 4, 6 
# print(a)
# print([a]) # [(1, 3, 2, 5, 4, 6)]


# 예외 종류
# 문법적으로 에러가 없지만, 코드 실행(런타임) 프로세스에서 발생하는 예외 처리도 중요
# 문법에서 에러가 나면 IDE 도구에서 linter : 코드 스타일, 문법 체크 역할을 해준다.



# SyntaxError : 잘못된 문법

# print("Test) # SyntaxError: EOL while scanning string literal
# if True # SyntaxError: invalid syntax
# x => y # SyntaxError: invalid syntax



# NameError : 참조 변수 없음

a=10
b=15
# print(c) # NameError: name 'c' is not defined



# ZeroDivisionError : 0 나누기 에러

# print(10/0) # ZeroDivisionError: division by zero


# IndexError : 인덱스 범위를 벗어 났을 때

x = [10,20,30]
# print(x[5]) # IndexError: list index out of range


# KeyError : 없는 key 조회

dic = {'name' : "Kim", "age" : 33, "city" : "seoul"}
# print(dic["hobby"]) # KeyError: 'hobby'
print(dic.get('hobby')) # 딕셔너리 key 확인 할 때는 get 메소드를 사용 할 것을 추천


# AttreibuteError : 모듈, 클래스에 있는 잘못된 속성 사용시에 발생

import time
print(time.time()) # 1617176164.7368734
# print(time.month()) # AttributeError: module 'time' has no attribute 'month'
# 처리가 쉽다. 모듈 위치로 가서 직접 확인이 가능하다.


# ValueError : 참조 값이 없을 때 발생

x = [1, 5, 9]
# print(dir(x))
# x.remove(10) # ValueError: list.remove(x): x not in list
# x.index(10) # ValueError: 10 is not in list



# FileNotFoundError

# f = open("test.txt",'r') # FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'



# TypeError : 서로 다른 Type

x = [1,2]
y = (1,2)
z = "test"
k= 2
# print(x+y) # TypeError: can only concatenate list (not "tuple") to list
# print(z+k) # TypeError: can only concatenate str (not "int") to str




# Summary
# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
# 그 후 런타임 예외 발생 시 예외처리 권장 (EAFP 코딩 스타일)
# 합리적인 방식 선 작업 후 에러 처리




# 예외 처리 기본
# try               에러가 발생 할 가능성이 있는 코드 실행
# except 에러명1:    여러 개 가능(에러 처리)
# except 에러명2: 
# else:             try 블록의 에러가 없을 경우 실행
# finally:          항상 실행


print()
# 예제1

name = ["Kim", "Lee", "park"]

try:
    z = "Kim" # "cho"라고 변수 할당하면 error발생
    x = name.index(z)
    print(f'{name} Found it! {x+1} in name')
except ValueError:
    print("Not found it! - Occured ValueError!")
else: # try에서 오류가 없을 때 실행
    print("ok! else!")


# 어떤 오류가 발생할지 모를때는 
# except: # 모든 Error를 캐치
#     pass


# 예제3

try:
    z = "Kim" # "cho"라고 변수 할당하면 error발생
    x = name.index(z)
    print(f'{name} Found it! {x+1} in name')
except ValueError:
    print("Not found it! - Occured ValueError!")
else: # try에서 오류가 없을 때 실행
    print("ok! else!")
finally: # 항상 실행
    print("finally ok")


print()

# 예제4 파이썬에서 많이 보이는 코딩 종류
# 예외처리는 하지 않지만, 무조건 수행 되는 코딩 패턴
try :
    print('Try')
finally :
    print('OK finally!!!')



try:
    z = "Kim" # "cho"라고 변수 할당하면 error발생
    x = name.index(z)
    print(f'{name} Found it! {x+1} in name')
except ValueError as l:
    print(l)
except IndexError:
    print("Not found it! - Occured IndexError!")
except Exception: # 모든 에러 다 걸러 단, 제일 마지막에 둔다. 제일 처음에 두면 Exception에 무조건 걸려서 error식별 안됨.
    print("Not found it! - Occured ExceptionError!")
else: # try에서 오류가 없을 때 실행
    print("ok! else!")
finally: # 항상 실행
    print("finally ok")

print()
# 예제6
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생 # 고급 프로그래밍

try :
    a = "Oh"
    if a == "kim":
        print("OK 허가")
    else :
        raise ValueError
# a = 'kim' 아니면 Value error 를 발생 시켜라
# else 문의 raise 에서 ValueError를 띄웟기 때문에 except ValueError: 에서 걸리게 되고 문제발생이 출력 된다.
# 사용자가 직접 예외 클래스를 규정을 하여 사용 하는 것.
except ValueError: 
    print("문제발생")
except Exception as f:
    print(f)
else :
    print("ok")