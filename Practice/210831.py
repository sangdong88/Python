# 탭을 공백 문자로 바꾸기

# A씨는 개발된 소스코드를 특정업체에 납품하려고 한다. 개발된 소스코드들은 탭으로 들여쓰기가 된것, 공백으로 들여쓰기가 된 것들이 섞여 있다고 한다.

# A씨는 탭으로 들여쓰기가 된 모든 소스를 공백 4개로 수정한 후 납품할 예정이다.

# A씨를 도와줄 수 있도록 소스코드내에 사용된 탭(Tab) 문자를 공백 4개(4 space)로 바꾸어 주는 프로그램을 작성하시오.


####################################


# 게시판 페이징

# A씨는 게시판 프로그램을 작성하고 있다.

# A씨는 게시물의 총 건수와 한 페이지에 보여줄 게시물수를 입력으로 주었을 때 총 페이지수를 리턴하는 프로그램이 필요하다고 한다.

# 입력 : 총건수(m), 한페이지에 보여줄 게시물수(n) (단 n은 1보다 크거나 같다. n >= 1)
# 출력 : 총페이지수

# A씨가 필요한 프로그램을 작성하시오.


a = input("총건수를 입력하세요 :         ")
a = int(a)
print(type(a))

b = input("게시물수를 입력 하세요 :        ")
b = int(b)
while True :
    if b >= 1 :
        print(f"총페이지 수는 : {a*b} 입니다")
        break
    else :
        b = input("게수물수를 다시 입력하세요 :   0보다 큰 수")
        b = int(b)
        if b >= 1 :
            print(f"총페이지 수는 : {a*b} 입니다")
            break
        

# 다른 풀이
import math

m = int(input('총건수: '))
n = int(input('한페이지에 보여줄 게시물수: '))

print(math.ceil(m/n))


# ceil 함수란 ??
# ceil() 함수는 소수점 자리의 숫자를 무조건 올리는 함수이다.

# ceil의 사전적의미 '<방에> 천장을 만들다'

# 처럼 무조건 소수점 자리를 올린다.

# ceil(99.2) = 100


# floor() 함수는 뜻 그대로 바닥으로 만든다.

# 소수점 아래를 무조건 무시

# floor(3.6) = 3

# floor(5.1) = 5

# floor(-1.6) = -2 



# round() 함수가 우리가 보통 알고 있는 반올림함수다.

# round(3.4) : 3

# round(5.6) : 6

# round(9.5) :10

# round(-2.5) : -3

# round(-3.6) : -4

# round(-5.4) : -5


