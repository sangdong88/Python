print ("구구단 계산기")

a=input("원하는 숫자를 입력하세요 :   ")
a=int(a)

for i in range(1,10):
    print(a*i, end=' ') # end = ' ' 는 한줄에 내용 표시. ' ' 사이에 공백을 넣으면 결과값 사이에 공백이 적용
