#Hello Universe

# a =1
# while True:
#     print("abc")
#     a += 1
#     print (a)
#     if a == 10 :
#         break       
    
# 04장 함수
def add (a,b):
    return a+b # a,b는 매개변수
c=add(3,2)
print(c)
print(add(3,5)) # 3, 5는 인수

# 일반적인 함수의 예
def sub (a,b):
    result = a+b
    return result
d = sub (3,7)
print(d)

# 입력값이 없는 함수
def say():
    return "HI"
print(say())

# 결과값이 없는 함수
def asd(a,b):
    print(f'{a}더하기{b}는 {a+b}야') # print 문은 단지 수행할 문장이지 asd함수의 결과값이 아니다. 결과값은 오직 return으로만, 결과값은 None으로 표시됨
asd(3,5)
print(asd(4,6))

# 입력값도, 결과값도 없는 함수
def hol():
    print("HI")
hol()

# 매개변수 지정하여 호출하기 // 순서에 상관없이 사용할 수 있다는 장점
def abcd(a,b):
    return a+b
result = abcd (b=6,a=3) # a에 3을 전달, b에 6을 전달 , 순서에 무관.
print (result)

# 입력 값이 몇 개가 될지 모를때는 어떻게 해야 할가 ?
def add_many(*args): # args는 매개변수를 뜻하는 영어단어 arguments의 약자이며, 괄호안에 args만 입력해도 *args로 자동 완성 *뒤에 아무단어나 와도 되나 args로 통일 할 것.
    result=0
    for i in args:
        result += i
    return result
print(add_many(1,2,3,4,5,6))

# *args + 매개 변수의 추가
def add_cal(choice, *args): # 매개변수 choice 추가
    if choice == 'add':
        result = 0
        for i in args:
            result += i
    elif choice == 'mul':
        result = 1
        for i in args:
            result *= i
    return result
print (add_cal('add',1,2,3,4));print(add_cal('mul',1,2,3,4))

# key workd parameter kwargs/ keyword arguments의 약자.
def print_kwargs(**kwargs): # key=value 형태로 입력하면 딕셔너리로 만들어져 출력된다. 이름앞에 **을 붙이면 매개변수는 딕셔너리로.
    return kwargs
print(print_kwargs(a=1,b=3))

# 함수의 결과값은 언제나 하나
def add_and_mul(a,b):
    return a+b, a*b
print(add_and_mul(3,5)) # 결과는 (8, 15) 튜플로 출력 된다.
# 결과를 따로 받고 싶다면
result1, result2 = add_and_mul(3,6)
print(result1);print(result2) 

# 그럼 함수 하나에 2가지 return을 입력 한다면 ?
def add_mul(a,b):
    return a+b
    return a*c
print (add_mul(3,5)) # 결과값은 8만 표시된다 함수는 return을 만나는 순간 결과값을 돌려준 다음 함수를 빠져나간다.

# return의 또다른 쓰임새
# 특별한 상황에서 함수를 빠져나가고 싶다면 return을 단독으로 써서 함수를 즉시 빠져나갈수 있다.
def say_nick(nick):
    if nick == "바보":
        return # break를 사용 하면 outside loop 라는 error 발생. 함수를 벗어나게되어 오류가 발생하는 듯하다..
                # 따라서 함수에서 아무것도 하지 않고 빠져나가고싶으면 return을 단독으로 사용
    print (f'나는{nick} 입니다')
say_nick("바다의보배")    


# 매개 변수 초기값(default/항상 같은 값) 미리 설정하기
def say_myself(name, age, man=True): #3번째 성별 변수를 man(True)로 고정 해놓은 것. 뭘 입력해도 True로 적용.
    print(f'이름은 {name} 입니다.')
    print(f'나이는 {age}살입니다.')
    if man:
        print("남자입니다.")
    else :
        print("여자입니다.")
        
say_myself("이상동",34,False)
#매개 변수 초기값의 위치는 항상 마지막에 둘 것!!!!!!!!!!!!!
#3번째 성별 변수를 man(True)로 고정 해놓은 것. 뭘 입력해도 True로 적용
# def say_myself(name,man=True,age): .
#     print(f'이름은 {name} 입니다.')
#     print(f'나이는 {age}살입니다.')
#     if man:
#         print("남자입니다.")
#     else :
#         print("여자입니다.")
        
# say_myself("이상동",34)
# SyntaxError: non-default argument follows default argument 
# 34가 성별인지 나이인지 결정을 못하고 error

# 함수 안에서 선언한 변수의 효력 범위.
t = 1
def vartest(t):
    t += 1
print(vartest(t)) # 2가 출력 될 것 같지만 None이 출력 return이 없기 때문. 함수만의 변수
print(t)          # 1이 출력 될 것. 

# 함수 안에서 함수 밖의 변수를 변경하는 법
# 방법 1
print("*"*30) # 줄바뀜 표시
o = 1
def vartest(o):
    o += 1
    return o # o를 결과값으로 받는다
print(vartest(o)) 
o = vartest(o) # 함수 안의 o와 함수 밖의 o는 다르다. 외부의 변수 o를 vartest(o)의 결과값인 return o로 받겟다.
print(o)

# lambda 함수 예약어로 def 와 동일한 역할. 주로 간결하게 만들 때 사용
print("*"*30) # 줄바뀜 표시
add3= lambda a,b : a+b #마지막에 return이 표기만 생략. 결과값을 돌려준다.
print(add3(5,6))
