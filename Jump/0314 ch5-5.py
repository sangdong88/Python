# 내장 함수
# 프로그램이 만들어져 있는지를 먼저 살펴 보아라.
# Don't Reinvent The Wheel. 이미 만들어진 것을 다시 만드는 것은 불필요한 행동이다.
# 그리고 이미 만들어진 프로그램은 테스트 과정을 수 없이 거쳤기 때문에 충분히 검증 되어 있다.
# 그래서 이미 만들어진 것들, 특히 파이썬 라이브러리를 살펴 보는 것이 중요하다.

# 라이브러리를 살펴보기 전에 파이썬 내장 함수를 먼저 살펴보자. 
# 파이썬 내장 함수는 외부 모듈과 달리 import가 필요하지 않기 때문에 아무런 설정없이 바로 사용 가능.

# abs ()

# 어떤 숫자를 입력 받았을 때, 그 숫자의 절대값을 돌려주는 함수
# >>> abs (3)
# 3
# >>> abs(-3)
# 3
# >>> abs(-3.2)
# 3.2

# all ()

# 반복 가능한(iterable) 자료형 x를 입력 인수로 받으며, 이 x요소가 모두 참이면 True, 거짓이 하나라도 있으면 False
# 반복 가능한 자료형이란 for 문으로 그 값을 출력 할 수 있는 것을 위미. 리스트, 튜플, 문자열, 딕셔너리, 집합 등이 있다.
# >>> all ([1,2,3])
# True
# >>> all ([1,2,3,0])   # 0요소 0은 거짓이므로 False를 돌려준다.
# False
# >>> all (range(1,10))
# True
# >>> all() # 괄호 안에 아무것도 입력 하지 않으면, error 발생.
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: all() takes exactly one argument (0 given)
# >>> all([]) # 빈 중괄호를 입력한 경우, True를 리턴.
# True

# any

# any(x)는 반복 가능한(iterable) 자료형 x를 인수로 받으며, 이 x의 요소 중 하나라도 참이 있으면 True를 돌려주고,
# x가 모두 거짓일 때에만 False를 돌려준다. all(x)의 반대이다. 
# >>> all([]) 
# True
# >>> any([1,2,3,0])
# True
# >>> any(["",0])
# False
# >>> any([])
# False

# chr

# chr(i)는 아스키(ASCII) 코드 값을 입력 받아 그 코드에 문자를 출력하는 함수이다.
# 아스키 코드란 0에서 127사이의 숫자를 각각 하나의 문자 또는 기호에 대응시켜 놓은 것이다.
# >>> chr(97)
# 'a'
# >>> chr(48)
# '0'

# # 아스키 코드 확인하는 코딩. 파일 저장.

# f = open ("test33.txt",'w')
# for i in range(0,128):
#     data = chr(i)
#     print (data)
#     f.write(data) # f.write에는 str type만 가능.
# f.close()

# dir

# dir은 객체가 자체적으로 가지고 있는 변수나 함수를 보여준다. 다음 예는 리스트와 딕셔너리 객체 관련(메서드)를
# 보여주는 예이다.
# dir([]) 리스트형
# dir(()) 튜플형
# dir({}) 딕셔너리형
# dir(str) 문자형
# dir(int) 정수형
# dir(float) 실수형 등등. 유용하게 사용 가능.

# divmod

# divmod(a,b)는 2개의 숫자를 입력으로 받는다. 그리고 a를 b로 나눈 몫과 나머지를 튜플형태로 돌려주는 함수.
# >>> divmod(22,5) 
# (4, 2)  몫 4 , 나머지 2

# enumerate()

# enumerate는 "열거하다" 라는 뜻이다. 이 함수는 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아
# 인덱스 값을 포함하는 enumerate객체를 돌려준다.
# 보통 enumerate 함수는 for 문과 함께 자주 사용하다.
# for i, name in enumerate(['body','foo','bar']):
#     print(i,name)
# 0 body
# 1 foo
# 2 bar
# 순서 값과 함께 body, foo, bar가 순서대로 출력되었다. 즉 위 예제와 같이 enumerate를 for 문과 함께 사용하면
# 자료형의 순서(index)와 그 값을 쉽게 알 수 있다.
# for문처럼 반복 되는 구간에서 객체가 현재 어느 위치에 있는지 알려주는 인덱스 값이 필요할 때 사용
# a = enumerate("askdjfaslkdfjeeo")
# b = [1,2,3,4,5,6,7]
# c = ("a","b","c","d","e")
# # print(a)
# # print(enumerate(b[0])) # 이렇게 따로 쓰면 안되는 구나....int 형은 non iterable
# print(enumerate(c)) >>><enumerate object at 0x0000027832738B80>

