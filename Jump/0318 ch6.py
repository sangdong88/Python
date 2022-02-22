# 6장 파이썬 프로그래밍, 어떻게 시작해야 할까 ?
# 6장에서는 아주 짤막한 스크립트와 함수들을 만들어본다. 아마 프로그래밍 감각을 키우는 데
# 더할 나위 없이 좋은 재료가 될 것이다. 스크립트란 에디터로 작성한 파이썬 프로그램 파일을 말한다.
# 앞으로는 에디터로 작성한 파이썬 프로그램파일을 파이썬 스크립트라고 부를 것이니 혼동하지말자
# 이 장에 소개된 모든 파이썬 프로그램 예제는 대화형 인터프리터가 아닌 에디터로 작성해야 한다.

# 6장-1 내가 프로그램을 만들 수 있을까 ?

# 프로그램을 막 시작하려는 사람이 맨 먼저 부딪히게 되는 벽은 아마도 다음과 같지 않을까?
# 어떤 프로그램을 짜야지 라는 생각보다는 다른 사람들이 만든 프로그램 파일을 자세히 들여다 보고
# 분석하는 데서 시작하는 것이 좋다. 그러다 보면 다른 사람들의 생각도 읽을 수 있고 거기에 더해
# 뭔가 새로운 아이디어가 떠오를 수도 있다. 하지만 여기에서 가장 중요한 것은 자신의 수준에 맞는
# 소스를 찾는일이다. 그래서 이 장에서는 아주 쉬운 예제부터 시작해서 차츰 수준을 높여 실용적인
# 예제까지 다루려고 노력하였다. 배운내용을 어떻게 활용하는 가는 독자의 몫이다.

# 필자는 예전에 프로그래밍을 막 시작한 사람에게 구구단 프로그램을 짜 보라고 한 적이 있다.
# 쉬운 과제이고 파이썬 문법도 다 공부한 사람이었는데 프로그램을 어떻게 만들어야 할지 갈피를 못잡더라

# 프로그램을 만들려면 가장 먼저 "입력"과 "출력"을 생각하라.

# 함수 이름은? GuGu로 짓자
# 입력받는 값은? 2
# 출력하는 값은? 2단(2, 4, 6, 8, …, 18)
# 결과는 어떤 형태로 저장하지? 연속된 자료형이니까 리스트!

# 1. 먼저 에디터를 열고 result = GuGu(2)를 입력한다. "입력"
# 2. 결과 값을 어떻게 받을 것인지 고민... 리스트 자료형으로 받자 [2,4.6.8.10,...]
# 3. GuGu로 이름 지은 함수를 만든다
# def GuGu (x):
#     print(x)
# GuGu(2) # >>>2 출력 확인
# 4. 이제 결과값을 담을 리스트를 하나 생성하자. print(x)는 함수 동작 확인용이니 지워도 좋다.
# 5. 리스트에 요소를 추가하는 .append()함수를 사용
# def GuGu (x):
#     result = [] # 리스트 생성
#     result.append(x*1)
#     result.append(x*2)
#     result.append(x*3)
#     result.append(x*4)
#     result.append(x*5)
#     result.append(x*6)
#     result.append(x*7)
#     result.append(x*8)
#     result.append(x*9)
#     return print(result)
# GuGu(2) # [2, 4, 6, 8, 10, 12, 14, 16, 18] 출력
# 6. 반복이 많다. 반복문을 사용해서 줄여보자
# def GuGu(x):
#     result = []
#     for i in range(1,10) :
#         result.append(x * i)
#     return print(result)
# GuGu(2) # [2, 4, 6, 8, 10, 12, 14, 16, 18]
# 이런식으로 복잡한 함수를 만들 때는 위와 같이 구체적이고 단계적으로 접근하는 방식이 매우 도움이 된다.
# 프로그래밍을 할 땐 매우 구체적으로 접근해야 머리가 덜 아프다는 것을 기억하자



