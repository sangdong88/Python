# 11번 문제

# D:/코딩/test 에 mymod.py 파이썬 모듈이 있다고 가정해 보자.
# 명령 프롬프트 창에서 파이썬 셀을 열어 이모듈을 import해서 사용할 수 있는 방법을 모두 기술하시오.
# 즉 다음과 같이 import mymod를 수행할때 오류가 없어야 한다.

# 우선 import 시에 검색 되게 하려면 경로를 수정해 줘야 한다.
# import sys
# sys.path.append("D:/코딩/test") # 로 디렉터리 지정해줘야 test 경로 안에 있는 mymod 모듈을
# import 할 수 있다.
# 이건 if __name__ = __main__ 을 해줘야 import

# 1) sys 모듈 사용하기

# 다음과 같이 sys.path 에 C:\doit 이라는 디렉터리를 추가하면 C:\doit 이라는 디렉터리에 있는 mymod 모듈을 사용할 수 있게 된다.

# >>> import sys
# >>> sys.path.append("c:/doit")
# >>> import mymod
# 2) PYTHONPATH 환경 변수 사용하기

# 다음처럼 PYTHONPATH 환경 변수에 C:\doit 디렉터리를 지정하면 C:\doit 디렉터리에 있는 mymod 모듈을 사용할 수 있게 된다.

# C:\Users\home>set PYTHONPATH=c:\doit
# C:\Users\home>python
# >>> import mymod
# 3) 현재 디렉터리 사용하기

# 파이썬 셸을 mymod.py가 있는 위치로 이동하여 실행해도 mymod 모듈을 사용할 수 있게 된다. 왜냐하면 sys.path 에는 현재 디렉터리인 . 이 항상 포함되어 있기 때문이다.

# C:\Users\home>cd c:\doit
# C:\doit>python
# >>> import mymod


# 12번문제

# 오류와 예외 처리
# 다음 코드의 실행 결과를 예측하고 그 이유에 대해 설명하시오.

# result = 0

# try:
#     [1, 2, 3][3]
#     "a"+1
#     4 / 0
# except TypeError:
#     result += 1
# except ZeroDivisionError:
#     result += 2
# except IndexError:
#     result += 3
# finally:
#     result += 4

# print(result) # 7

# result 는 7이 출력
# 순서상 제일 먼저 [1, 2, 3][3] 이 실행 될 것이고, IndexError 가 발생하게 된다.
# result = 3 이 더해지고
# finally 부분으로 이동 3+4가 되어 최종 7이 출력 된다.

# 13번 문제

# DashInsert 함수
# DashInsert 함수는 숫자로 구성된 문자열을 입력받은 뒤 문자열 안에서 홀수가 연속되면
# 두 수 사이에 - 를 추가하고, 짝수가 연속되면 * 를 추가하는 기능을 갖고 있다. DashInsert 함수를 완성하시오.

# 입력 예시: 4546793
# 출력 예시: 454*67-9-3

# abc = input("숫자를 입력 하세요 :    ")
# abc1 = list(map(int,abc)) # 숫자 문자열을 숫자 리스트로 변경 리스트로 받을때 (map(int, ...))사용
# print(abc1,type(abc1)) # [4, 5, 4, 6, 7, 9, 3] <class 'list'>
# # 그럼 이제 숫자형을 바뀐 리스트가 되고
# # 함수를 짜볼 텐데 for 문으로 반복 하고
# # 리스트의 인덱싱을 해주는 enumerate() 함수를 사용 해보자

# result = [] # 결과를 저장할 리스트 생성.
# for i, num in enumerate(abc1) :
#     result.append(str(num))        # 최종결과물은 문자열이므로 str 로 변경하여 result.append
#     if i < len(abc1)-1 : # 다음 수가 있다면
#         odd = abc1[i]
#         nextodd = abc1[i+1] # 다음 수를 미리 알 수 있구나 abc는 이미 for문 밖에서 정해져있으니
#         if odd % 2 == 1 and nextodd % 2 ==1 :
#             result.append("-")
#         if odd % 2 == 0 and nextodd % 2 ==0 :
#             result.append("*")

