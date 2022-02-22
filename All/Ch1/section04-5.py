# Section04-5
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형
# 데이터 타입 관련 퀴즈(정답은 영상)

# 1. 아래 문자열의 길이를 구해보세요.
q1 = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"
print("1.", len(q1)) # 38

# 2. print 함수를 사용해서 아래와 같이 출력해보세요.
#    apple;orange;banana;lemon
print('\tappe;orange;banana;lemon')
#         appe;orange;banana;lemon

# 3. 화면에 * 기호 100개를 표시하세요.
print("*"*100)


# 4. 문자열 "30" 을 각각 정수형, 실수형, 복소수형, 문자형으로 변환해보세요.
a = '30'
print(int(a),type(a))
print(float(a),type(a))
print(complex(a),type(a))
print(str(a),type(a))
print()

# 5. 다음 문자열 "Niceman" 에서 "man" 문자열만 추출해보세요.
b = "Niceman"
b_idx = b.index("man")
print(b_idx) # 4 가출력
print(b[b_idx:b_idx+3]) # man
print(b[4:]) # man

# 6. 다음 문자열을 거꾸로 출력해보세요. : "Strawberry"
c = "Strawberry"
print(list(map(str,c)))
d = list(map(str,c))
d.reverse()
print("".join(d))
# yrrebwartS
# 또 다른 방법 
print(c[::-1])
# yrrebwartS

# 7. 다음 문자열에서 '-'를 제거 후 출력하세요. : "010-7777-9999"
e = "010-7777-9999"
e1 = e.split("-")
e1="".join(e1)
print(e1) 
# 01077779999
# 또 다른 방법
print(e[0:3]+e[4:8]+e[9:13])
# 01077779999

# 정규표현식
import re
print(re.sub('[^0-9]','',e)) # 빼는게 아니라 대체하는 것이고 숫자가 아닌것을 "" 로 대체한다.
# 01077779999
p11 = re.compile('[^0-9]')
m11 = p11.sub("",e)
print(m11) # 동일한 값이 나옴

# 8. 다음 문자열(URL)에서 "http://" 부분을 제거 후 출력하세요. : "http://daum.net"
import re
p= re.compile(".{4}[.].{3}")
r = p.search("http://daum.net")
print(r.group()) # daum.net

# 9. 다음 문자열을 모두 대문자, 소문자로 각각 출력해보세요. : "NiceMan"
aa = "Niceman"
aa1= aa.lower()
print(aa1) # niceman
aa2=aa.upper()
print(aa2) #NICEMAN

# 10. 다음 문자열을 슬라이싱을 이용해서 "cde"만 출력하세요. : "abcdefghijklmn"
bb = "abcdefghijklmn"
print(bb[2:5])
#cde
# 11. 다음 리스트에서 "Apple" 항목만 삭제하세요. : ["Banana", "Apple", "Orange"]
cc = ["Banana", "Apple", "Orange"]
cc.remove("Apple")
print(cc) # ['Banana', 'Orange']

# 12. 다음 튜플을 리스트로 변환하세요. : (1,2,3,4)
dd= (1,2,3,4)
print(list(dd)) # [1, 2, 3, 4]

# 13. 다음 항목을 딕셔너리(dict)으로 선언해보세요. : <성인 - 100000 , 청소년 - 70000 , 아동 - 30000>
asdf = {"성인" : 10000, "청소년" : 7000, "아동" : 3000}
print(asdf) # {'성인': 10000, '청소년': 7000, '아동': 3000}
print(list(asdf)) # ['성인', '청소년', '아동']

# 14. 13번 에서 선언한 dict 항목에 <소아 - 0> 항목을 추가해보세요.
asdf["소아"] = 0
print(asdf) # {'성인': 10000, '청소년': 7000, '아동': 3000, '소아': 0}

# 15. 13번에서 선언한 딕셔너리(dict)에서 Key 항목만 출력해보세요.
print(asdf.keys()) # dict_keys(['성인', '청소년', '아동', '소아'])

# 16. 13번에서 선언한 딕셔너리(dict)에서 value 항목만 출력해보세요.
print(asdf.values()) # dict_values([10000, 7000, 3000, 0])

# *** 결과 값만 정확하게 출력되면 됩니다. ^^* 고생하셨습니다. ***
