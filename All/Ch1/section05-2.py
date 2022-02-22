# Section05-2
# 파이썬 흐름제어 (반복문)
# 반복문 실습

# 코딩의 핵심 -> 조건 해결 중요

# 기본 반복문 : for, while

import time
v1 = 1
while v1 < 11:
    print("v1 is :", v1)
    v1 += 1


for v2 in range(10):
    print("v2 is : ", v2)

for v3 in range(1, 11):
    print("v3 is : ", v3)
    time.sleep(0.1)

# 1~100 합
sum1 = 0
cnt1 = 1

while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1
print("1~100 :", sum1)
print("1~100 :", sum(range(1, 101)))  # sum 함수로 간단히 계산 리스트내 인자들을 모두 더해줌
print("1~100 :", sum(range(1, 101, 2)))  # 짝수만 계산

# 시퀀스(순서o) 자료형을 반복 iterable
# 문자열, 리스트,. 튜플, (집합, 사전) [반복 가능]
# iterable 리턴 함수: range(), reversed(), enumerate(), filter(), map(), zip()

names = ['kim', 'Park', "cho", "choi", "Yoo"]

for name in names:
    print("you are : ", name)

word = "dreams"
# 문자열은 immutable, 순서가 있고 한 단어 한 단어가 자기 공간에 맞게 할당이 되어 있다.

for i in word:
    print("you are : ", i)


my_info = {
    "name": "kim",
    "age": 33,
    "city": "Seoul"
}

# 기본 값은 키
for key in my_info:
    print("myinfo", key)

# Value
for key in my_info.values():
    print("myinfo", key)

# 키
for key in my_info.keys():
    print("myinfo", key)

# 키 and 값
for key in my_info.items():
    print("myinfo", key)


# 대문자는 소문자로, 소문자는 대문자로 변경
name = "KennRY"

for n in name:
    if n.isupper():
        print(n.lower())
    else:
        print(n.upper())
# k
# E
# N
# N
# r
# y


# break 문 for 문에서 사용 가능
# 내가 하고자 하는 작업 조건이 맞으면 반복문을 즉시 탈출 할 수 있는 기능
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 37, 15, 34, 36, 38]

# for i in numbers:
#     if i == 33 :
#         print("33이 있다")
#         break
#     else :
#         print(i)
# 33이후에는 for 문을 빠져 나감

# for -else 구문 (반복문이 정상적으로 수행 된 경우 else 블럭 수행.)
for i in numbers:
    if i == 33:
        print("33이 있다")
        break
    else:
        print(i)
else:
    print("Not found 33 ............")
# for 문이 끝나고 작업을 지정해줄수 있다. 좋은 듯..

# continue

lt = ["1", 2, 5, True, 4.3, complex(4)]
for v in lt:
    if type(v) is float:
        continue
    print("타입 : ", type(v))
# continue를만나면 for 문이 다음으로 진행.
# 타입 :  <class 'str'>
# 타입 :  <class 'int'>
# 타입 :  <class 'int'>
# 타입 :  <class 'bool'>
# 타입 :  <class 'complex'>
# 그래서 if 조건에 맞는 float 형만 continue 되서 print 되지 않는다.


name = "niceman"
print(reversed(name))
print(list(reversed(name)))
# ['n', 'a', 'm', 'e', 'c', 'i', 'n']