# 6장-2 3과 5의 배수 합하기
# 자, 다음 문제를 어떻게 풀면 좋을지 생각해 보자
# 10 미만의 자연수에서 3과 5의 배수를 구하면 3, 5, 6, 9이다. 이들의 총합은 23이다.
# 1000 미만의 자연수에서 3의 배수와 5의 배수의 총합을 구하라.

def cal ():
    result = []
    for i in range(1000):
        if i % 3 == 0:
            result.append(i)
        elif i % 5 == 0 :
            result.append(i)
        else :
            pass
    # print(result)
    print(sum(result))
cal()

result1 = 0
for n in range(1, 1000):
    if n % 3 == 0 or n % 5 == 0:
        result1 += n
print(result1)

print ("*"*40) # 줄 바꿈


# 6장-3 게시판 페이징하기
# A씨는 게시판 프로그램을 작성하고 있다. 그런데 게시물의 총 건수와 한 페이지에 보여 줄
# 게시물 수를 입력으로 주었을 때 총 페이지 수를 출력하는 프로그램이 필요하다.
# 이렇게 게시판의 페이지 수를 보여주는 것을 "페이징"한다고 부른다.

# 함수이름은 ? page
# 입력 받는 값은 ? 게시물의 총 건수(m), 한 페이지에 보여줄 게시물 수(n)
# 출력하는 값은 ? 총페이지 수

# A씨가 필요한 프로그램을 만들기 위해 입력 값과 결과 값이 어떻게 나와야 하는지 먼저 살펴보자
# 게시물의 총 건수가 5건이고 한 페이지 에서 보여줄 게시물 수가 10이면 총 페이지 수는 1이된다.
# 만약 게시물의 총 건수가 15이고 한 페이지 에서 보여줄 게시물 수가 10이라면 총 페이지 수는 2가 된다.
# 게시물의 총 건수(m)	페이지당 보여줄 게시물 수(n)	총 페이지 수
# 5	    10	1
# 15	10	2
# 25	10	3
# 30	10	3

# 이 문제는 게시판 프로그램을 만들 때 가장 처음 마주치는 난관이라고 할 수 있는 총 페이지수를
# 구하는 문제이다. 사실 실제 업무에서 사용하는 페이징 기술은 훨씬 복잡한데 여기에서는
# 그중 가장 간단한 총 페이지 수를 구하는 방법에 대해서만 알아보겠다.

# 올림 함수 math.ceil(x)
import math
def page(m, n):
    return print(math.ceil(m/n))
print(page(9,3))



# 6장-4 간단한 메모장 만들기

# 원하는 메모를 파일에 저장하고 추가 및 조회가 가능한 간단한 메모장을 만들어 보자.
# 필요한 기능은 ? 메모 추가하기, 메모 조회하기
# 입력 받는 값은 ? 메모 내용, 프로그램 실행 옵션
# 출력하는 값은 ? memo.txt

# 가장 먼저 해야 할 일은 메모를 추가하는 것이다.
# 다음 명령을 실행 했을 때 메모를 추가할 수 있도록 만들어 보자.
# python memo.py -a "Life is too short"
# memo.py는 우리가 작성할 파이썬 프로그램 이름이다. 위치 D:/코딩/Mymod
# -a는 이 프로그램의 실행 옵션이고, "Life is too short" 추가할 내용

# D:/코딩/Mymod/memo.py
# import sys

# a = sys.argv
# # a[0]은 파일이름 memo.py
# option = a[1]


# if option == '-a':
#     memo = a[2]
#     f = open("D:/코딩/Mymod/memo.txt",'a')
#     f.write(memo)
#     f.write('\n')
#     f.close()

# elif option == '-v':
#     f = open("D:/코딩/Mymod/memo.txt") # open에 옵션을 지정하지 않으면 자동 읽기 모드
#     memo=f.read()
#     f.close
#     print(memo)
# else :
#     print(TypeError)



# PS D:\코딩\mymod> python memo.py -a "Life is too short"
# -a
# Life is too short