# print(result)
# # ['4', '5', '4', '*', '6', '7', '-', '9', '-', '3']
# print("".join(result)) # 454*67-9-3


# 문제풀이
#다음 프로그램의 주석문을 참고하자.

# data = "4546793"
# numbers = list(map(int, data))   # 숫자 문자열을 숫자 리스트로 변경
# print (numbers)
# result = []

# for i, num in enumerate(numbers):
#     result.append(str(num))
#     if i < len(numbers)-1:                   # 다음 수가 있다면
#         is_odd = num % 2 == 1                # 현재 수가 홀수
#         is_next_odd = numbers[i+1] % 2 == 1  # 다음 수가 홀수
#         if is_odd and is_next_odd:           # 연속 홀수
#             result.append("-")
#         elif not is_odd and not is_next_odd: # 연속 짝수
#             result.append("*")

# print("".join(result))



# 14번 문제

# 문자열 압축하기
# 문자열을 입력 받아 같은 문자가 연속적으로 반복되는 경우에 그 반복 횟수를 표시해 문자열을 압축해서 표시하시오
# 입력 예시: aaabbcccccca
# 출력 예시: a3b2c6a1

# bbc = input("문자를 입력 하세요 :    ")
# bbc1 = list(map(str,bbc)) # 숫자 문자열을 숫자 리스트로 변경 리스트로 받을때 (map(int, ...))사용
# print(bbc1,type(bbc1))
# # ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'c', 'a'] <class 'list'>

# def compress_string(s):
#     blank = ""
#     print(blank) # 아무것도 없음 # 빈 문자열 의미
#     cnt = 0
#     result = ""
#     for c in s:
#         if c != blank:
#             blank = c
#             if cnt:
#                 result += str(cnt)
#             result += c
#             cnt = 1
#         else:
#             cnt +=1
#     if cnt:
#         result += str(cnt)
#     return print(result)

# compress_string(input("문자입력 :  ")) # a3b2c6a1 출력

# 이 문제를 해결 하기 위해서는 아이디어가 좀 필요 했음
# 빈 문자열 1개를 이용하여, 입력 되는 문자와 같다면, 카운트를 1 올리고,
# 다르면 빈 문자열을 새로입력된 문자로 교체 하고 기존의 카운트를 결과로 보낸다.
# 그리고 카운트는 다시 1로 만들어 준다.
# 다시 한 번 작성해보자

def zip (s):
    blank = "" # 빈 문자열 1개 생성, for 문에서 차례로 들어오는 문자와 대조하는 key로 쓸 예정
    cnt = 0
    result = "" # 출력되는 결과를 저장할 result 변수도 생성
    # 이제 for 문을 작성해보자
    # Keypoint는 blank에서 가진 값과 다른 값이 들어 왔을때 어떻게 처리 하는가 ? 이다.
    for c in s :
        if c != blank : # 다른 문자가 들어온다면
            blank = c # 새로운 문자를 blank에 저장해준다.
            if cnt :
                result += str(cnt)
            result += c
            cnt = 1
        else :
            cnt += 1
    if cnt:
        result += str(cnt)
    return print(result)
zip("aaabbcccccca") # a2b3c5a1 출력 되는 값을 받을 수 있다
# zip(input("문자입력 :  ")) # a2b3c5a1 출력 되는 값을 받을 수 있다


# 15번 문제

# Q15 Duplicate Numbers
# 0~9의 문자로 된 숫자를 입력받았을 때, 이 입력값이 0~9의 모든 숫자를 각각 한 번씩만
# 사용한 것 인지 확인하는 함수를 작성하시오.

# 입력 예시: 0123456789 01234 01234567890 6789012345 012322456789
# 출력 예시: True False False True False


