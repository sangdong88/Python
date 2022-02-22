# 문제1 주어진 자연수가 홀수 인지 짝수인지 판별해주는 함수를 작성
a = input("숫자를 입력하세요 :  ")
a1 = int(a)

def is_odd (num):
    if num % 2 == 0:
        return "짝수 입니다"
    else :
        return "홀수 입니다."
    
print(is_odd(a1))

# 람다함수
# return은 따로 쓰지 않는다

is_odd3 = lambda x: print("홀수") if x % 2 == 1 else print("짝수")
is_odd3(3)
