# 0~9까지의 문자로 된 숫자를 입력 받았을 때, 이 입력 값이 0~9까지의 숫자가 각각 한 번 씩만
# 사용된 것인지 확인하는 함수를 구하시오.

# sample inputs: 0123456789 01234 01234567890 6789012345 012322456789

# sample outputs: true false false true false

# 내 풀이

a = ["0123456789", "01234", "01234567890", "6789012345", "012322456789"]


def decide(x):
    for v in x:
        bb = 0
        y1 = "".join(sorted(v, key=None, reverse=False))
        print(y1, type(y1))
        for i in range(10):
            i = str(i)
            if y1.count(i) == 1:
                pass
            else:
                bb = + 1
                break
        if bb == 1:
            print(False)
        else:
            print(True)


decide(a)

# sorted 함수 공부
myDict = {3: 1, 2: 3, 1: 4}
print(sorted(myDict))
print(sorted(myDict.items()))
print(sorted(myDict.items(), reverse=True, key=lambda x: x[1]))
print(sorted(myDict.items(), reverse=True, key=lambda x: x[0]))

print(myDict.keys())
print(myDict.items())
print(myDict.values())

print()
# best 풀이1
n = [''.join(sorted(x)) for x in a]  # 리스트 컴프리헨션
for x in n:
    print("true" if x == "0123456789" else "false", end=" ")

print()


def best(x):
    for ii in x:
        # print(sorted(ii))
        print("True" if "".join(sorted(ii)) ==
              "0123456789" else "false", end=" ")


best(a)


print()
# best 풀이2
print(list(map(lambda n: len(set(n)) == 10 and len(n) == 10,
      "0123456789 01234 01234567890 6789012345 012322456789".split())))

# map 함수 map(변환함수, iterable)