def dupli (s):
    cnt = 0
    for i in s :
        if s.count(i) == 1:
            cnt += 1
        # else :
        #     return False # 이걸 가려도 동작
    return cnt == 10 # 이렇게 하니까 자동으로 Trueaaabbcccccca False 판정 가능이네

print(dupli("0123456799"))

# 문제 풀이
def chkDupNum(s):
    result = []
    for num in s:
        if num not in result:
            result.append(num)
        else:
            return False
    return len(result) == 10

# print(chkDupNum("0123456789"))      # True 리턴
# print(chkDupNum("01234"))           # False 리턴
# print(chkDupNum("01234567890"))     # False 리턴
# print(chkDupNum("6789012345"))      # True 리턴
# print(chkDupNum("012322456789"))    # False 리턴
# 리스트 자료형을 사용하여 중복된 값이 있는지 먼저 조사한다.
# 중복된 값이 있을 경우는 False를 리턴한다.
# 최종적으로 중복된 값이 없을 경우 0~9까지의 숫자가 모두 사용되었는지 판단하기 위해
# 입력 문자열의 숫자 값을 저장한 리스트 자료형의 총 개수가 10인지를 조사하여
# 10일 경우는 True, 아닐 경우는 False를 리턴한다.


# 16번 문제

# Q16 모스 부호 해독
# 문자열 형식으로 입력받은 모스 부호(dot:. dash:-)를 해독하여 영어 문장으로 출력하는 프로그램을 작성하시오.

# 글자와 글자 사이는 공백 1개, 단어와 단어 사이는 공백 2개로 구분한다.
# 예를 들어 다음 모스 부호는 "HE SLEEPS EARLY"로 해석해야 한다.
# .... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--
# 모스부호 규칙 표

# 문자	부호	문자	부호
# A	    .-	    N	    -.
# B	    -...	O	    ---
# C	    -.-.	P	    .--.
# D	    -..	    Q	    --.-
# E	    .	    R	    .-.
# F	    ..-.	S	    ...
# G	    --.	    T	    -
# H	    ....	U	    ..-
# I	    ..	    V	    ...-
# J	    .---	W	    .--
# K	    -.-	    X   	-..-
# L	    .-..	Y	    -.--
# M	    --	    Z	    --..

# 딕셔너리 쓰라는 말 같은데
dic = {
    '.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F',
    '--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L',
    '--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R',
    '...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X',
    '-.--':'Y','--..':'Z'
}

def morse(src):
    result = []
    for word in src.split("  "):
        for char in word.split(" "):
            result.append(dic[char]) # dic[key] = value
        result.append(" ") # 단어 끝마다 한칸 띄우기 위해
        print(result)
    return "".join(result)


print(morse('.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'))







dic = {
    '.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F',
    '--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L',
    '--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R',
    '...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X',
    '-.--':'Y','--..':'Z'
}

# 모스 부호를 입력 할 것이고, 단어 사이는 2칸, 글자사이는 1칸으로 띄어서 입력함
# 입력 받은 모스부호를 영어로 출력해보자
# ('.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--') 입력 할 모스 부호.

# 함수로 시작

def mos(s):
    result = [] # 일단 for 문을 통과한 단어들을 result로 담아 둔다.
    for word in s.split("  ") :
        for char in word.split(" "):
            result.append(dic[char]) # dic[char]를 하면 key에 맞는 value 즉 번역된 영문이 나옴
        # 단어가 끝나면 띄어쓰기를 위해 공백 1개 추가
        result.append(" ")
    return print("".join(result)) # 리스트를 "".join 하면 문자열로 출력
# join 함수는 매개변수로 들어온 리스트에 있는 요소 하나하나를 합쳐서
# 하나의 문자열로 바꾸어 반환하는 함수입니다.
# 아 join 함수는 그러니까 구분자.join(list)형을 문자열로 만들어 준다는 것
# 문자열로 만들 때 리스트 객체 사이사이에 구분자를 넣겠다라는것이고
# "".join(list)는 객체와객체를 바로 붙이겠다. 띄우지 않겠다라는 것이다.
mos('.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--')


