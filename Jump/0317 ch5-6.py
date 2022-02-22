# 라이브러리

# 전 세계 파이썬 사용자들이 만든 유용한 프로그램을 모아 놓은 것이 바로 파이썬 라이브러리이다.
# 모든 라이브러리를 다 알 필요는 없고, 어떤 일을 할 때 어떤 라이브러리를 사용해야 한다는 정도만 알면 된다.
# 자주 사용 되고 꼭 알아 두면 좋은 라이브러리를 중심으로 하나씩 살펴보자.

# sys

# sys모듈은 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈이다
# 명령 행에서 인수 전달하기 -> sys.argv
# testing.py
# import sys
# print(sys.argv)

# D:\코딩\Mymod>python testing.py asd dnd ddd
# ['testing.py', 'asd', 'dnd', 'ddd']

# python 명령어 뒤의 모든 것들이 공백을 기준으로 나뉘어서 sys.argv 리스트의 요소가 된다.

# ※ 명령 프롬프트 창에서는 /, \든 상관없지만, 소스코드 안에서는 반드시 / 또는 \\ 기호를 사용해야 한다.

# 강제로 스크립트 종료하기 - sys.exit

# >>> sys.exit()
# sys.exit는 Ctrl+Z나 Ctrl+D를 눌러서 대화형 인터프리터를 종료하는 것과 같은 기능을 한다. 프로그램 파일 안에서 사용하면 프로그램을 중단시킨다.

# 자신이 만든 모듈 불러와 사용하기 - sys.path

# sys.path는 파이썬 모듈들이 저장되어 있는 위치를 나타낸다. 즉 이 위치에 있는 파이썬 모듈은 경로에 상관없이 어디에서나 불러올 수 있다.

# 다음은 그 실행 결과이다.

# >>> import sys
# >>> sys.path
# ['', 'C:\\Windows\\SYSTEM32\\python37.zip', 'c:\\Python37\\DLLs', 
# 'c:\\Python37\\lib', 'c:\\Python37', 'c:\\Python37\\lib\\site-packages']
# >>>
# 위 예에서 ''는 현재 디렉터리를 말한다.

# # path_append.py
# import sys
# sys.path.append("C:/doit/mymod")
# 위와 같이 파이썬 프로그램 파일에서 sys.path.append를 사용해 경로 이름을 추가할 수 있다. 이렇게 하고 난 후에는 C:/doit/Mymod 디렉터리에 있는 파이썬 모듈을 불러와서 사용할 수 있다.

# pickle
# pickle은 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈이다
# 다음 예는 pickle 모듈의 dump 함수를 사용하여 딕셔너리 개체인 data를 그대로 파일에 저장하는 방법을 보여준다.

# import pickle   # 피클은 항시 binary로 선택
# f = open("test.txt",'bw')
# data = ({1:'python', 2:'you need'},[1,2,3],"python",123)
# pickle.dump(data,f)
# f.close()

# f = open("test.txt",'bw')
# data = pickle.load(f)
# print (data)

# f1 = open("test123.txt",'wb')
# a = "우리들 마음에 빛이 있다면"
# a1 = a.encode("UTF-8")
# f1.write(a1)
# f1.close()

# f1 = open("test123.txt",'wb')
# a = "We need a python"
# a1 = a.encode("ascii")
# f1.write(a1)
# f1.close()

# binary란 컴퓨터가 인식 할수 있는 이진수로 된 data를 말함.
# 따라서 text 형과 binary 형은 다른 형태이며, 용도와 목적에 따라 binary형으로 data 저장 할 것인지 선택해야 함.
# 문자형 자료를 binary 형으로 변환 하려면 encode 함수를 사용하면 된다.
# 영문은 "ascii", "UTF-8"코드를 사용하여 변경 하면 되고, 한글은 "UTF-8"코드를 사용.

# os

