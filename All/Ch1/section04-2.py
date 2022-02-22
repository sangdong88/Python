# section04-2
# 문자형 연산자, 슬라이싱

str1 = "I am a Boy"
str2 = "Niceman"
str3 = ' '
str4 = str()
str5 = str('ace')


print(len(str1),len(str2),len(str3),len(str4),len(str5)) # 10 7 1 0 3

escape_str1 = "Do you have a \"big colliection\""
print(escape_str1) # Do you have a "big colliection"

escape_str2 = "Tab \tTab\tTab"
print(escape_str2) # Tab     Tab     Tab

# Raw String
raw_s1 = r'C:\Programs\Test\Bin'
print(raw_s1) # C:\Programs\Test\Bin
raw_s2 = r'\\a\\a'
print(raw_s2) # \\a\\a

# 멀티라인
multi = ''' 문자열 멀티라인 테스트 '''
print(multi)


multi2 =  """
문자열
멀티라인
테스트
"""
print (multi2)

# 문자열 연산

str_o1 = "*"
str_o2 = 'abc'
str_o3 = "def"
str_o4 = "niceman"
print(str_o1 * 100)
print(str_o2 + str_o3)
# print(str_o1 + 3) # error
print('a' in str_o4) # a라는 문자가 str_o4에 포함되어 있냐 True or False
# True
print ('z' not in str_o4) # z라는 문자가 str_o4 에 없는지 없으면 True 있으면 False

# 문자열 형 변환

print(str(77))
print(str(10.4))
print(str(77)+'a')


# 문자열 함수
# 참고 : https:\\www.w3schools.com\python\python\python_ref_string.asp

# a = 'Niceman'
# b = 'orange'

# print(a.islower()) # 다 소문자인지 묻는것
# print(a.endswith('s'))# 끝 글자가 s로 끝나니 ?
# print(a.capitalize()) # 첫 글자만 대문자로 변경
# print(a.replace('Nice','Good'))
# print(list(reversed(b))) # ['e', 'g', 'n', 'a', 'r', 'o']


# 문자열 슬라이싱

a = 'Niceman'
b = 'orange'

print(a[0:4])
# Nice
print(a[:])
# Niceman
print(a[0:len(a)]) # 직접 세지 않아도 끝까지 표시
# Niceman
print(b[0:4:2])
# oa  
print(b[1:-2])
# ran
print(b[::-1])
# egnaro # 역순출력

