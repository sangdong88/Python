def prt1():
    print("I'm NiceBoy!")


def prt2():
    print("I'm Goodboy!", print(__name__))


# 단위 실행(독립적으로 파일 실행)
# 모듈이 제대로 동작하는지 확인하기 위해서는 함수를 직접 실행해 봐야함. 단위 테스트
# 파이썬 2.x 버전
# __main__ 이라는 것은 해당 파일에서 실행 할 때만 적용. 다른 파일에서 실행 될때는 __main__ 아님
if __name__ == "__main__":
    print("This is", dir())
    prt1()
    prt2()