# os 모듈은 환경 변수나 디렉터리, 파일 등의 os 지원을 제어할 수 있게 해주는 모듈이다.
# 내 시스템의 환경 변수값을 알고 싶을 때. - os environ
# 시스템은 제각기 다른 환경 변수 값을 가지고 있는데, os.environ은 현재 시스템의 환경 변수 값을 보여 준다. 다음을 따라 해 보자.

# >>> import os
# >>> os.environ
# environ({'PROGRAMFILES': 'C:\\Program Files', 'APPDATA': … 생략 …})
# >>>
# 위 결괏값은 필자의 시스템 정보이다. os.environ은 환경 변수에 대한 정보를 딕셔너리 객체로 돌려준다. 자세히 보면 여러 가지 유용한 정보를 찾을 수 있다.

# 돌려받은 객체가 딕셔너리이기 때문에 다음과 같이 호출할 수 있다. 다음은 필자 시스템의 PATH 환경 변수 내용이다.
# >>> os.environ['PATH'] # 키를 입력
# 'C:\\ProgramData\\Oracle\\Java\\javapath;...생략...'

# 디렉터리 위치 변경하기 - os.chdir
# os.chdir를 사용하면 다음과 같이 현재 디렉터리 위치를 변경할 수 있다.
# >>> os.chdir("C:\WINDOWS")

# 디렉터리 위치 돌려받기 - os.getcwd
# os.getcwd는 현재 자신의 디렉터리 위치를 돌려준다.
# >>> os.getcwd()
# 'C:\WINDOWS'

# 시스템 명령어 호출하기 - os.system
# 시스템 자체의 프로그램이나 기타 명령어를 파이썬에서 호출할 수도 있다. os.system("명령어")처럼 사용한다. 다음은 현재 디렉터리에서 시스템 명령어 dir을 실행하는 예이다.

# >>> os.system("dir")
#  D 드라이브의 볼륨: Data
#  볼륨 일련 번호: 4C8C-9E68

#  D:\코딩 디렉터리

# 2021-03-17  오전 10:41    <DIR>          .
# 2021-03-17  오전 10:41    <DIR>          ..
# 2021-03-10  오전 08:06    <DIR>          .vscode
# 2021-03-17  오전 09:35    <DIR>          code
# 2021-03-17  오전 09:43    <DIR>          Mymod
# 2021-03-11  오전 10:09                 0 newfile.txt
# 2021-03-17  오전 11:01                 0 test.txt
# 2021-03-17  오전 10:56                16 test123.txt
# 2021-02-02  오후 04:09                 4 Untitled-1.sql
#                4개 파일                  20 바이트
#                5개 디렉터리  168,967,876,608 바이트 남음
               
               

# 실행한 시스템 명령어의 결괏값 돌려받기 - os.popen
# os.popen은 시스템 명령어를 실행한 결괏값을 읽기 모드 형태의 파일 객체로 돌려준다.
# >>> f = os.popen("dir")
# >>> print(f.read())
#  D 드라이브의 볼륨: Data
#  볼륨 일련 번호: 4C8C-9E68

#  D:\코딩 디렉터리

# 2021-03-17  오전 10:41    <DIR>          .
# 2021-03-17  오전 10:41    <DIR>          ..
# 2021-03-10  오전 08:06    <DIR>          .vscode
# 2021-03-17  오전 09:35    <DIR>          code
# 2021-03-17  오전 09:43    <DIR>          Mymod
# 2021-03-11  오전 10:09                 0 newfile.txt
# 2021-03-17  오전 11:01                 0 test.txt
# 2021-03-17  오전 10:56                16 test123.txt
# 2021-02-02  오후 04:09                 4 Untitled-1.sql
#                4개 파일                  20 바이트
#                5개 디렉터리  168,967,876,608 바이트 남음

# 기타 유용한 os 관련 함수
# 함수	설명
# os.mkdir(디렉터리)	디렉터리를 생성한다.
# os.rmdir(디렉터리)	디렉터리를 삭제한다.단, 디렉터리가 비어있어야 삭제가 가능하다.
# os.unlink(파일)	파일을 지운다.
# os.rename(src, dst)	src라는 이름의 파일을 dst라는 이름으로 바꾼다.

