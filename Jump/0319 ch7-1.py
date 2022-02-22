# 7장 정규표현식

# 필자는 "정규 표현식"을 이 책<<점프 투 파이썬>>에 포함 시켜야 할지 오랜시간 고민했다.
# 왜냐하면 정규 표현식은 꽤 오랜 기간 코드를 작성해 온 프로그래머라도 잘 모를 수 있는
# 고급 주제여서 초보자를 대상을 하는 이 책에서 어울리지 않을 수 있기 때문이다.

# 하지만 정규 표현식을 배워 익히기만 하면 아주 달콤한 열매를 맛볼 수 있다.
# 그래서 파이썬 하우투 https://docs.python.org/3.7/howto/regex.html를 참고하여,
# 그곳에서 소개하는 수준의 내용만이라도 독자들이 이해하고 사용할 수 있도록 노력했다.
# 여러분이 정규 표현식을 잘 다루면 파이썬 외에 또 하나의 강력한 무기를 얻게 되는 것이다.
# 다시 말하지만 프로그래밍 입문자가 이해하기에는 어려운 내용이니 부담갖지말고 편하게 읽어주길 바란다.


# 7장-1 정규 표현식 살펴보기

# 정규 표현식 (Regular Expresstion)은 복잡한 문자열을 처리할 때 사용하는 기법으로,
# 파이썬 고유만의 문법이아니라, 문자열을 처리하는 모든 곳에서 사용한다.
# 정규 표현식을 배우는 것은 파이썬을 배우는 것과는 또 따른 영역의 괒에ㅣ다
# 정규 표현식은 줄여서 간단히 "정규식"이라고도 말한다.

# 정규 표현식은 왜 필요한가 ?
# 다음과 같은 문제가 주어졌다고 가정해 보자.
# 주민등록번호를 포함하고 있는 텍스트가 있다. 이 텍스트에 포함된 모든 주민등록번호의 뒷자리를 
# * 문자로 변경해보자

# 우선 정규식을 전혀 모르면 다음과 같은 순서로 프로그래밍을 작성해야 할 것이다.
# 1. 전체 텍스트를 공백 문자로 나눈다.(split)
# 2. 나뉜 단어가 주민등록번호 형식인지 조사한다
# 3. 단어가 주민번호 형식이라면 뒷자리를 * 로 변환한다.
# 4. 나뉜 단어를 다시 조립한다.

# 이를 구현하는 코드는 아마도 다음과 같을 것이다.

# data = """
# park 800905-1049118
# kim 700905-1059119
# """

# data1 = data.split('\n')
# print(data1)
# #['', 'park 800905-1049118', 'kim  700905-1059119', '']
# data1 = data1[1:3]
# print(data1)

# for i in  data1:
#     i2 = i # 'park 800905-1049118'
#     i3 = i2.split(" ")[1]
#     i4 = i3.split("-")[1]
    
#     print(i3)
#     print(i4)

# 위에 코드는 해답 안보고 trial. 엉망

# .isdigit() # 모든 string이 digit이면 True, 하나라도 아니면 False

# 어떻게 data를 구분 지을지 부터 생각.
# '\n' 으로 나눠서 받자 .split('\n')
# 나눠진 자료들을 한 번더 .split(" ")으로 나눈다. ['park', '800905-1049118']
# 여기서 주민등록 부분 만 인식하여 변수에 저장
# 저장된 변수에서 뒷자리 내용을 치환하면 된다.

# data = """
# park 800905-1049118
# kim 700905-1059119
# """
# result = []
# data1 = data.split('\n')
# for aaa in data1 :
#     result = aaa.split(" ")
#     print(result)
#     for bbb in result:
#         print(bbb)
#         if len(bbb)==14 and bbb[0:6].isdigit() and bbb[7:].isdigit():
#             print(bbb)
#         elif bbb == "":
#             pass
#         else:
#             print(f'{bbb}는이름입니다.')
             # 오케이 논리 구조 확실히 파악 끝 
# ['']

# ['park', '800905-1049118']
# park
# park는이름입니다.
# 800905-1049118
# 800905-1049118
# ['kim', '700905-1059119']
# kim
# kim는이름입니다.
# 700905-1059119
# 700905-1059119
# ['']


# data = """
# park 800905-1049118
# kim 700905-1059119
# """

# result = []
# for ii in data.split('\n'):
#     resultword = []
#     for aa in ii.split(" "): #['park', '800905-1049118']
#         if len(aa) == 14 and aa[0:6].isdigit() and aa[7:].isdigit():
#             aa = aa[0:6] + "-" + "*"*7
#         resultword.append(aa)
#         print (resultword) # ['', 'park', '800905-*******', 'kim', '700905-*******', '']
#     result.append(" ".join(resultword))
#     print(result)
# print("\n".join(result))

# park 800905-*******
# kim 700905-*******


# result = []
# for line in data.split("\n"):
#     word_result = []
#     for word in line.split(" "):
#         if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
#             word = word[:6] + "-" + "*******"
#         word_result.append(word)
#     result.append(" ".join(word_result))
# print("\n".join(result))

# 복잡 했지만 for 문의 섭리를 이해하는데 도움이 되었다.

# 반면에 정규식을 사용하면 다음처럼 훨씬 간편하고 직관적인 코드를 작성할 수 있다.
# 아직 정규식 사용 방법을 배우지 않았으니, 눈으로만 살펴보자

import re

data = """
park 800905-1049118
kim 700905-1059119
"""

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))
# compile(pattern: AnyStr, flags: Union[int, RegexFlag]) -> Pattern[AnyStr]

# park 800905-*******
# kim 700905-*******
# 정규 표현식을 사용하면 이렇게 간단한 예제에서도 코드가 상당히 간결해진다.
# 만약 찾으려는 문자열 또는 바꾸어야 할 문자열의 규칙이 매우 복잡하다면 효용은 더 커진다.
