### input 함수 ###

# input()  # 사용자가 입력 한 문자를 변수로 지정 할 수 있는 함수

# input("숫자를 입력 해주세요 :      ")  # 괄호 안에 문자열은 입력에 포함 되지 않는다.

a = input("숫자를 입력해주세요 >>> ")
print(a)
print(type(a))
a = int(a)
print(type(a))
print()  # 줄간격


# 형 변환 함수
str()  # 문자형으로 변환
b = 33
print(b, type(b))
b = str(33)
print(b, type(b))

print()
int()  # 정수형으로 변환d
c = "44"
print(c, type(c))
c = int(c)
print(c, type(c))

float()  # 실수형으로 변환
complex()  # 복소수형으로 변환