# shutil

# shutil은 파일을 복사해 주는 파이썬 모듈이다.
# 다음 예시는 src라는 이름의 파일을 dst로 복사한다. 만약 dst가 디렉터리 이름이라면 src라는 파일 이름으로 dst 디렉터리에 복사하고
# 동일한 파일 이름이 있을 경우에는 덮어쓴다.

# import shutil
# shutil.copy("D:/코딩/code/test11.txt", "D:/코딩/mymod")
# shutil.copy("D:/코딩/code/test11.txt","D:/코딩/code/test22.txt")
# # 정리 해보면 copy 함수 ("복사하려는 대상파일", 경로 또는 복사 되는 파일이름)

# glob

# 가끔 파일을 읽고 쓴느 기능이 있는 프로그램을 만들다 보면 특정 디렉터리에 있는 파일 이름 모두를 알아야 할 때가 있다.
# 이럴때 사용하는 모듈이 glob
# 디렉터리에 있는 파일들을 리스트로 만들기 -glob(pathname)
# glob 모듈은 디렉터리안의 파일들을 읽어서 돌려준다. *, ? 등 메타 문자를 써서 원하는 파일만 읽어 들일 수도 있다.
# 다음은 D:/코딩/code 디렉터리에 있는 파일 중 이름이 mark로 시작하는 파일을 모두 찾아서 읽어들이는 예이다
# import glob
# print(glob.glob("D:/코딩/code/*.py")) # 특정 확장자를 가진 파일만 보고싶을 때
# print(glob.glob("D:/코딩/code/*")) # 모든 항목을 다보고싶을 때는 *를 써서 읽어 들일 수 있다

# tempfile

# # 파일을 임시로 만들어서 사용할 때 유용한 모듈이 바로 tempfile이다. tempfile.mkstemp()는 중복되지 않는 임시파일의 이름을 무작위로 만들어서 돌려준다.
# import tempfile
# f = tempfile.mkstemp()
# print(f, type(f)) # (3, 'C:\\Users\\lee022\\AppData\\Local\\Temp\\tmpnjxui5bq') 3은 뭘까 ?

# tempfile.TemporaryFile()은 임시 저장 공간으로 사용할 파일 객체를 돌려준다. 이 파일은 기본적으로 바이너리 쓰기 모드(wb)를 갖는다. f.close()가 호출되면 이 파일 객체는 자동으로 사라진다.

# >>> import tempfile
# >>> f = tempfile.TemporaryFile()
# >>> f.close()
# tempfile 내용이 100% 이해 되지 않음...

# time

# 시간과 관련된 time 모듈에는 함수가 굉장히 많다.

# time.time
# time.tiem()은 UTC(Universal Time Coordinated 세계 표준시)를 사용하여 현재 시간을 실수 형태로 돌려준다.
# 1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간을 초단위로 돌려준다.
# import time
# print(time.time()) # 1615954707.6699643

# time.localtime
# time.localtime은 time.time()이 돌려준 실수 값을 사용해서 연도, 월, 일, 시, 분, 초의 형태로 바꿔주는 함수.
# print(time.localtime(time.time()))
# time.struct_time(tm_year=2021, tm_mon=3, tm_mday=17, tm_hour=13, tm_min=19, tm_sec=38, tm_wday=2, tm_yday=76, tm_isdst=0)

# 연도 / 월 / 일 / 시 / 분 / 초 / wday [0,6] 요일 / yday [365] 일수 / 
# isdst [1,0,-1] 현재의 Time Zone 이 DaylightSaving 을 이용하는 경우인지를 지정하는 값입니다. 0 이면 사용안함. 1 이상이면 사용, -1 이면 시스템 설정에 의해 작동됩니다.

# time.asctime
# time.localtime에 의해서 반환된 튜플 형태의 값을 인수로 받아서 날짜와 시간을 알아보기 쉬운 형태로 돌려주는 함수
# print(time.asctime(time.localtime(time.time()))) # Wed Mar 17 13:24:55 2021

