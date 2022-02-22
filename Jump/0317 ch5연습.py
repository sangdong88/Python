# # 1번문제
# class Calculator():
#     def __init__(self):
#         self.value = 0
        
#     def add (self, val):
#         self.value += val
# # 위 클래스를 상속하는 UpgradeCalculator를 만들고 값을 ㅃ래 수 있는 minus 메서드를 추가해보자
# # 다음과 같이 동작하는 클래스를 만들어야 한다.

# # cal = UpgradeCalculator()
# # cal.add(10)
# # cal.min(7)

# # print(cal.value) # 10에서 7을 뺀 3을 출력.

# # 우선 Calculator 클래스를 상속하는 UpgradeCalculator를 생성

# class UpgradeCalculator(Calculator):
#     def min (self, val):
#         self.value -= val
     
# # 이제 객체에 UpgradeCalculator 클래스를 지정해준다.
# cal = UpgradeCalculator()   
# print (cal.value)
# cal.add(10)
# print (cal.value)
# cal.min(7)
# print(cal.value)

# 2번문제
# 객체 변수 value 가 100 이상의 값을 가질 수 없도록 제한 하는 MaxLimitCalculator 클래스를 만들어 보자
# 즉 다음과 같이 동작해야한다.

# cal = MaxLimitCalculator()
# cal.add(50)
# cal.add(60)
# print(cal.value) # 100을 출력하라 제한 100
# 단 Calculator 클래스를 상속하라

# class Calculator():
#     def __init__(self):
#         self.value = 0
        
#     def add (self, val):
#         self.value += val
        
# class Maxlimit(Calculator):
#     def add (self, val):
#         self.value += val
#         if self.value <= 100 :
#             return print(self.value)
#         else :
#             return print(100)

# cal = Maxlimit()

# cal.add (60) # 60
# cal.add (30) # 90
# cal.add (30) # 100

# 3번 문제
# 하나
from unittest import result

print(all([1,2,abs(-3)-3]))
# # false
# print(abs(-3)-3) = 0 이라서 0은 거짓이므로 False 출력

# 둘
print(chr(ord('a')) == 'a') # ==> True
print(ord('a')) # ==> 'a'의 아스키 코드 97 출력
print(chr(97)) # ==> 아스키 코드 97을 'a'로 출력
# 결국 chr(ord(*))를 하면 원래 문자 출력

# 4번 문제
# filter와 lambda를 사용하여 리스트 [1,-2,3,-5,8,-3]
# filter 함수는 filter(함수이름, iterable)로 사용.
def positive(x):
    result = []
    for i in (x):
        if i >= 0 :
            result.append(i)
    return result
a = [1,-2,3,-5,8,-3]
print(positive(a)) # ==> [1, 3, 8] 출력

def positive1(x):
    return x > 0
print(positive1(-3)) # ==> False라고 출력이 되는 구나....
#print (positive1(a)) # 이렇게 하면 list [1,-2,3,-5,8,-3] > 0 이 되어 부등식이 성립하지 않아 에러
# 그래서 filter 함수의 자료형을 하나씩 함수에 입력해주는 기능이 필요한 것.
print(list(filter(positive1,a))) # ==>[1, 3, 8]
# filter 함수 앞에 항상 tuple로 받을 건지 list로 받을 건지 설정해줘야 한다.

# 람다 함수를 사용하여 간단히 써보자
print(list(filter(lambda x : x > 0,a))) # 같은 값을 출력[1, 3, 8]

# 5번 문제
# 234라는 10 진수의 16 진수는 다음과 같이 구할 수 있다.
# hex(234) --> '0xea'
# 이번에는 반대로 16진수 문자열 '0xea'를 10 진수로 변경해 보자
# 내장 함수 int를 활용

print(int('0xea',16)) # 간단히 변경

# 6번 문제
# map과 lambda를 사용하여 [1,2,3,4] 리스트의 각 요솟값에 곱해진 리스트 [3,6,9,12]를 만들자.
b = [1,2,3,4]
print(list(map(lambda x : x * 3, b))) # ==> [3, 6, 9, 12]
# 함수를 썻을 때도 작성해보자
# def trimul(x): # 함수 이름 제일 앞에 숫자가 오면 안된다
#     result1 = []
#     for i in x:
#         i1 = i * 3
#         result1.append(i1)
#     return result1

# print(trimul(b)) # ==> [3, 6, 9, 12]
# map 함수를 사용해보면,
# def trumul1 (x):
#     return 3 * x
# print(list(map(trumul1,b))) # ==> [3, 6, 9, 12]
# # 모두 동일한 결과를 얻는다.

# # 7번 문제
# # 다음 리스트의 최대값과 최솟값의 합을 구해보자
# c = [-8, 2, 7, 5, -3, 5, 0, 1]
# def maxmin(x):
#     a = max(x)
#     print("max",a)
#     b = min(x)
#     print("min",b)
#     return print(a+b)
# maxmin(c)
# max 7
# min -8
# -1

# 8번 문제
# 17/3의 결과를 소숫점 4자리까지만 반올림하여 표시해 보자.
print(round(17 / 3 , 4))

