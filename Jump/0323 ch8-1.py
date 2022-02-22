# 8 장 종합문제
# ㅍ아ㅣ썬은 웹, GUI, 네트워크, 딥러닝 등 상당히 많은 일을 할 수 있는 언어이다.
# 여기에 준비한 문제들을 풀어보면서 얼마나 익숙해졌는지 점검해보자

# 1번 문제

# 다음과 같은 무자열이 있다.
# a:b:c:d
# a#b#c#d로 고치시오

# case 1 replace만 사용
a = "a:b:c:d"
a1 = a.replace(":", "#")
print(a1)
# case 2 split과 join 함수 사용
b = "a:b:c:d"
b1=b.split(":")
b2="#".join(b1)
print(b2)


# 2번 문제

# 딕셔너리 값 추출하기
# 다음은 딕셔너리의 a에서 'C'라는 key에 해당하는 value를 출력하는 프로그램이다.
aa = {'A' : 90, 'B' : 80}
# aa['C']
# Traceback (most recent call last):
#   File "D:\코딩\python\0323 ch8.py", line 27, in <module>
#     aa['C']
# KeyError: 'C'
# C : 70 을 딕셔너리에 추가하자

print(dir(dict)) # 생각이 안날 땐 dir 함수로 검색
# ['__class__', '__contains__', '__delattr__',  '__delitem__', '__dir__', '__doc__', '__eq__',
#  '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__',
#  '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__',
#  '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__setitem__', '__sizeof__', '__str__',
#  '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem',
#  'setdefault', 'update', 'values']
aa.update({'C': 70})
print(aa) # {'A': 90, 'B': 80, 'C': 70} 추가 된 것 확인
print(aa['C']) # 70 출력


# 3번 문제

# 리스트의 더하기와 extend 함수
# 다음과 같은 리스트가 있다.
aa1 = [1,2,3]
print(id(aa1)) # 2492698555456
aa1 = aa1 + [4,5]
print (aa1, id(aa1)) # [1, 2, 3, 4, 5] 2492696943936

aa2 = [1,2,3]
print(id(aa2)) # 2492698555456
aa2.extend([4,5])
print(aa2,id(aa2)) # [1, 2, 3, 4, 5] 2492698555456

# 출력되는 결과는 둘 다 동일
# + 로 더한 것은 원래 객체의 id 주소가 변하게 되고
# extend로 추가한 것은 객체의 id 주소가 동일하게 유지 됨을 알 수 있다.



# 4번 문제

# 리스트 총합 구하기
# 다음은 A학급 학생의 점수를 나타내는 리스트이다. 다음 리스트에서 50점 이상 점수의 총합을 구하시오.
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
# print(dir(list))
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop',
# 'remove', 'reverse', 'sort']
result = 0
for i in A:
    if i >= 50 :
        result+=i
print(result) # 481




# 5번 문제

# 피보나치 함수
# 첫 번째 항의 값이 0이고 두번째 항의 값이 1일때, 이후에 이어지는 항은 이전의 두 항을 더한 값으로
# 이루어지는 수열을 피보나치 수열이라고 한다.

# 0,1,1,2,3,5,8,13 .......
# 입력을 정수 n으로 받았을 때, n 이하 까지의 피보나치 수열을 출력하는 함수를 작성해보자

def fib(n) :
    if n == 0 : return 0
    if n == 1 : return 1
    return fib(n-2)+fib(n-1)

for i in range(5):
    print(fib(i))



# 6번 문제

# 사용자로부터 다음과 같은 숫자를 입력 받아 입력 받은 숫자의 총합을 구하는 프로그램을 작성하시오
# 단, 숫자는 콤마로 구분하여 입력한다.

# userint = input("숫자를 입력해 주세요 :  ")
# print(userint)
# userint = userint.split(",")
# print(userint)
# resultint = 0
# for i in userint :
#     i = int(i)
#     resultint += i
# print(resultint)


# 7번 문제

# 한줄 구구단
# 사용자로부터 2~9의 숫자 중 하나를 입력 받아 해당 숫자의 구구단을 한줄로 출력하는 프로그램 작성

# gugu = int(input(":   "))

# for i in range(1,10) :
#     print ((gugu*i), end=" ")
# 3 6 9 12 15 18 21 24 27

# 8번 문제

# 다음과 같은 내용의 파일 abc.txt가 있다.