# time.ctime
# time.asctime(time.localtime(time.time()))은 time.ctime()으로 간단하게 표기 될 수 있다. asctime과 다른점은 항상 현재시간만을 돌려준다.
# print(time.ctime())

# time.strftime
# time.strftime('출력할 형식 포맷 코드', time.localtime(time.time()))
# strftime 함수는 시간에 관계된 것을 세밀하게 표현하는 여러 가지 포맷 코드를 제공
# 포맷코드	설명	예
# %a	요일 줄임말	Mon
# %A	요일	Monday
# %b	달 줄임말	Jan
# %B	달	January
# %c	날짜와 시간을 출력함	06/01/01 17:22:21
# %d	날(day)	[01,31]
# %H	시간(hour)-24시간 출력 형태	[00,23]
# %I	시간(hour)-12시간 출력 형태	[01,12]
# %j	1년 중 누적 날짜	[001,366]
# %m	달	[01,12]
# %M	분	[01,59]
# %p	AM or PM	AM
# %S	초	[00,59]
# %U	1년 중 누적 주-일요일을 시작으로	[00,53]
# %w	숫자로 된 요일	[0(일요일),6]
# %W	1년 중 누적 주-월요일을 시작으로	[00,53]
# %x	현재 설정된 로케일에 기반한 날짜 출력	06/01/01
# %X	현재 설정된 로케일에 기반한 시간 출력	17:22:21
# %Y	년도 출력	2001
# %Z	시간대 출력	대한민국 표준시
# #%%	문자	%
# %y	세기부분을 제외한 년도 출력	01

# print(time.strftime('%x'" "'%X', time.localtime(time.time()))) # 한 번에 여려개를 사용 할 수 있다.
# 03/17/21 13:49:36

# time.sleep
# time.sleep(float) 함수는 주로 루프 안에서 많이 사용한다. 이 함수를 사용하면 일정 시간 간격을 두고 루프를 실행 할 수 있다.
# for i in range(3):
#     print(i)
#     time.sleep(0.1) # 실수는 소수점 거의 무한대로 입력 가능. 특정 error 발생하지 않음
    
# calendar

# calendar는 파이썬에서 달력을 볼 수 있게 해주는 모듈이다.
# calendar.calendar(연도) 사용 하면 그 해의 전체 달력을 볼수 있다.
# import calendar
# print(calendar.calendar(2021))
# print(calendar.prcal(2021)) 도 같은 결과를 얻는다.
#                                   2021

#       January                   February                   March
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#              1  2  3       1  2  3  4  5  6  7       1  2  3  4  5  6  7
#  4  5  6  7  8  9 10       8  9 10 11 12 13 14       8  9 10 11 12 13 14
# 11 12 13 14 15 16 17      15 16 17 18 19 20 21      15 16 17 18 19 20 21
# 18 19 20 21 22 23 24      22 23 24 25 26 27 28      22 23 24 25 26 27 28
# 25 26 27 28 29 30 31                                29 30 31

#        April                      May                       June
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#           1  2  3  4                      1  2          1  2  3  4  5  6
#  5  6  7  8  9 10 11       3  4  5  6  7  8  9       7  8  9 10 11 12 13
# 12 13 14 15 16 17 18      10 11 12 13 14 15 16      14 15 16 17 18 19 20
# 19 20 21 22 23 24 25      17 18 19 20 21 22 23      21 22 23 24 25 26 27
# 26 27 28 29 30            24 25 26 27 28 29 30      28 29 30
#                           31

#         July                     August                  September
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#           1  2  3  4                         1             1  2  3  4  5
#  5  6  7  8  9 10 11       2  3  4  5  6  7  8       6  7  8  9 10 11 12
# 12 13 14 15 16 17 18       9 10 11 12 13 14 15      13 14 15 16 17 18 19
# 19 20 21 22 23 24 25      16 17 18 19 20 21 22      20 21 22 23 24 25 26
# 26 27 28 29 30 31         23 24 25 26 27 28 29      27 28 29 30
#                           30 31