# eval

# eval (expression)은 실행 가능한 문자열 을 입력으로 받아 문자열을 실행한 결과 값을 돌려주는 함수
# # eval함수 괄호안의 값은 전체 큰 따음표나 작은 따음표로 지정 해야한다.
# >>> eval('1+2')
# 3
# >>> eval('"Hello"+"World"') 
# # 'HelloWorld'
# >>> eval("divmod(4,3)")
# (1, 1)

# filter 

# filter 란 무엇인가를 걸러낸다는 뜻으로 filter 함수도 동일한 의미를 갖는다.
# filter 함수는 첫 번째 인수로 함수 이름을, 두 번째 인수로 그 함수에 차례로 들어갈 반복 가능한 자료형을 받는다.
# 그리고 두 번째 인수인 반복 가능한 자료형 요소가 첫 번째 인수인 함수에 입력 되었을때, 반환 값이 참인 것만 묶어서 돌려준다.

# def positive(l):
#     result=[]
#     for i in l:
#         if i > 0 :
#             result.append(i)
#     return (result)

# print(positive([1,-3,2,0,-5,6]))  # [1, 2, 6] 결과 값

# # filter 함수를 이용하여 간단하게 작성 할 수 있다.

# def positive1(x):
#     return x > 0
#     # if return == True:
#         # ??.append (x)
# # 근데 이건 어느 변수에 필터링 된 값이 저장되는 걸까 ? # 필터 함수에 저장?

# print(list(filter(positive1,[1,-3,2,0,-5,6]))) # [1, 2, 6] 결과 값
# print(tuple(filter(positive1,[1,-3,2,0,-5,6]))) # (1, 2, 6) 결과 값
# # positive 함수에서 result = [] 리스트형으로 지정한 것 처럼 filter 함수 앞에는 list 혹은 tuple 같이 어떤 형식으로 결과값을 출력할지 선택해야 한다.

# 좀더 간단하게 작성해보면 lambda 함수를 사용해 보자.

# print(list(filter(lambda x : x > 0,[1,-3,2,0,-5,6]))) # 결과 값[1, 2, 6]

# hex

# hex(x)는 정수 값을 입력 받아 16진수(hexadeciaml)로 변환하여 돌려 주는 함수.
# >>> hex(234)
# '0xea'
# >>> hex(3)
# '0x3'

# id

# id(object)는 객체를 입력 받아 객체 고유 주소값을 돌려주는 함수이다.
# >>> a =3  
# >>> id(3)
# 2872867055984
# >>> id(a)
# 2872867055984
# >>> a=b
# >>> id(b)
# 2872867055984

# input

# input([prompt])은 사용자 입력을 받는 함수이다. 매개변수로 문자열을 주면 다음 세번째 예에서 볼 수 있듯이 그 문자열은 프롬프트가 된다.
# [] 기호는 괄호 안의 내용을 생략할 수 있다는 관례 표기법임을 기억하자.
# 많이 사용해 보았으니 pass.

# int

# int(x)는 문자열 형태의 숫자나 소수점이 있는 숫자 등을 정수 형태로 돌려주는 함수로, 정수를 입력으로 받으면 그대로 돌려준다.
# 오직 문자열 형태의 숫자, 소수점잇는 숫자만 인트 함수의 입력 값이 도리 수 있다.
# >>> int('3')
# 3
# >>> int(3.4)
# 3
# >>> int('11' ,2) # 2진수 '11'을 10진수로 바꿔준다
# 3
# >>> int('1A', 16) # 16진수 '1A'를 10진수로 바꿔준다
# 26

# isinstance