# 17번 문제

# Q17 기초 메타 문자
# 다음 중 정규식 a[.]{3,}b과 매치되는 문자열은 무엇일까?

# a로 시작한다.
# [.]은 문자dot이 와야 한다.
# {3,} 3개 이상 # 즉 문자 dot가 3개이상일것
# 마지막은 b
data = '''
acccb
a....b # 매치 되는 정답은 2 번째
aaab
a.cccb
'''
import re
p = re.compile(r'a[.]{3,}b', re.MULTILINE)
m = p.findall(data)
print(m)
# ['a....b'] 정답 출력



# 18번 문제

# Q18 문자열 검색
# 다음 코드의 결괏값은 무엇일까?

# >>> import re
# >>> p = re.compile("[a-z]+")
# >>> m = p.search("5 python")
# >>> m.start() + m.end()


p1= re.compile('[a-z]+')
m1 = p1.search("5 python")
print(m1) # <re.Match object; span=(2, 8), match='python'>
#(python)
print(m1.start()) # 2
print(m1.end()) # 8
print(m1.start() + m1.end()) # 10



# 19번 문제

# Q19 그루핑
# 다음과 같은 문자열에서 휴대폰 번호 뒷자리인 숫자 4개를 ####로 바꾸는 프로그램을
# 정규식을 사용하여 작성하시오.

data = """
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768
"""

p2 = re.compile(r'\w+\s\d+[-]\d+[-](?P<name>\d+)', re.MULTILINE)
m2 = p2.findall(data)
print(data)
#
# park 010-9999-9988
# kim 010-9909-7789
# lee 010-8789-7768
#
p2 = re.compile(r'\w+\s\d+[-]\d+[-](?P<name>\d+)')
m2 = p2.search(data)
print(data)
#
# park 010-9999-9988
# kim 010-9909-7789
# lee 010-8789-7768
#
# 결과는 동일하다.

p2 = re.compile(r'(?P<sup>\w+\s\d+[-]\d+)[-](?P<name>\d+)', re.MULTILINE)
print(p2.sub('\g<sup>-****', data))

# park 010-9999-****
# kim 010-9909-****
# lee 010-8789-****


import re

s = """
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768
"""

pat = re.compile("(\d{3}[-]\d{4})[-]\d{4}")
result = pat.sub("\g<1>-####", s)

print(result)

# park 010-9999-####
# kim 010-9909-####
# lee 010-8789-####



# 20번 문제

# Q20 전방 탐색
# 다음은 이메일 주소를 나타내는 정규식이다.
# 이 정규식은 park@naver.com, kim@daum.net, lee@myhome.co.kr 등과 매치된다.
# 긍정형 전방 탐색 기법을 사용하여 .com, .net이 아닌 이메일 주소는 제외시키는 정규식을 작성하시오.

# .*[@].*[.].*$

# 전방 탐색

# .com과 .net에 해당되는 이메일 주소만을 매치하기 위해서 이메일 주소의 도메인
# 부분에 다음과 같은 긍정형 전방탐색 패턴을 적용한다.

# pat3 = re.compile(".*[@].*[.](?=com$|net$).*$")
# 다음은 위 패턴을 적용한 파이썬 코드이다.

import re

pat3 = re.compile(".*[@].*[.](?=com$|net$)")
# 이렇게 하니 일치하는  역시나 소비되지 않고 나머지 값만 출력 (출력안됨)

print(pat3.match("pahkey@gmail.com"))
# <re.Match object; span=(0, 13), match='pahkey@gmail.'>
m33 = pat3.match("pahkey@gmail.com")
print(m33.group())
# pahkey@gmail.
print(pat3.match("kim@daum.net"))
# <re.Match object; span=(0, 9), match='kim@daum.'>
print(pat3.match("lee@myhome.co.kr"))
# None 형식이 맞지않아 matching 실패