#       October                   November                  December
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#              1  2  3       1  2  3  4  5  6  7             1  2  3  4  5
#  4  5  6  7  8  9 10       8  9 10 11 12 13 14       6  7  8  9 10 11 12
# 11 12 13 14 15 16 17      15 16 17 18 19 20 21      13 14 15 16 17 18 19
# 18 19 20 21 22 23 24      22 23 24 25 26 27 28      20 21 22 23 24 25 26
# 25 26 27 28 29 30 31      29 30                     27 28 29 30 31

# print(calendar.prmonth(2021,1))
#     January 2021
# Mo Tu We Th Fr Sa Su
#              1  2  3
#  4  5  6  7  8  9 10
# 11 12 13 14 15 16 17
# 18 19 20 21 22 23 24
# 25 26 27 28 29 30 31

# print(calendar.weekday(2021,1,30)) # 5 토요일

# print(calendar.monthrange(2015, 12)) # 그 달의 1일이 무슨 요일인지, 그 달의 마지막 날이 몇 일인지 튜플로 돌려준다. 
# (1, 31) 2015년 12월의 1일은 화요일이며, 마지막 날은 31일 까지 있다.

# random

# random은 난수 (규칙이 없는 임의의 수)를 발생시키는 모듈이다. random과 randit에 대해 알아보자
# 다음은 0.0에서 1.0 사이의 실수 중 난수 값을 돌려주는 예를 보여준다.

# import random
# print(random.random())

# 다음 예는 1에서 10 사이의 정수 중에서 난수값을 돌려준다. 1과 10을 포함
# print(random.randint(1,10))

# random 모듈을 사용해서 재미있는 함수를 하나 만들어 보자.

# # random_pop.py
# import random
# def random_pop(data):
#     number = random.randint(0, len(data)-1)
#     return data.pop(number)

# # if __name__ == "__main__": # __name__ == __main__은 인터프리터에서 직접 실행했을 경우에만 if문 내의 코드를 돌리라는 명령이 됩니다.#
# #     data = [1, 2, 3, 4, 5]
# #     while data: 
# #         print(random_pop(data))
# #         time.sleep(0.2)

# data = [1, 2, 3, 4, 5]
# while data: 
#     print(random_pop(data))
#     time.sleep(0.2)

# random_pop 함수는 random 모듈의 choice 함수를 사용하여 다음과 같이 좀 더 직관적으로 만들 수도 있다.
# random.choi 함수는 입력으로 받은 리스트에서 무작위로 하나를 선택하여 돌려준다.
# import random

# def random_pop(data):
#     while data:
#         number = random.choice(data)
#         data.remove(number)
#         print(number)
#         time.sleep(0.1)

# random_pop([1,2,3,4,5])

# 함수에서 return을 만나면 return 값을 출력하고 함수를 빠져 나간다.
# 따라서 while 문에서는 return이 아닌 print로 값을 받자.

# 리스트의 항목을 무작위로 섞고 싶을 때는 random.shuffle 함수를 사용하면 된다.

# import random
# data = [1, 2, 3, 4, 5]
# random.shuffle(data)
# print(data)
# [5, 1, 3, 4, 2]

# [1, 2, 3, 4, 5] 리스트가 shuffle 함수에 의해 섞여서 [5, 1, 3, 4, 2]로 변한 것을 확인할 수 있다.

# webbrowser

# webbrowser는 자신의 시스템에서 사용하는 기본 웹 브라우저를 자동으로 실행하는 모듈이다.

# import webbrowser
# webbrowser.open("http://google.com")
# webbrowser.open_new("http://google.com") # 이미 웹브라우저가 실행된 상태이더라도 새로운 창으로 해당 주소가 열린다.


# math