# isinstance(object, class)는 첫 번째 인수로 인스턴스, 두 번째 인수로 클래스 이름을 받는다.
# 입력으로 받은 인스턴스가 그 클래스의 인스턴스인지를 판단하여 참이면, True. 거짓이면 False를 돌려준다.
# class person :
#     pass
# a = person() # a 는 person 클래스가 만든 인스턴스
# b = 3 # b는 person 클래스가 만든 인스턴스가 아니다
# print(isinstance(a, person)) # True
# print(isinstance(b, person)) # False
# 그러니까 해당 객체에 person 클래스가 연결 되어있나를 확인 할 때 쓰는 듯.

# len

# len(s)는 입력값 s의 길이를(요소 전체의 길이)를 돌려주는 함수 이다.
# >>> len('python')
# 6
# >>> len([1,2,3])
# 3
# >>> len((1,'a')) 
# 2

# list

# list(s)는 반복 가능한 자료형 s를 입력 받아 리스트로 만들어줌.
# >>> list("python")
# ['p', 'y', 't', 'h', 'o', 'n']
# # 리스트 함수에 리스트를 입력으로 주면 똑같은 리스트를 복사하여 돌려준다.
# >>> a=[1,2,3]
# >>> b = list(a)
# >>> b
# [1, 2, 3]

# map

# map(f, iterable)은 함수(f)와 반복 가능한(iterable) 자료형을 입력으로 받는다.
# map은 입력받은 자료형의 각 요소를 함수f가 수행한 결과를 묶어서 돌려주는 함수이다.

# def two(numberlist): # 리스트 요소를 입력받아 각 요소에 2를 곱한 값을 돌려준다.
#     result = []
#     for number in numberlist:
#         result.append(number*2)
#     return result

# result = two ([1,2,3,4])
# print(result) 
# [2, 4, 6, 8]

# def two(x):
#     return x*2
# print(list(map(two,[1,2,3,4]))) # 리스트 형으로 결과값을 받아야 하기 때문에 list 함수를 map 함수 앞에 써준다. filter함수랑 같은 내용
# [2, 4, 6, 8] 

# lambda 함수로 더 간단히 작성해보자
# print(list(map(lambda x: x * 2,[1,2,3,4])))
# [2, 4, 6, 8] 

# max

# max(iterable)는 인수로 반복 가능한 자료형을 입력받아 그 최대값을 돌려주는 함수이다.
# >>> max([1,2,3])
# 3

# min

# min(iterable)는 인수로 반복 가능한 자료형을 입력받아 그 최소값을 돌려주는 함수이다.
# >>> min([1,2,3])
# 1

# oct

# oct(x)는 정수 형태의 숫자를 8진수 문자열로 바꾸어 돌려주는 함수이다.
# >>> oct(34)
# '0o42'
# >>> oct(12345)
# '0o30071'

# open

# open(filename, [mode])은 "파일 이름"과 "읽기 방법"을 입력받아 파일 객체를 돌려주는 함수이다. 
# 읽기 방법(mode)을 생략하면 기본값인 읽기 전용 모드(r)로 파일 객체를 만들어 돌려준다.

# mode	설명
# w	쓰기 모드로 파일 열기
# r	읽기 모드로 파일 열기
# a	추가 모드로 파일 열기
# b	바이너리 모드로 파일 열기                   ### 바이너리가 무엇인지 공부하기
 
# b는 w, r, a와 함께 사용한다.

# >>> f = open("binary_file", "rb")
# 위 예의 rb는 "바이너리 읽기 모드"를 의미한다.

# 다음 예의 fread와 fread2는 동일한 방법이다.

# >>> fread = open("read_mode.txt", 'r')
# >>> fread2 = open("read_mode.txt")
# 즉 모드 부분을 생략하면 기본값으로 읽기 모드 r를 갖게 된다.

# 다음은 추가 모드(a)로 파일을 여는 예이다.
# >>> f = open("append_mode.txt", 'a')

# ord

# ord(c)는 문자의 아스키 코드 값을 돌려주는 함수이다.

# ※ ord 함수는 chr 함수와 반대이다.
# >>> ord('a')
# 97
# >>> ord('0')
# 48

# pow

# pow(x, y)는 x의 y 제곱한 결괏값을 돌려주는 함수이다.
# >>> pow(2, 4)
# 16
# >>> pow(3, 3)
# 27

# range

# range([start,] stop [,step] )는 for문과 함께 자주 사용하는 함수이다. 이 함수는 입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 돌려준다.

