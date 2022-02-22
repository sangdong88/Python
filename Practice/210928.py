# 람다 함수
# def 함수 선언 없이 간단한 함수를 바로 선언하여 사용 가능

from functools import reduce
def f(x): return x**2


print(f(2))

print(list(map(lambda x: x**2, [1, 2, 3, 4, 5])))

print(list(filter(lambda x: x == 1 or x == 2, [1, 2, 3, 4, 5])))

print(reduce(lambda x, y: x*y, [1, 2, 3, 4, 5]))


# A씨는 두 개의 버전을 비교하는 프로그램을 작성해야 한다.

# 버전은 다음처럼 "." 으로 구분된 문자열이다.

# 버전 예) 1.0.0, 1.0.23, 1.1

# 두 개의 버전을 비교하는 프로그램을 작성하시오.

# 다음은 버전 비교의 예이다.

# 0.0.2 > 0.0.1
# 1.0.10 > 1.0.3
# 1.2.0 > 1.1.99
# 1.1 > 1.0.1
##################### My answer 

# a = input("버전1을 입력하시오 :  ")
# b = input("버전2을 입력하시오 :  ")

# aa = a.split(".")
# bb = b.split(".")

# dd = max(len(aa), len(bb))

# c = 0
# for i in range(len(aa)):
#     # print(i)
#     # print(aa[i],type(aa[i]),bb[i],type(bb[i]))
#     if int(aa[i]) > int(bb[i]):
#         print(f'{a} > {b}')
#         break
#     elif int(aa[i]) < int(bb[i]):
#         print(f'{a} < {b}')
#         break
#     elif int(aa[i]) == int(bb[i]):
#         c += 1

# if c == len(aa):
#     print(f'{a} < {b}')
# 0.0.2 > 0.0.1
# 1.0.10 > 1.0.3
# 1.2.0 > 1.1.99
# 1.1 > 1.0.1
print()
# max 함수를 쓰면 2개 중 큰 수를 사용 할 수 있다.
# 내 답변 개선.

def compare(aa, bb) :
    aa_1 = list(map(int, aa.split(".")))
    bb_1 = list(map(int, bb.split(".")))

    for i in range(min(len(aa_1), len(bb_1))):
        if aa_1[i] > bb_1[i]:
            return f'{aa} > {bb}'
        elif aa_1[i] == bb_1[i]:
            continue
        else:
            return f'{aa} < {bb}'

print(compare("0.0.2", "0.0.1"))
print(compare("1.0.10", "1.0.3"))
print(compare("1.2.0", "1.1.99"))
print(compare("1.1", "1.0.1"))
print()

# best 풀이

from itertools import zip_longest

def compare(left, right):
    left_vars = map(int, left.split('.'))
    right_vars = map(int, right.split('.'))
    for a, b in zip_longest(left_vars, right_vars, fillvalue = 0):
        if a > b:
            return '>'
        elif a < b:
            return '<'
    return '='

CASES = [['0.0.2', '0.0.1'],
         ['1.0.10', '1.0.3'],
         ['1.2.0', '1.1.99'],
         ['1.1', '1.0.1']]

if __name__ == '__main__':
    for case in CASES:
        print('{0[0]} {1} {0[1]}'.format(case, compare(*case)))

