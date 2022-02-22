# Section02-2
# 파이썬 기초 코딩
# 몸풀기 코딩 실습

# import this # 파이썬 언어에 대한 철학을 볼 수 있다.
import sys

# 파이썬 기본 인코딩
# 3버전 부터 기본 UTF8
print(sys.stdin.encoding)
# utf-8
print(sys.stdout.encoding)
# utf-8
# 입력과 출력 모두 utf-8

# 출력문
print("my name is Goodboy")

# 변수 선언
Myname = 'Goodboy'
# Myname 이라는 변수에 'Goodboy'라는 문자열을 할당해라.

# 조건문
if Myname == "Goodboy":
    print('ok') # ok 출력

# 반복문
for i in range(1,10):
    for j in range(1,10):
        print('%d * %d ='% (i,j),i*j)
        print(f'{i} * {j} = {i*j}')

# 변수 선언(한글)

이름 = "좋은사람"
# 출력
print(이름) # 한글도 print 되는 구나

# 함수 선언
def 인사():
    print("안녕하세요. 반갑습니다.")

인사() # 안녕하세요. 반갑습니다.

# 클래스 - 객체지향
class Cookie:
    pass

# 객체생성 - 인스턴스
cookie = Cookie()
print(id(cookie)) # 2024449791504
print(dir(cookie))
# ['__class__', '__delattr__', '__dict__', '__dir__',
# '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
# '__gt__', '__hash__', '__init__', '__init_subclass__',