# 인수가 하나일 경우
# 시작 숫자를 지정해 주지 않으면 range 함수는 0부터 시작한다.
# >>> list(range(5))
# [0, 1, 2, 3, 4]

# 인수가 2개일 경우
# 입력으로 주어지는 2개의 인수는 시작 숫자와 끝 숫자를 나타낸다. 단 끝 숫자는 해당 범위에 포함되지 않는다는 것에 주의하자.
# >>> list(range(5, 10))
# [5, 6, 7, 8, 9]
# 인수가 3개일 경우

# 세 번째 인수는 숫자 사이의 거리를 말한다.
# >>> list(range(1, 10, 2))
# [1, 3, 5, 7, 9]
# >>> list(range(0, -10, -1))
# [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
# >>> list(range(0,-10, 1))  # 거리는 절대값이 아니다 따라서 음수 range의 거리는 -가 붙어야된다.
# [] 

# round

# round(number[, ndigits]) 함수는 숫자를 입력받아 반올림해 주는 함수이다.
# ※ [, ndigits]는 ndigits가 있을 수도 있고 없을 수도 있다는 의미이다.
# >>> round(4.6)
# 5
# >>> round(4.2)
# 4
# 다음과 같이 실수 5.678을 소수점 2자리까지만 반올림하여 표시할 수 있다.
# >>> round(5.678, 2)
# 5.68
# # round 함수의 두 번째 매개변수는 반올림하여 표시하고 싶은 소수점의 자릿수(ndigits)이다.
# 사사오입 원칙
# round()는 사사오입 원칙을 따른다. 
# 반올림할 자리의 수가 5이면 반올림 할 때 앞자리의 숫자가 짝수면 내림하고 홀수면 올림 한다.
# >>> round(4.5)  #결과는 4
# >>> round(3.5)  #결과는 4



# sorted

# sorted(iterable) 함수는 입력값을 정렬한 후 그 결과를 리스트로 돌려주는 함수이다.
# a = [1,5,2,4,3,-2,-5]
# print(sorted(a)) # [-5, -2, 1, 2, 3, 4, 5] 이 출력
# print(a.sort()) # None 이 출력
# print(a) # [-5, -2, 1, 2, 3, 4, 5]

# sort() 함수는 리스트 자료형의 객체 그 자체를 정렬만 해줄 뿐 결과를 돌려주지는 않는다.
# 따라서, a.sort() 후에 다시 객체 a 를 출력해야 한다. 

# str

# str(object)은 문자열 형태로 객체를 변환하여 돌려주는 함수이다.
# >>> str(3)
# '3'
# >>> str([1,2,3])
# '[1, 2, 3]'
# >>> type(str([1,2,3]))
# <class 'str'> # list도 문자열 형태가 될 수 있구나

# sum

# sum(iterable)은 입력받은 리스트나 튜플의 모든 요소의 합을 돌려주는 함수이다.
# >>> sum((1,2,3))  
# 6
# >>> sum([1,2,3])
# 6
# >>> sum(1,3)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'int' object is not iterable
# >>> sum('1','3') 
# Traceback (most recent call last):

# tuple

# tuple(iterable)은 반복 가능한 자료형을 입력받아 튜플 형태로 바꾸어 돌려주는 함수이다. 만약 튜플이 입력으로 들어오면 그대로 돌려준다.

# >>> tuple("abc")
# ('a', 'b', 'c')
# >>> tuple([1, 2, 3])
# (1, 2, 3)
# >>> tuple((1, 2, 3))
# (1, 2, 3)

#type

# type(object)은 입력값의 자료형이 무엇인지 알려 주는 함수이다.

# >>> type("abc")
# <class 'str'>
# >>> type([ ])
# <class 'list'>
# >>> type(open("test", 'w'))
# <class '_io.TextIOWrapper'>

# zip

# zip(*iterable)은 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수이다.
# ※ 여기서 사용한 *iterable은 반복 가능(iterable)한 자료형 여러 개를 입력할 수 있다는 의미이다.
# 잘 이해되지 않는다면 다음 예제를 살펴보자.

# >>> list(zip([1, 2, 3], [4, 5, 6]))
# [(1, 4), (2, 5), (3, 6)]
# >>> list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))
# [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
# >>> list(zip("abc", "def"))
# [('a', 'd'), ('b', 'e'), ('c', 'f')]
