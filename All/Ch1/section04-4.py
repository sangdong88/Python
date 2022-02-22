# Section04-4
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형

# 딕셔너리 (Dictionary) : 순서x, 중복x. 수정o, 삭제o

# Key, Value (Json) -> MongoDB  중요
# 사용법을 확실히 알고 넘어 갈 것
# 선언
a = {'name': 'kim', 'Phone':'010-7777-7777','birth':893122}
b = {0 : 'Hello python', 1: 'Hello coding'} 
# key는 우리가 찾고자 하는 의미있는 단어로 하는 경우가 많음.
c = {'arr' : [1,2,3,4,5]}
print(type(c)) #<class 'dict'>

# 출력
print(a['name']) # kim
# print(a['name1']) # KeyError: 'name1' key없음
print(a.get('name')) # kim
print(a.get('address')) # None
# a.get method를 사용하게 되면 특정 key가 딕셔너리 안에 있는지 오류 없이 확인 할 수 있다. 추천하는 방법
print(c['arr'][1:2]) # [2]


# 딕셔너리 추가
a['address'] = 'Seoul'
print(a) # {'name': 'kim', 'Phone': '010-7777-7777', 'birth': 893122, 'address': 'Seoul'}
a['rank'] = [1,2,3,4]
a['rank2'] = (1,2,3,4)
print(a)
# {'name': 'kim', 'Phone': '010-7777-7777', 'birth': 893122, 'address': 'Seoul', 'rank': [1, 2, 3, 4], 'rank2': (1, 2, 3, 4)}

# keys, values, items 아이템은 key, value 한 쌍

print(a.keys()) # dict_keys(['name', 'Phone', 'birth', 'address', 'rank', 'rank2'])
# print(a.keys()[0]) # TypeError: 'dict_keys' object is not subscriptable
# 생긴 건 list 처럼 생겼으나 list 형이 아님
print(list(a.keys())) # ['name', 'Phone', 'birth', 'address', 'rank', 'rank2']
temp = list(a.keys())
print(temp[2]) # birth

print(a.values())
# dict_values(['kim', '010-7777-7777', 893122, 'Seoul', [1, 2, 3, 4], (1, 2, 3, 4)])

print(a.items())
# dict_items([('name', 'kim'), ('Phone', '010-7777-7777'), ('birth', 893122), ('address', 'Seoul'), ('rank', [1, 2, 3, 4]), ('rank2', (1, 2, 3, 4))])
print(list(a.items()))
# ('name', 'kim'), ('Phone', '010-7777-7777'), ('birth', 893122), ('address', 'Seoul'), ('rank', [1, 2, 3, 4]), ('rank2', (1, 2, 3, 4))]
print(2 in b) # False
print('name2' in a) # False

# 집합 [수치 계산, 과학, 연산, 머신러닝 등에 많이 쓰임]
# 집합 (sets) : 순서x, 중복x
a = set()
b = set([1,2,3,4])
c = set([1,4,5,6,6])

print(type(a)) # <class 'set'>
# set은 주로 변환해서 많이 사용
t= tuple(b)
print(t) # (1, 2, 3, 4)
l = list(b)
print(l) # [1, 2, 3, 4]

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print(s1.intersection(s2)) # {4, 5, 6} 교집합
print(s1 & s2) # {4, 5, 6}
# 합집합
print(s1 | s2) # {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s1.union(s2)) # {1, 2, 3, 4, 5, 6, 7, 8, 9}
# 차집합
print(s1 - s2)  # {1, 2, 3}
print(s1.difference(s2)) # {1, 2, 3}

# 추가 & 제거 가능
s3 = set([7,8,10,15])
s3.add(18)
s3.add(7)
print(s3)
# {7, 8, 10, 15, 18}

s3.remove(15)
print(s3) # {7, 8, 10, 15, 18}
print(type(s3)) # <class 'set'>