# AAA
# BBB
# CCC
# DDD
# EEE
# 이 파일의 내용을 역순을 바꾸어 저장하시오.
# data='''AAA
# BBB
# CCC
# DDD
# EEE'''
# f = open("D:/코딩/test/abc.txt", 'w')
# f.write(data)
# f.close()

# # 우선 abc.txt에 내용 저장 완료.

# f=open("D:/코딩/test/abc.txt", 'r')
# lines= f.readlines() # 모든 라인을 다 읽음
# f.close()

# lines.reverse()

# f=open("D:/코딩/test/abc.txt", 'w')
# for line in lines :
#     line = line.strip() # 포함 되어 있는 줄바꿈 문자 제거 # 처음과 끝에 있는 whitespace 삭제
#     f.write(line)
#     f.write('\n')
# f.close()

# 역순 저장 : 정답

# 파일 객체의 readlines를 사용하여 모든 라인을 읽은 후에 reversed를 사용하여 역순으로 정렬한 다음 다시 파일에 저장한다.

# f = open('abc.txt', 'r')
# lines = f.readlines()    # 모든 라인을 읽음
# f.close()

# lines.reverse()          # 읽은 라인을 역순으로 정렬

# f = open('abc.txt', 'w')
# for line in lines:
#     line = line.strip()  # 포함되어 있는 줄 바꿈 문자 제거
#     f.write(line)
#     f.write('\n')        # 줄 바꿈 문자 삽입
# f.close()



# 9번 문제

# 평균값 구하기
# 다음과 같이 총 10줄로 이루어진 sample.txt파일이 있다. sample.txt파일의 숫자 값을 모두 읽어 총합과
# 평균 값을  result.txt파일에 프로그램을 작성하시오.

data1 ='''70
60
55
75
95
90
80
80
85
100'''

f = open("D:/코딩/test/sample.txt", 'w')
f.write(data1)
f.close()

f = open("D:/코딩/test/sample.txt", 'r')
line = f.readlines()
print(line)#['70\n', '60\n', '55\n', '75\n', '95\n', '90\n', '80\n', '80\n', '85\n', '100']
f.close()
# line = f.readlines()
# line = line.strip() # 리스트라 strip 함수를 사용 할 수 없다.
# print(line) # AttributeError: 'list' object has no attribute 'strip'
# 그러면 for 문 사용해서 strip함수를 쓰자


total = 0
aver = 0
for li in line :
    li = li.strip()
    #print(li, end=" ") # 70 60 55 75 95 90 80 80 85 100 \n 문자 삭제 된 것 확인
    total += int(li)
aver = total / len(line)
print(aver)
print(total)

f=open("D:/코딩/test/result.txt", 'w')
f.write("Total amount\n")
f.write(str(total))
f.write('\n')
f.write("Average value\n")
f.write(str(aver)) # write 안에는 str 문자열만 입력 될 수 있다.
f.write('\n')

# Total amount
# 790
# Average value
# 79.0
#
# 평균 값 구하기 # 정답

# f = open("sample.txt")
# lines = f.readlines( )  # sample.txt를 줄 단위로 모두 읽는다.
# f.close( )

# total = 0
# for line in lines:
#     score = int(line)  # 줄에 적힌 점수를 숫자형으로 변환한다.
#     total += score
# average = total / len(lines)

# f = open("result.txt", "w")
# f.write(str(average))
# f.close()



# 10 번 문제

# 사칙연산 계산기
# 다음과 같이 동작하는 클래스 Calculator를 작성하시오.
# >>> cal1 = Calculator([1,2,3,4,5])
# >>> cal1.sum() # 합계
# 15
# >>> cal1.avg() # 평균
# 3.0
# >>> cal2 = Calculator([6,7,8,9,10])
# >>> cal2.sum() # 합계
# 40
# >>> cal2.avg() # 평균
# 8.0

# 클래스 안에 합계, 평균 2가지 함수가 있으면 된다.
# 입력은 리스트로 받는다.

class Cal:
    def __init__(self, num):
        self.num = num
        print(self.num)

    def sum(self) :
        result444=0
        for num in self.num :
            result444 += num
        return result444
    def avg(self) :
        total = self.sum()
        return total / len(self.num)

cal1 = Cal([5,6,7,8,9,10])
print(cal1.sum())
print(cal1.avg())