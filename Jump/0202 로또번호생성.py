# random 모듈을 활용하여 로또 번호 생성기 만들기

import random

l=[]
while True:
    temp = random.randint(1,45)
    if temp not in l:
        l.append(temp)
    if len(l) == 6:
        break

print(type(l))
print(l)
l.sort() # 소팅은 다른 변수로 지정해줄 필요없이 기존 변수에 바로 적용 변경가능.ArithmeticError
print(l)
