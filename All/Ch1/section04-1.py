# 데이터 타입

# 파이썬 데이터 타입 종류
# Boolean 0과 1
# Numbers
# String
# Bytes
# Lists
# Tuples
# Sets
# Dirctionaries

v_str = "Niceman"
v_bool = True  # False
v_str2 = "Goodboy"
v_float = 10.7
v_int = 7
v_=dict = {
    "name": "Kim",
    "age" : 25
}

v_tuple = 3,5,7
v_set = {7,8,9}
v_list = [3,5,7] # 다른 언어에서 배열

print(v_str, type(v_str)) # Niceman <class 'str'>
print(v_set, type(v_set)) # {8, 9, 7} <class 'set'>


# 파이썬 숫자형 및 연산자

i1 = 39
i2 = 939
bigint1 = 999999999999999999999999999999999999999999
bigint2 = 777777777777777777777777777777777777777777
f1 = 1.234
f2 = 3.784
f3 = .5
f4 = 10.

print(i1 * i2) # 36621
print(bigint1 * bigint2) # 777777777777777777777777777777777777777776222222222222222222222222222222222222222223
print(f1 ** f2) # 2.2158306445574567
print(f3 + i2)# 939.5

result = f3 + i2
print(result, type(result)) # 939.5 <class 'float'>

a = 5.
b = 4
print (type(a),type(b))
result2 = a + b
print(result2) # 9.0

# 형변환 함수
# int, float, complex(복소수)
print(int(result2)) # 9 정수형으로 변경
print(int(True)) # 1
print(int(False)) # 0
print(complex(False)) # 0j

y= 100
y *= 100
print(y) # 10000

# https://docs.python.org/3/library/math.html

print(abs(-7)) #7
n, m = 10, 20 #동시에 2개 변수 할당
n, m = divmod(100, 8)
print(n,m) # 12 4 몫과나머지

import math

print(math.ceil(5.1)) # 5.1보다 크면서 가장 작은 정수
print(math.floor(3.874)) # 3.874보다 작은수중 가장작은 정수  


