# Special Sort
# 19
# 출처 : http://www.careercup.com/question?id=5201559730257920

# 구글 전화면접 문제

# n개의 정수를 가진 배열이 있다. 이 배열은 양의정수와 음의 정수를 모두 가지고 있다. 이제 당신은 이 배열을 좀 특별한 방법으로 정렬해야 한다.

# 정렬이 되고 난 후, 음의 정수는 앞쪽에 양의정수는 뒷쪽에 있어야 한다. 또한 양의정수와 음의정수의 순서에는 변함이 없어야 한다.

# 예. -1 1 3 -2 2 ans: -1 -2 1 3 2.


s = [-1, 1, 3, -2, 2]

sMns = filter(lambda x: x < 0, s)
sPls = filter(lambda x: x > 0, s)

li1 = list(sMns)+list(sPls)
al = " ".join(list(map(str, li1)))
print(al, type(al))

# Map 함수
# 파이썬의 내장 함수인 map() 는 여러개의 데이터를 한 번에 다른 형태로 변환하기 위해서 사용 됩니다. 따라서, 여러개의 데이터를 담고 있는 list나 tuple을 대상으로 주로 사용하는 함수
# 기본 문법 map(변환함수, iterable data)
# map() 함수는 두번째 인자로 넘어온 데이터가 담고 있는 모든 데이터에 변환 함수를 적용하여 다른형태의 데이터를 반환합니다.)
users = [{'mail': 'gregorythomas@gmail.com', 'name': 'Brett Holland', 'sex': 'M'},
        {'mail': 'hintoncynthia@hotmail.com', 'name': 'Madison Martinez', 'sex': 'F'},
        {'mail': 'wwagner@gmail.com', 'name': 'Michael Jenkins', 'sex': 'M'},
        {'mail': 'daniel79@gmail.com', 'name': 'Karen Rodriguez', 'sex': 'F'},
        {'mail': 'ujackson@gmail.com', 'name': 'Amber Rhodes', 'sex': 'F'}]

def conv (fnb):
    first, last = fnb["name"].split()
    return {"first":first, "last" : last}

for ii in map(conv, users):
    print (ii)

for tt in map(lambda u: "남" if u["sex"] == "M" else "여", users):
    print(tt)


# # List Comprehension
print([user["mail"] for user in users])
print([ (x, y) for x in ['쌈밥', '치킨', '피자'] for y in ['사과', '아이스크림', '커피']])
print([ x for x in range(10) if x < 5 if x % 2 == 0 ])
