#매개 변수는 3개 (숫자1, 숫자2, 연산)
#연산의 기본 매개변수는 덧셈

a1 = int(input ("숫자 3개를 입력하세요: "))
a2 = int(input ("숫자 3개를 입력하세요: "))
a3 = int(input ("숫자 3개를 입력하세요: "))
def cal (a,b,c):
    if c == 0:
        return a+b
    elif c== 1 :
        return a-b
    elif c==2 :
        return a * b
    elif c==3:
        return a / b
    else :
        print("0부터 3까지다")


print (cal(a1,a2,a3))

