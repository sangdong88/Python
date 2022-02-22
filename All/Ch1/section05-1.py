# Setction05-1
# 파이선 흐름제어(제어문)
# 조건문 실습

print(type(True),type(False))
# <class 'bool'> <class 'bool'>

# 예제 1
if True :
    print("yes")

# 예제 2
if False :
    print("No") # 출력되는것없음

# 예제 13
if False :
    print("No")
else:
    print("Yes2")

# 관계 연산자
# >, >=, <, <=, ==, !=
# 크다, 크거나 같다, 작다, 작거나 같다, 같다, 같지 않다

a=10
b=0
print(a==b) # False
print(a!=b) # True
print(a>b) # True

# 참 거짓 종류(True, False)
# 참 : "내용", "[내용]", (내용), {내용}, 1
# 거짓 : "", [], (), {}, 0

city = ""

if city:
    print(">>>>True")
else:
    print(">>>>False")


# 논리 연산자
# and / or / not
a = 100 
b = 60
c = 15

print('and : ', a>b and b>3)
# and :  True  둘다 만족
print('or :', a>b or c>b)
# or : True 둘 중에 하나라도 만족하면 True
print('not : ', not a >b)
# not :  False 반대


# 산술, 관계, 논리 연산자
# 산술 > 관계 > 논리 순서로 적용
print('ex ": ', 5 + 10 >0 and not 7+3 ==10)
# ex ":  False 
# True and False 는 False

score1 = 90
score2 = 'A'

if score1 >= 90 and score2 =='A':
    print("합격")
else :
    print("불합격")


# 다중 조건문
num = 90

if num >= 90:
    print("num 등급 A" , num)
elif num >= 80:
     print("num 등급 B" , num)
elif num >= 70:
    print("num 등급 C" , num)
else:
    print("꽝")

# 목적에 맞게 흐름을 제어하는데 if 문 사용

# 중첩조건문
age = 27
height = 175

if age >= 20 :
    if height >= 170 :
        print ("A지망 지원가능 ")
    elif height >= 160 :
        print ("B지망 지원가능")
    else :
        print("지원 불가")
else :
    print("나이미달")