# 그 다음 옵션 -a에 대한 action을 지정하여 준다.
# if 문을 사용하여 a[1]의 값이 '-a'가 입력 된다면,
# memo.txt를 추가하기 모드로 열어 memo 내용을 추가하고 file을 닫는다.

# 이제 작성한 메모를 출력하는 부분을 만들 차례이다. 메모 출력은 다음과 같이 동작하도록 만들어 보자
# python memo.py -v
# 이 말은 option = a[1]이 -v 일때 if 문이 필요하고 거기서 메모 출력을 해줘야 한다.

# python memo.py -v 라고 입력하면 sys.argv[2]항목의 입력값은 없다.
# 그래서 아래 처럼 오류 발생.
# memo는 -a 모드에서 추가할때만 필요하니 if '-a' 문 밑으로 이동.

# Traceback (most recent call last):
#   File "D:\코딩\mymod\memo.py", line 6, in <module>
#     memo = a[2]
# IndexError: list index out of range





# 6장-5 탭을 4개의 공백을 바꾸기

# 이번에는 문서 파일을 읽어서 그 문서 파일 안에 있는 탭(tab)을 공백 (space) 4개로 바꿔 주는
# 스크립트를 작성해보자.

# 다음과 같은 형식으로 프로그램이 수행되도록 만들 것이다.
# python tabto4.py src dst

# tabto4.py는 우리가 작성해야 할 파이썬 프로그램 이름이고 src는 탭을 포함하고 잇는 원본 파일이름이다.
# dst는 파일 안의 탭을 공백 4개로 변환한 결과를 저장할 파일이름이다.

# 예를 들어 a.txt 파일에 있는 탭을 4개의 공백으로 바꾸어 b.txt 파일에 저장하고 싶다면 다음과 같이 수행해야한다.
# python tabto4.py a.txt b.txt

# 1. 다음과 같이 tabto4.py 파일을 작성해 보자
# tabto4.py는 D:/코딩/Mymod 에 저장한다.

# import sys
# src = sys.argv[1]
# dst = sys.argv[2]

# print (src)
# print (dst)

# PS D:\코딩\mymod> python tabto4.py a.txt b.txt
# a.txt
# b.txt
# 입력으로 전달한 a.txt와 b.txt가 정상적으로 출력되는 것을 확인 할 수 있다.

# 테스트를 위한 원본 파일(탭을 포함하는 파일)인 a.txt를 다음과 같이 작성한다.
# 각 단어는 탭(\t)문자로 분리되도록 입력해야 한다.
# 이건 txt 메모장에서 직접 탭으로 입력해야 \t이 인식이 된다.
# 파이썬에서 a.txt 파일만들고 백 날 해봐야 인식 못함 ㅡㅡ
# c:/doit/tabto4.py

# import sys

# a = sys.argv[1]
# b = sys.argv[2]

# f = open(a)
# tab_content = f.read()
# f.close()

# space_content = tab_content.replace("\t","*"*4)
# print(tab_content.find("\t"))
# print(space_content)

# f = open(b,'w')
# f.write(space_content)
# f.close()

# a = "Life\tis\ttoo\tshort"
# print(a)
# b=a.replace('\t',"*"*3)
# print(a.find('\t'))
# print(b)



# 6장-6 하위 디렉터리 검색하기

# 특정 디렉터리 부터 시작해서 그 하위 모든 파일 중 파이썬 파일(*.py)만 출력해주는
# 프로그램을 만들려면 어떻게 해야 할까 ?

# 1. 다음과 같이 subdirsearch.py 파일을 작성해보자

# def search(dirname):
#     print(dirname)

# print(search("D:/"))

# search 함수를 만들고 시작 디렉터리를 입력 받도록 코드를 작성했다.

# 2. 이제 이 디렉터리에 있는 파일을 검색할 수 있도록 소스를 변경해보자.

