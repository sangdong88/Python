# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 = {"봄": "딸기", "여름": "토마토", "가을": "사과"}
for i in q1:
    if i == "가을":
        print(q1[i])

print(q1['가을'])
# 사과

# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 = {"봄": "딸기", "여름": "토마토", "가을": "사과"}
if "사과" in q2.values():
    print("사과 있다.")
# 사과 있다.

print("사과" in q2.values())
# True

for k, v in q2.items():
    if v == " 사과":
        print(k, v)
        break
else:
    print("사과 없음")


# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점
q3 = int(input("score :  "))

if q3 > 80:
    print("A학점")
elif q3 > 60:
    print("B학점")
elif q3 > 40:
    print("C학점")
elif q3 > 20:
    print("D학점")
elif q3 >= 0:
    print("E학점")

# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18
q4 = [12, 6, 18]

q44 = 0
for i in q4:
    if i > q44:
        q44 = i
    else:
        continue
print(q44)

print(max(q4))  # max 함수 안에는 iterable
# 18

# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)
a = "885532-1321233"
b = "213212-2342532"

q5 = [a, b]
for i in q5:

    # str타입을 int 로바꿔 줘야 1과 3이랑 매치가 될 수 있다.
    if int(i[7]) == 1 or int(i[7]) == 3:
        # if int(i[7]) % 2 = 1 :
        print("남자")
    else:
        print("여자")

# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]
for i in q3:
    if i == "정":
        continue
    else:
        print(i)
# 갑
# 을
# 병


# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
for i in range(1, 101, 2):
    print(i, end=' ')
# 1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 51 53 55 57 59 61 63 65 67 69 71 73 75 77 79 81 83 85 87 89 91 93 95 97 99

print()
# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]
for i in q4:
    # print(i)
    # print(len(i))
    if len(i) >= 5:
        print(i)
# study
# python
# anaconda

# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]
for i in q5:
    if i.islower():
        print(i, end=" ")
# b c e h

print()
# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]
q66 = []
for i in q6:
    if i.islower():
        q66.append(i.upper())
    else:
        q66.append(i.lower())
print(q66)
# ['a', 'B', 'C', 'd', 'E', 'f', 'g', 'H']


# 리스트 컴프리핸션

number = []
for n in range(1, 101):
    number.append(n)
print(number)

number2 = [x for x in range(1, 101)]  # 규모가 큰 iterable 자료형을 만들 때 사용.
print(number2)

q33 = ["갑", "을", "병", "정"]
q5 = [x for x in q33 if x != "정"]
print(q5)  # ['갑', '을', '병']

# x = [x for x in range(1,100) if 조건문 ]
# 맨처음 x 는 append 될 것. 마지막에 if 가 추가 되면 if 조건 문 만족 하는 것 만 x로 append 하겠다.
