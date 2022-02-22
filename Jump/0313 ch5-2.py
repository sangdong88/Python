# 모듈 
# 모듈이란 함수나 변수 또는 클래스를 모아 놓은 파일이다.
# 모듈은 다른 파이썬 프로그램에서 불러와 사용할 수 있게끔 만든 파이썬 파일이라고도 할 수 있다.
# 프로그래밍 시에 굉장히 많은 모듈을 사용한다. 
# 모듈을 어떻게 만들고 사용할 수 있는지 알아보겠다.

# # 모듈 만들기
# import sys
# sys.path.append("D:\\coding\\Mymod")
# import mod1
# print(mod1.add(3, 4))

# 함수 이름만 사용하고 싶을때는
# from 모듈이름 import 모듈함수


# from mod1 import add
# print (add(3, 4))

# mod1 모듈의 함수를 추가로 사용하고 싶다면,

# from mod1 import add, sub
# print (add(3,4),sub(5,4))

# # mod1 모듈안에 있는 함수 모두를 불러오고 싶다면 "*" 모든 것을 의미
# from mod1 import *
# print (add(3,4),sub(5,4))


# # PS D:\코딩\연습> python mod1.py
# 5
# 6

# PS D:\코딩\연습> python
# Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import mod1
# 5
# 6
# import mod1을 수행하는 순간 mod1.py가 실행이 되어 결과값을 출력한다. 
# 우리는 단지 mod1.py 파일의 add 함수와 sub 함수만 사용하려고 했는데 말이다.
# 이런 문제를 방지하려면
# mod1.py 파일에서 아래 내용 추가
# if __name__ == "__main__":
#     print (add(1, 4))
#     print (add(4, 2))
# else:
#     print ("PASS")

# __name__ 변수란 ?
# 파이썬의 __name__ 변수는 파이썬이 내부적으로 사용하는 특별한 변수 이름이다.
# 만약 d:/코딩/연습/ python mod1.py처럼 직접 mod1.py 파일을 실행 할 경우 mod1.py 의
# __name__ 변수에는 __main__ 값이 저장되어 if 문이 참이 된다. 
# __name__ == __main__ 참

# 하지만 파이썬 쉘이나 다른 인터프리터에서 mod1을 import 할 경우에는 mod1.py의 __name__ 변수에는
# mod1.py의 모듈 이름 값 mod1이 저장된다.
# __name__ == __mod1__ 거짓.

# 그러니까 if __name__ == "__main__" : 를 사용하는 이유는,
# python mod1.py 처럼 파일을 직접 실행 하였는가 ?
# 아니면 파이선 인터프리터에서 import mod1을 하였는가? 구분하기 위함이다.
# 인터프리터에서 import mod1 입력했는데, 하위 변수를 사용하고 싶은데 이미 파일이 실행되버리면 안되기 때문.