# import os
# def search(dirname):
#    filenames = os.listdir(dirname) 
#    # os.listdir 함수는 해당 경로에 있는 항목들을 list로 돌려준다. 숨김 처리된 파일도 보여줌
#    #['$RECYCLE.BIN', 'BOkdxInv0h_CR_EDR', 'Creoview', 'Desktop', 'Favorites', 'local', 'pagefile.sys', 'performance sheet macro file', 'Report', 'System Volume Information', '코딩', '코딩zOkdxInv0h_CR_EDR']
#    print(filenames)
#    for filename in filenames:
#        full_filename = os.path.join(dirname, filename)
#        # os.path.join() 경로를 병합하여 새로운 경로 생성
#        # 디렉터리와 파일이름을 이어주는 함수 전체 경로를 쉽게 구할 수 있음
#        # "구분자".join() join ()안에 str을 구분자를 기준으로 합침
#        print(full_filename)
# search("D:/")

# 3. 이제 D:/ 디렉터리에 있는 파일들 중 확장자가 .py 인 파일만을 출력하도록 변경해보자

# import os
# def search(dirname):
#     filenames = os.listdir(dirname) 
#     print(filenames)
#     for filename in filenames:
#         full_filename = os.path.join(dirname, filename)
#         ext = os.path.splitext(full_filename)[-1]
#          # os.path.splitext(경로) 하면 (확장자 전 후로 split 해준다.)
#          # 확장자만 따로 받고 싶을 때 사용. 내용은 tuple로 저장되며 마지막 순서
#          # 따라서 ext만 인덱싱할때는 [-1] 사용
#           # D:/pagefile.sys
#          # ('D:/pagefile', '.sys')
#         if ext == ".py":
#             print(full_filename)
# search("D:/")

# 4. 하지만 우리가 원하는 것은 D:/ 디렉터리 바로 빝에 잇는 파일 뿐만 아니라 그 하위 디렉터리
# sub directory를 포함한 모든 파이썬 파일을 검색하는 것이다. 하위 디렉터리도 검색하도록 코드 변경

import os
def search(dirname):
    try: 
        # try except로 감싸는 이유는 os.listdir를 수행할 때 권한이 없는 디렉터리에 접근하더라도
        # 프로그램이 오류로 종료되지 않고 그냥 수행 되도록하기 위해서이다.
        filenames = os.listdir(dirname)
                # print(filenames)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                # 디렉터리 경로가 존재하는지 체크 즉, 디렉터리인지 확인하는 것
                # 재귀 호출이란 자기 자신을 다시 호출하는 프로그래밍 기법이다.
                # 이 코드에서 보면 search 함수에서 다시 자신 search 함수를 호출하는 것이 재귀호출
                search(full_filename)
                # 디렉터리가 맞다면 search 함수 다시 돌려 (재귀 함수)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.py':
                    print(full_filename)
    except PermissionError:
        pass
    
search("D:/")
print("*"*40) # 줄바꿈
# 하위 디렉터리 검색을 쉽게 해주는 os.walk

# os.walk를 사용하면 위에서 작성한 코드를 보다 간편하게 만들 수 있다. os.walk는 시작 디렉터리부터
# 그 하위 모든 디렉터리를 차례대로 방문해주는 함수이다.

print(tuple(os.walk("D:/")))

import os
for (path, dir, files) in os.walk("D:/"):
# 이런 식으로 os.walk(경로)에 있는 모든 하위 디렉터리 및 모든 파일이 튜플형태로 출력.
# 튜플 안에서 path, dir, file 3가지로 구분되어지며, 항목들은 리스트형으로 묶인다.
# 따라서 for 문 에서 받아야 하는 항목은 총 3개이며 tuple 지정이 필요한 것
# ('D:/코딩', ['.vscode', 'code', 'python', 'test'], [])
# ('D:/코딩\\.vscode', [], ['tasks.json'])
# ('D:/코딩\\code', [], ['j.ipynb', 'test11.txt'])
    for file in files :
        # 마지막 files의 리스트에서 하나 씩 file로 추출.
        ext1 = os.path.splitext(file)[-1]
        # os.path.splitext 확장자 분리 함수를 사용.
        if ext1 == '.py':
            print(f'{path}{file}')