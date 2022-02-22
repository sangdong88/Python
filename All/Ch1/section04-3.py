# section04-3
# 파이썬 데이터 타입 (자료형)
# 리스트, 튜플
# 리스트는 배열 또는 그릇. 숫자의 모음, 또는 학생의 모음

# 리스트 (순서o, 중복o, 수정o, 삭제o)
# 선언

a = []
b= list()
c = [1,2,3,4]
d = [10, 100, 'pen', 'banana', 'orange']
e = [10, 100, ['pen', 'banana', 'orange']]

# 문자열은 한 번 지정 하면 익덱스를 가지고 내부 할당이 되어있어 변경 불가능, Immunatalbe

# 인덱싱
print(d[3])
print(d[-2]) 
print(d[0]+d[1]) # 110
print(e[2][1]) # banana
print(e[-1][-2]) # banana

# 슬라이싱
print(d[0:3]) # [10, 100, 'pen']
print(d[0:1]) # [10]
print(e[2][1:3]) # ['banana', 'orange']

# 연산
print(c+d)
print(c * 3)
print(str(c[0]) + 'hi')

# 리스트 수정, 삭제
c[0] = 77
print(c) # [77, 2, 3, 4]

c[1:2] = [100, 1000, 10000]
print(c) # [77, 100, 1000, 10000, 3, 4] 삽입이 되네

c[1] = ['a', 'b', 'c']
print(c) # [77, ['a', 'b', 'c'], 1000, 10000, 3, 4]

del c[1] # 삭제 del 은 키워드
print(c) # [77, 1000, 10000, 3, 4]
print()
print()


# 리스트 함수
y= [5,2,3,4,1]
print(y)
y.append(6)
print(y) # [5, 2, 3, 4, 1, 6]
y.sort()
print(y) # [1, 2, 3, 4, 5, 6]
y.reverse()
print(y) # [6, 5, 4, 3, 2, 1]
y.insert(2,7) # 2번 인덱스에 7을 넣을 거야
print(y) # [6, 5, 7, 4, 3, 2, 1]
y.remove(2) # 2를 찾아서 지워라 인덱스 아님
print(y) # [6, 5, 7, 4, 3, 1] 
y.pop() # pop 은 stack 마지막꺼를 꺼내고 나머지를 출력
print(y) # [6, 5, 7, 4, 3]
# pop은 LIFO Last in First out

ex = [88,77]
y.append(ex) # append 는 리스트로서 추가가 되고 마지막에
print(y) #[6, 5, 7, 4, 3, [88, 77]]
y.extend(ex) # extend는 원소로서 마지막에 추가가 됨
print(y) #[6, 5, 7, 4, 3, [88, 77], 88, 77]

# 삭제 del,remove,pop


# 튜플 (순서o, 중복o, 수정x, 삭제x)

# 중요한 자료형 삭제 수정되면 안되는 것들. 변경 되면 프로그램 흐름에 영향을 끼치는 것

a = ()
b = (1,)
c = (1,2,3,4)
# del c[2] # TypeError: 'tuple' object doesn't support item deletion
d = (10, 100, ('a','b','c'))
print(d[2][2]) # c
print(d[2:]) # (('a', 'b', 'c'),)
print(d[2][0:2]) # ('a', 'b')
print(c+d) # (1, 2, 3, 4, 10, 100, ('a', 'b', 'c'))
print()
print()


# 튜플 함수
z = (5,2,3,1,4)
print(z)
print(3 in z) # True 
print(z.index(3)) # 2 몇번째인지를 반환
print(z.count(1)) # 1 1은 1개가 있다.