# 9번 문제
# 다음과 같이 실행할 때 입력값을 모두 더하여 출력하는 스크립트를 작성해보자
# D:\> cd 코딩/Mymod
# D:\코딩/mymod> python testing.py 1 2 3 4 5 6 7 8 9 10
# 55

# # sys.argv를 활용한다.
# # 우선 Mymod 폴더에 testing.py 를 만든다.
# import sys # sys.argv를 사용하기 위해 sys를 import 해준다
# a = sys.argv[1:] # sys.argv를 a 변수에 지정
# # sys.argv는 0번째 인자가 파일이름으로 슬라이싱하여 제거
# # ['testing.py', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# # ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'] [1:] 슬라이싱 후 결과
# # 이제 입력 받은 값들은 모두 더하는 for 문 작성
# result = 0 # 더한 값들을 저장할 result 변수를 0으로 지정
# for i in a: # a 리스트안에서 인자를 1개 씩 꺼내오자
#     result += int(i) # i 값은 '1'  과같은 문자 형이므로 int 함수로 정수형으로 변경
# print (result) ==>> 55 결과값 을 얻는다

# 10번 문제
# os 모듈을 사용하여 다음과 같이 동작하도록 코드를 작성해 보자.

# C:\doit 디렉터리로 이동한다.
# dir 명령을 실행하고 그 결과를 변수에 담는다.
# dir 명령의 결과를 출력한다.

# import os 
# os.chdir("D:/코딩/code")
# print(os.getcwd())
# f = os.popen("dir")
# print(f.read())

# 11번 문제
# glob 모듈을 사용하여 D:/코딩/code 디렉터리의 파일 중 확장자가.py인 파일만 출력하는 프로그램을 작성해 보자.
# import glob
# print(glob.glob("D:/코딩/code/*.py"))
# ['D:/코딩/code\\0115 합겹불합격.py', 'D:/코딩/code\\0122.py', 'D:/코딩/code\\0128.py', 'D:/코딩/code\\0129ch4연습2.py', 'D:/코딩/code\\0201.py', 'D:/코딩/code\\0202 lambda함수.py', 'D:/코딩/code\\0202 lambda함수2.py', 'D:/코딩/code\\0202 로또번호생성.py', 'D:/코딩/code\\0202 웹크롤링.py', 'D:/코딩/code\\0202.py', 'D:/코딩/code\\0205 구구단 여러개.py', 'D:/코딩/code\\0308 구구단계산기.py', 'D:/코딩/code\\0311 ch4-1.py', 'D:/코딩/code\\0311 ch4-2.PY', 'D:/코딩/code\\0311 ch4연습1.py', 'D:/코딩/code\\0311 ch4연습2.py', 'D:/코딩/code\\0312 ch4연습3~7.py', 'D:/코딩/code\\0312 ch5-1.py', 'D:/코딩/code\\0313 ch5-1-2.py', 'D:/코딩/code\\0313 ch5-1-3.py', 'D:/코딩/code\\0313 ch5-2.py', 'D:/코딩/code\\0313 ch5-3.py', 'D:/코딩/code\\0314 ch5-4.py', 'D:/코딩/code\\0314 ch5-5.py', 'D:/코딩/code\\0317 ch5-6.py', 'D:/코딩/code\\0317 ch5연습.py', 'D:/코딩/code\\시험.py', 'D:/코딩/code\\자판기.py', 'D:/코딩/code\\점수계산.py', 'D:/코딩/code\\찻집 
# 계산.py', 'D:/코딩/code\\합 불 판독.py', 'D:/코딩/code\\환율계산.py']

# 12번문제
# time 모듈을 사용하여 현재 날짜와 시간을 다음과 같은 형식으로 출력해 보자.
# 2018/04/03 17:20:32
import time
print(time.strftime('%Y ''%x'" "'%X', time.localtime(time.time())))
# Q13
# random 모듈을 사용하여 로또 번호(1~45 사이의 숫자 6개)를 생성해 보자(단 중복된 숫자가 있으면 안 됨)

print(time.strftime("%Y/%m/%d %H:%M:%S"))   # %Y:년, %m:월, %d:일, %H:시, %M:분, %S:초
# time.localtime(time.time()) 생략 가능하다

# 13번 문제
# random 모듈을 사용하여 로또 번호(1~45 사이의 숫자 6개)를 생성해보자 (중복 금지)
import random # 우선 random 모듈 import
# random모듈의 무슨 함수를 쓸까 ?
# random.randint를 써보자

result12 = []
for i in range(6): # 0 1 2 3 4 5
    num = random.choice(range(1,46))
    if num not in result12 :
        result12.append(num)
    # 문제는 중복을 제거 하는 것
 # 정렬한번 해주고
print (sorted(result12))
# sort 함수를 쓰려면
# result12.sort()
# print(result12) 이렇게 작성


# import random

# result = []
# while len(result) < 6:
#     num = random.randint(1, 45)   # 1부터 45까지의 난수 발생
#     if num not in result:
#         result.append(num)

# print(result)