# math 모듈
import math
# 올림 함수 math.ceil(x)
print(math.ceil(-3.14))
print(math.ceil(3.14))
# 내림 함수 math.floor(x)
print(math.floor(-3.14))  # - 4
print(math.floor(3.14)) # 3
# 내림 함수가 하나 더있다. math.trunc(x)
print(math.trunc(-3.14)) # -3
print(math.trunc(3.14)) # 3
print(int(-3.14)) # - 3
# trunc()함수는 내림을 하더라도 0으로 향하는 반면 floor() 함수는 무조건 아래만 향해 내림한다. 
# 참고로 math.trunc()함수는 int()와 같이 결과를 반환한다.


# 스레드를 다루는 threading 모듈

# 컴퓨터에서 동작하고 있는 프로그램을 프로세스 (Process)라고 한다. 보통 1개의 프로세스는 한 가지 일만하지만,
# 스레드를 사용하면 한 프로세스 안에서 2가지 똔느 그 이상의 일을 동시에 수행할 수 있다.

# # thread_test.py
# import time

# def longtask(): # 5초의 시간이 걸리는 함수
#     for i in range (5):
#         time.sleep(1) # 1초 간격
#         print(f'working:{i+1}\n')
# print("start")

# for i in range(5): # longtask를 5회 수행한다.
#     longtask()
# print("end")

# 위 프로그램은 이 함수를 총 5번 반복해서 수행하는 프로그램이다. 총 25초의 시간 소요

# 스레드를 사용하면 5초의 시간이 걸리는 longtask() 함수를 동시에 실행 할 수 있어 시간을 줄일 수 있다.
# thread_test.py
# import time
# import threading  # 스레드를 생성하기 위해서는 threading 모듈이 필요하다.

# def long_task():
#     for i in range(5):
#         time.sleep(1)
#         print(f"\nworking:{i+1}")

# print("Start")

# threads = []
# for i in range(5):
#     t = threading.Thread(target=long_task)  # 스레드를 생성한다.
#     print(t)
#     threads.append(t) 
#     print(threads)

# # <Thread(Thread-1, initial)>
# # [<Thread(Thread-1, initial)>]
# # <Thread(Thread-2, initial)>
# # [<Thread(Thread-1, initial)>, <Thread(Thread-2, initial)>]
# # <Thread(Thread-3, initial)>
# # [<Thread(Thread-1, initial)>, <Thread(Thread-2, initial)>, <Thread(Thread-3, initial)>]
# # <Thread(Thread-4, initial)>
# # [<Thread(Thread-1, initial)>, <Thread(Thread-2, initial)>, <Thread(Thread-3, initial)>, <Thread(Thread-4, initial)>]
# # <Thread(Thread-5, initial)>
# # [<Thread(Thread-1, initial)>, <Thread(Thread-2, initial)>, <Thread(Thread-3, initial)>, <Thread(Thread-4, initial)>, <Thread(Thread-5, initial)>]

# for t in threads:
#     t.start()  # 스레드를 실행한다.

# print("End")
# 위와 같이 프로그램을 수정하고 실행해 보면 25초 걸리던 작업이 5초 정도에 수행되는 것을 확인 할 수 있다.
# threading.Thread를 사용하여 만든 스레드 객체가 동시 작업을 가능하게 해 주기 때문이다.

# 하지만 위 프로그램을 실행해 보면 "Start"와 "End"가 먼저 출력되고 그 이후에 스레드의 결과가 출력되는 것을 확인 할 수 있다.
# 우리가 기대하는 것은 "Start"가 출력되고 그 다음에 스레드의 결과가 출력된 후 마지막으로 "End"가 출력되는 것이다.
# 프로그램을 수정해보자

import time
import threading
def longtask():
    for i in range(5):
        time.sleep(0.3)
        print(f'\nworking: {i+1}')
        
print ("Start")

threads = []
for i in range(5):
    t = threading.Thread(target=longtask)
    threads.append(t)
    
for t in threads:
    t.start()
    
for t in threads:
    t.join() # join으로 스레드가 종료 될 때 까지 기다린다.

print("End")

# 스레드의 join 함수는 해당 스레드가 종료 될 때까지 기다리게 한다.

