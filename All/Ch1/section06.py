# List comprehension [ 복 습 ]

l = [x for x in range(1, 100) if x % 2 == 0]
print(l)

# SEction06
# 파이썬 함수 식 및 람다(lambda)

# 함수는 하나의 기능만 하도록 하는 것이 좋다.
# 함수 정의 방법
# def function_name(parameter):
#   code

# 함수 호출
# function_name(parameter)

# 함수 선언 위치 중요 !

# 예제1


def hello(world):
    print("Hello", world)


hello("python")  # Hello python 출력
hello(777)  # Hello 777

# 파이썬은 위에서 아래로 한줄씩 인터프리터 되기 때문에 함수 선언이 먼저 선행되고
# 출력문이 나중에 나와야 오류가 없다.

# 예제2


def hello_return(world):
    val = "Hello" + str(world)
    return val


print(hello_return("Python"))  # HelloPython

# 예제3 (다중리턴) # 파이썬에서 함수를 짜임새 있게 사용 할 수 있음.


def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3


val1, val2, val3 = func_mul(100)
print(val1, val2, val3)  # 10000 20000 30000
# <class 'int'> <class 'int'> <class 'int'>
print(type(val1), type(val2), type(val3))

# 예제4 (다중리턴) # 리스트로 받을 때


def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]  # (y1, y2, y3)


lt = func_mul(100)
print(lt)  # [10000, 20000, 30000]
# 튜플로도 가능하다

# 예제5
# *args, *kwargs


def args_func(*args):  # 가변 매개변수 매개 변수가 몇개인지 모를때, 혹은 다중 매개변수를 받아야 할때
    for i, v in enumerate(args):
        print(i, v)


# args_func("kim") # ('kim',)
# args_func("kim","park") # ('kim', 'park')
args_func("kim", "park", "Lee")
# 0 kim
# 1 park
# 2 Lee

# *kwargs
# * 1개일때는 튜플로 받는데, * 2개일때는 딕셔너리로 받는다


def kwargs_func(**kwargs):
    print(kwargs)


kwargs_func(name1="kim", name2="park")
# {'name1': 'kim', 'name2': 'park'}


def kwargs_func(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


kwargs_func(name1="kim", name2="park")
# name1 kim
# name2 park


# 전체 혼합
def example_mul(arg1, arg2, *args, **kwargs):  # arg1, arg2 필수 입력 인자
    # *args와 **kwargs는 가변 매개 변수
    print(arg1, arg2, args, kwargs)


example_mul(10, 20)  # 10 20 () {}
example_mul(10, 20, "park", "kim", age1=24, age2=35)
# 10 20 ('park', 'kim') {'age1': 24, 'age2': 35}


# 중첩함수 (클로저)
# 함수 안에 함수가 있는 것
def nested_func(num):
    def func_in_func(num):  # 처음 입력 받은 num을 그대로 이어받음
        print(num)
    print("in func")
    func_in_func(num+10000)


nested_func(10000)
# in func
# 20000

# 이건 for나 if 문 처럼 줄의 순서대로 진행 되는 것이 아님
# 함수안에서만 순서대로 진행이 되는 것을 이해해야 한다.
# 1. nested_func(10000)입력 되면 nested_func함수 parameter num에 10000이 입력 된다.
# 2. nested_func함수의 코드 print("in func")가 수행 된다.
# 3. nested_func함수의 코드 func_in_func(num+10000)가 수행 되며
# 함수 안에 함수인 func_in_func에 입력받은 (10000+10000)이 parameter로 입력 된다.
# 4. func_in_func의 코드 print(num)이 수행되면서 20000이 출력된다.

# closer와 decorator는 따로 시간 내서 공부하기


# 예제 6
# Hint 힌트
# 가독성을 높이기 위한 정보를 주는 기능
# Hint가 상이해도 error 가 발생 되지는 않는다. 가이드 느낌
def func_mul3(x: int):  # -> list : 인데 글자 색이 이상해진다.
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]


print(func_mul3(10))
# [1000, 2000, 3000]


# 람다식 예제
# 람다식 : 메모리 절약, 가독성, 간결한 코드
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(heap 초기화) -> 메모리 초기화

# 일반적 함수 -> 변수 할당
def mul_10(num: int) -> int:
    return num * 10


print(mul_10)  # <function mul_10 at 0x000001DA236EACA0>
var_func = mul_10
print(var_func)  # <function mul_10 at 0x000001DA236EACA0>
print(type(var_func))  # <class 'function'>
# var_func에 함수를 할당하고 메모리를 할당
print(var_func(10))  # 100


def lambda_mul_10(num): return num * 10


print(type(lambda_mul_10))  # <class 'function'>
print(lambda_mul_10)  # <function <lambda> at 0x00000233F85DAD30>
print(lambda_mul_10(10))  # 100


def fun_final(x, y, func):  # 매개 변수로 함수도 받을 수 있다.
    return print(x * y * func(10))


fun_final(10, 10, lambda_mul_10)  # 10000

fun_final(10, 10, lambda x: x * 100)  # 100000
# 람다함수를 즉석에서 매개변수로 입력 할 수 있는 장점
# 함수로 매개 변수로 넘길 때 람다 함수를 많이 사용. 한 번 실행 할 경우에..
# fun_final 함수에서 func(10)을 고정으로 입력 해주고 있다.
# 따라서 10 * 10 * (10 *100) 의 결과값으로 100000 출력
