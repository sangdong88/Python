# Section02-1
# 파이썬 기초 코딩
# print 구문의 이해

# 기본 출력
print('Hello python')
print("Hello python")
print("""Hello python""")
print('''Hello python''')

print() # print 함수 안에 ()빈 괄호는 줄바꿈

# Separator 옵션 사용

print('T', 'E', 'S', 'T')
print('T', 'E', 'S', 'T', sep="")
print('2019','02','19',sep="-")
print('niceman','google.com',sep="@")

# end 옵션 # 다음 출력과 붙여서 출력 붙일 때 " "안에 있는 문자열로 붙임

print ('Welcome To', end=" ")
print('the Hell', end=" ")
print('piano')

print()

# format 옵션 [] 대괄호 {} 중괄호 () 소괄호
print('{} and {}'.format('You', 'Me'))
print("{0} and {1} and {0}".format('You','Me'))
# 매핑하는 것 포맷 함수 안에 0부터 시작
print("{a} and {b}".format(a='You',b='Me'))
# 직접 포맷함수의 변수 입력

print() # 줄바꿈

print("%s's favorite number is %d" %('sid',7))
# sid's favorite number is 7
# %s문자 %d 정수 %f 실수
print("Test1 : %5d, Price :  %4.2f" %(776,6545.12))
# Test1 :   776, Price :  6545.12
print("Test1 : {0: 5d}, Price : {1: 4.2f}".format(776,6543.123))
# Test1 :   776, Price :  6543.12
print("Test1 : {a: 5d}, Price : {b: 4.2f}".format(a=776,b=6543.123))
# Test1 :   776, Price :  6543.12

"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\r : 캐리지 리턴
\f : 폼 피드
\a : 벨 소리
\b : 백 스페이스
\000 : 널 문자
...

"""

# file 옵션 사용
import sys

print('GeeksForGeeks', file=sys.stdout)
