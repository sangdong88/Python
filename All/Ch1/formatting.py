# Formatting




# 방법1




# 포매팅 연산자 '%'
# %s(문자열), %d(정수), %c(문자 1개), %f(부동소수)

print("%s" % "apple") # apple
print("%d" % 113) # 113
print("%c" % "c") # c 문자열 1개 표시로 별로 쓸일 없음
print("%f" % 12.222) # 12.222000

# 방법1-1
# 정렬과 소수점 표현
# 오른쪽 정렬
print("%10s" % "hi" ) #         hi # 공백 10칸 후에 문자열 대입
# 왼쪽 정렬
print("%-10sjane" % "hi") # hi        jane # 역방향으로 공백 10칸 # 대입문자열 다음 공백 10칸
print()

# 소수점 & 자리수 표현
print("%10.4s" % 999.879852) #       999.
# 정수(전체 자리수), 소수점 뒤 숫자는 총 표현 자리수 (입력값의 4자리만 표현)
print("%-10.4s" % 999.879852) #999.      
# -는 왼쪽 정렬, 10은 총 10자리, .4는 입력값의 4자리만 표현
print("%10.4f" % 999.879852) #  999.8799  # 소수점 4자리만 표시
# % 바로 뒤에 정수는 전체 자리수를 의미하고 .뒤에 숫자가 소수점 표시 자리수
# 만일 전체 자리수 보다 작은 숫자가 입력되면 무시하고 999.8799만 표시 된다.
# 정수(전체 자리수)가 입력 된 숫자의 자리수 보다 클 때만 공백 생성




# 방법2




# 포맷함수 사용 {}.format()

print("{}".format("Hi")) # Hi
print("{}".format(123)) # 123
print("{}".format(123.5255)) # 123.5255
#{} 중괄호 안에 format()괄호 안에 들어가는 문자열, 정수형, 소수형 모든 자료형이 다 들어간다.
# 포매팅 연산자는 자료형의 타입을 나누어 줘야 하지만 포맷함수는 No need.

# 방법2-2 

# 인덱스 지정
print("{0}  {1}".format("Hi","Everybody")) # Hi  Everybody
print("{1}  {0}".format("Hi","Everybody")) # Everybody  Hi
# 인덱스 번호 지정이 가능하므로 자료의 순서를 원하는대로 포매팅 할 수 있다.

# 변수이름 지정
fruit = "apple"
num = 123
print("{0}  {1}".format(fruit,num)) # apple  123
print("{fruit}  {num}".format(fruit="watermelon",num=3)) # watermelon  3
# format 함수에 {name} 형태를 사용할 때는 반드시 .format(name = value) 안에 형태로 입력 되야한다.

# 방법2-3

# 정렬과 소수점 표현
# 왼쪽 정렬
print("{:<10}".format("hi")) #hi          # 화살표 방향<에 문자가 위치
# 오른쪽 정렬
print("{:>10}".format("hi")) #         hi # 화살표 방향>에 문자가 위치
# 가운데 정렬
print("{:^10}".format("hi")) #    hi      # 가운데 ^
# 정렬을 사용하면서 공백을 채우는 것도 가능하다
print("{:=<10}".format("hi")) #hi======== # :뒤에 오는 문자 '='로 공백 채움
print("{:*>10}".format("hi")) #********hi # :뒤에 오는 문자 '*'로 공백 채움

# 소수점 & 자리수 표현
print("{:10.4}".format(777.777777)) #      777.8
# : 입력 후 10 (전체자리수), .4 (입력값의 4자리 표시), 나머진 공백처리
print("{:10.4f}".format(777.777777)) #  777.7778
# : 입력 후 10 (전체자리수), .4f (소수점4자리까지 표시), 나머진 공백처리





# 방법3




# f문자열 포매팅

# 기존 {}.format("""")에서 f'{""""}'로 변경 하여 사용
print(f"{'HI'}") # HI
print(f"{123}") # 123
print(f"{123.5255}") # 123.5255

# 인덱싱 기능은 사용 할 수 없음

# 변수이름 지정
fruit = "apple"
num = 123
print(f"{fruit}  {num}") # apple  123
print(f"{fruit}  {num}") # apple  123

# 정렬과 소수점 표현
print(f"{'hi':<10}") #hi          # 화살표 방향<에 문자가 위치
# 오른쪽 정렬
print(f"{'hi':>10}") #         hi # 화살표 방향>에 문자가 위치
# 가운데 정렬
print(f"{'hi':^10}") #    hi      # 가운데 ^
# 정렬을 사용하면서 공백을 채우는 것도 가능하다
print(f"{'hi':=<10}") #hi======== # :뒤에 오는 문자 '='로 공백 채움
print(f"{'hi':*>10}") #********hi # :뒤에 오는 문자 '*'로 공백 채움

# 소수점 & 자리수 표현
print(f"{777.7777:10.4}") #      777.8
# : 입력 후 10 (전체자리수), .4 (입력값의 4자리 표시), 나머진 공백처리
print(f"{777.7777:10.4f}") #  777.7778
# : 입력 후 10 (전체자리수), .4f (소수점4자리까지 표시), 나머진 공백처리