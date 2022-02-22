# 7장-3 강력한 정규 표현식의 세계로

# 이제 07-2에서 배우지 않은 몇몇 메타 문자의 의미를 살펴보고 그룹(Group)을 만드는 법,
# 전방 탐색 등 더욱 강력한 정규 표현식에 대해서 살펴보자

# 메타 문자
# 아직 살펴보지 않은 메타 문자에 대해서 모두 살펴보자
# 여기에서 다룰 메타 문자는 앞에서 살펴본 메타 문자와 성격이 조금 다르다.
# 앞에서 살펴본 +, *, [], {} 등의 메타 문자는 매치가 진행 될 때 현재 매치되고 있는 문자열의 위치가 변경된다 (소비된다)
# 하지만 이와 달리 문자열을 소비시키지 않는 메타문자도 있다.
# 이번에는 이런 문자열 소비가 없는 메타 문자에 대해 살펴보자

# # 문자열 소비 (Zerowidth Assertion)
# 이 굉장히 추상적인 개념은 예시를 들어 한번만 생각하면 굉장히 쉽게 이해가 가능하다.
# 예를 들어 아버지가방에들어간다 라는 문자열이 있다고 해보자. 내가 궁금한 정보는 가방을 찾고 방에 를 찾고 싶다.
# 이러한 문제에 대해 [가방] 이렇게 정규식을 작성하고 검색을 진행했을 때,
# 정규식 엔진이 어떤 방식으로 구동하는지를 따라가 보자.

# 아버지 부분 까지는 매치가 되지 않으므로 그냥 지나간다.
# 가방을 확인하고는 매치되었으므로 문자열을 소비해 버린다. 즉 없애 버린다와 같은 개념으로 보는 것이다.
# 소비된 문자열은 쳐다도 안보고 그 다음 문자열인 에들어간다 라는 문자열에 대해 가방 문자열을 찾는다.
# 가방을 찾는 정규표현식은 끝난다.
# 방에를 찾는 정규표현식이 시작되고, 찾지 못한 상태로 끝난다.
# 이 예시를 보다보면, 소비라는 것이 어떤 의미로 사용되었는지 이해할 수 있다. 즉, 매치가 되는 경우 해당 부분이 없어지게 된다. 정말 소비라는 단어에 걸맞는 행동이다.

# Zero-width Assertion
# 그렇다면, 너비가 없는 확인 이라는 의미의 Zero-width Assertion은 무엇일까.
# 위에서 가방이라는 단어는 2의 너비를 가진다고 볼 수 있다. 그리고 매칭이 되었을 때,
# 이 2의 너비에 해당하는 문자열이 소비된다. 이러한 관점에서 보았을 때, 0의 너비를 가진다고 함은,
# 검증을 진행하는데 있어 소비가 되는 문자열이 없다라는 의미로 와닿는다.
# 결과적으로 이러한 해석이 맞으며, Zero-width Assertion는 검색을 진행하는데 있어 위에서 알아본
# 문자열 소비가 없는 방법을 말한다. 이제 이러한 종류의 메타 문자에 대해서 알아보자.


# |
# | 메타 문자는 or 과 동일한 의미로 사용 된다 A | B 라는 정규식이 있다면 A or B 라는 의미가 된다.

import re
p = re.compile('crow|rowing')
m = p.match('rowingcrow')
m1 = p.findall('rowingcrow')
m2 = p.finditer('rowingcrow')
print(m.group()) # 이건 뭐든지 먼저 나오는 애 출력하고 끝 # rowing
print(m1) # ['rowing', 'crow'] findall로 찾으면 list로 돌려줌
# gruop(), start(), end() span() 메서드는 match나 search랑 만 사용.

# ^
# ^ 메타 문자는 문자열의 맨 처음과 일치함을 의미한다. 앞에서 살펴본 컴파일 옵션 re.MULTILINE을 사용할 경우에는
# 여러 줄의 문자열일 때 각 줄의 처음과 일치하게 된다.

print(re.search('^Life', 'Life is too short'))
#<re.Match object; span=(0, 4), match='Life'>
print(re.search('^Life', 'My Life'))
# None
# ^Life 정규식은 Life 문자열이 처음에 온 경우에는 매치하지만 처음위치가 아닌경우에는 매치 되지 않음을 알수 있다.

# $
# $ 메타문자는 ^ 메타 문자와 반대의 경우디ㅏ. 즉 $ 는 문자열의 끝과 매치함을 의미한다.
print(re.search('short$', 'Life is too short'))
# <re.Match object; span=(12, 17), match='short'>
print(re.search('short$', 'Life is too short, you need python'))
# None

# short& 정규식은 문자열이 short로 끝난 경우에는 매치되지만 그 이외의 경우에는 매치되지 않음을 알 수 있다.
# ^ 또는 & 문자를 메타 문자가 아닌 문자 그 자체로 매치하고 싶은 경우에는 \^ \&로 사용하면 된다.


# \A
# \A는 문자열의 처음과 매치 됨을 의미한다. ^ 메타 문자와 동일한 의미이지만 re.MULTILINE 옵션을 사용할 경우에는 다르게 해석된다.
# re.MULTILINE 옵션을 사용할 경우 ^ 은 각 줄의 문자열의 처음과 매치 되지만, \A는 줄과 상관없이 전체 문자열의 처음하고만 매치된다.
# 무조건 문자열의 처음

# \Z
# \A의 반대
# \Z는 문자열의 끝과 매치됨을 의미한다. re.MULTILINE옵션을 사용할 경우 & 메타 문자와는 달리 전체 문자열의 끝과 매치된다.
# 무조건 문자열의 마지막

# \b
# \b는 단어 구분자 (word boundary)이다. 보통 단어는 whitespace에 의해 구분된다.
print(re.search(r'\bclass\b', 'no class at all'))
# <re.Match object; span=(3, 8), match='class'>
# \bclass\b 정규식은 앞뒤가 whitespace로 구분된 class라는 단어와 매치됨을 의미한다.
# 따라서 no class at all의 class라는 단어와 매치됨을 확인할 수 있다.

print(re.search(r'\bclass\b', 'the declassified algorithm'))
# None # 앞 뒤 공백이 있는 class 가 아니라 매치 안됨

# \b 메타 문자를 사용할 때 주의해야 할 점이 있다.
# \b는 파이썬 리터럴 규칙에 의하면 백스페이스(BackSpace)를 의미하므로 백스페이스가 아닌
# 단어 구분자임을 알려 주기 위해 r'\bclass\b'처럼 Raw string임을 알려주는 기호 r을 반드시 붙여 주어야 한다.


# \B
# \B 메타 문자는 \b 메타 문자와 반대의 경우이다. 즉 whitespace로 구분된 단어가 아닌 경우에만 매치된다.
print(re.search(r'\Bclass\B', 'the declassified algorithm'))
# <re.Match object; span=(6, 11), match='class'> 앞뒤가 whitespace 공백이 아니기 때문에 매치
print(re.search(r'\Bclass\B', 'one subclass is'))
# None  class 뒤에 공백이 있으므로 매치 되지 않음


# 그루핑 (Grouping)

# ABC 문자열이 계속해서 반복되는지 조사하는 정규식을 작성하고 싶다고 하자. 어떻게 해야할까 ? 지금까지 공부한
# 내용으로는 위 정규식을 작성할 수 없다. 이럴 때 필요한 것이 바로 그루핑이다.

# (ABC)+ # 그룹을 만들어 주는 메타 문자는 바로 () 이다.

print(re.search('(ABC)+', 'ABCABCABC OK'))
# <re.Match object; span=(0, 9), match='ABCABCABC'>

p1 = re.compile('(ABC)+')
m1 = p1.search('ABCABCABC OK?')
print(m1) # <re.Match object; span=(0, 9), match='ABCABCABC'>
print(m1.group()) # ABCABCABC
# 매치의 객체를 지정해줘야 group()으로 출력

p2 = re.compile("\w+\s+\d+[-]\d+[-]\d+") # 여기는 raw string r을 안해줘도 됨
# raw stiring은 r은 백슬래쉬 때문에 사용한다.
pp = re.compile(r'\\wsection')
mm = pp.match('\\wsection')
print(mm)  # <re.Match object; span=(0, 9), match='\\wsection'>
pp1 = re.compile(r'\wsection')
mm1 = pp1.match('dsection')
print(mm1) # <re.Match object; span=(0, 8), match='dsection'>
pp2 = re.compile('\wsection')
mm2 = pp2.match('dsection')
print(mm2) # <re.Match object; span=(0, 8), match='dsection'>
# 같은 결과를 보임.
# 정리해보면 \ 1개면 r을 쓰던 안쓰던 메타문자 \w로 인식 되는 것.
pp3 = re.compile(r'\\wsection')
mm3 = pp3.match('\\wsection')
print(mm3) # <re.Match object; span=(0, 9), match='\\wsection'>
pp4 = re.compile('\\wsection')
mm4 = pp4.match('esection')
print(mm4) # <re.Match object; span=(0, 8), match='esection'>
# r'\\ 2개 사용시 r을 썻을 때는 \\는 문자 그대로 백슬래시 2개를 의미한다. 메타 문자 아님
# \\만 2개 사용시 \\2개가 리터럴 법칙으로 \ 개로 적용 \w 메타 문자로 인식
pp5 = re.compile(r'\\\wsection')
mm5 = pp5.match('\\psection')
print(mm5) # <re.Match object; span=(0, 9), match='\\psection'>
pp6 = re.compile('\\\wsection')
mm6 = pp6.match('\wsection')
print(mm6) # <re.Match object; span=(0, 9), match='\\wsection'>
# r'\\\ 3개 사용시 \\2개는 문자 백슬래시가 되고, \w 메타 문자가 된다.
# \\\ 만 3개 사용시 \1개는 증발 ? \\2개가 합쳐져 문자 백슬래시 1개가 됨.
m2 = p2.search("park 010-1234-5555")
print(m2.group()) # park 010-1234-5555

# r"\w+\s+\d+[-]\d+[-]\d+"은 이름 + " " + 전화번호 형태의 문자열을 찾는 정규식이다.
# 그런데 이렇게 매치된 문자열 중에서 이름만 뽑아내고 싶다면 어떻게 해야 할까 ?
# 보통 반복되는 문자열을 찾을 때 그룹을 사용하는데, 그룹을 사용하는 보다 큰 이유는 위에서 볼 수 있듯이
# 매치된 문자열 중에서 특정 부분의 문자열만 뽑아내기 위해서인 경우가 더많다.

##################################################################################################
# 즉 그룹핑은 ( )
# 반복되는 문자열을 매치하기 위해서 사용하거나,
# 매치된 문자열 중에서 특정 부분의 문자열만 뽑아내기 위해서 사용 된다. 그룹 인덱스 지정()

p2 = re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")
m2 = p2.search("park 010-1234-5555")
print(m2.group(1)) # park 만 추출

# 이름 부분인 (\w+)을 그룹으로 만들면 match 객체의  group(인덱스) 메서드를 사용하여 그루핑 된
# 부분의 문자열만 뽑아 낼 수 있다. group 메서드의 인덱스는 다음과 같은 의미를 갖는다.


# group(인덱스)	설명
# group(0)	    매치된 전체 문자열
# group(1)    	첫 번째 그룹에 해당되는 문자열
# group(2)	    두 번째 그룹에 해당되는 문자열
# group(n)	     n 번째 그룹에 해당되는 문자열

p3 = re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")
m3 = p3.match("park 010-1234-5555")
print(m3.group(2)) # 2번째 괄호인 전화 번호 부분만 출력 010-1234-5555
# 이번에는 전화번호 부분을 추가로 그룹 (\d+[-]\d+[-]\d+)로 만들었다.
# 이렇게 하면 group(2)처럼 사용하여 전화번호만 뽑아낼 수 있다.

# 만약 전화 번호 중에서도 서비스 번호만 뽑아 내고 싶다면 ? 서비스 번호 부분만 그루핑하면 된다.
p4 = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")
m4= p4.search("park 010-1234-1234")
print(m4.group(3)) # ((\d+)[-]\d+[-]\d+) 안에 (\d+)을 그루핑하여 출력한 것

# 그룹이 중첩되어 있는 경우는 바깥쪽부터 시작하여 안쪽으로 들어갈 수록 인덱스가 증가한다.


# 그루핑된 문자열 재참조하기
# 그룹의 또 하나 좋은 점은 한 번 그루핑한 문자열을 재참조 (Backreferences)할 수 있다는 점이다.
p5 = re.compile(r'(\b\w+)\s+\1') # \b는 왜쓰는건가 ?
print(p5.search('Paris in the the spring').group()) # the the
# 연속적으로 연속적으로 연속적으로 연속적으로
# 정규식 (\b\w+)\s+\1은 (그룹) + " " + 그룹과 동일한 단어와 매치됨을 의미한다.
# 이렇게 정규식을 만들게 되면 2개의 동일한 단어를 연속적으로 사용해야만 매치된다.
# 이것을 가능하게 해주는 것이 바로 재참조 메타 문자인 \1이다. \1은 정규식의 그룹 중 첫 번째 그룹을 가리킨다.
# ※ 두 번째 그룹을 참조하려면 \2를 사용하면 된다.


# 그루핑 된 문자열에 이름 붙이기

# 정규식 안에 그룹이 무척 많아진다고 가정해보자. 예를 들어 정규식 안에 그룹이 10개 이상만 되어도 매우 혼란
# 거기에 더해 정규식이 수정되면서 그룹이 추가, 삭제되면 그 그룹을 인덱스로 참조한 프로그램도 모두
# 변경해줘야 하는 위험도 갖게 된다.
# 만약 그룹을 인덱스가 아닌 이름(Named Groups)로 참조할 수 있다면 어떨까 ? 그렇다면 이런 문제에서 해방되지 않을까?

# 이러한 이유로 정규식은 그룹을 만들 때 그룹 이름을 지정할 수 있게 했다. 그 방법은 다음과 같다.

# (?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)
# 위 정규식은 앞에서 본 이름과 전화번호를 추출하는 정규식이다. 기존과 달라진 부분은 다음과 같다.
# (\w+) --> (?P<name>\w+)
# 대단히 복잡해진 것 처럼 보이지만 (\w+) 라는 그룹에 name이라는 이름을 붙인 것에 불과하다
# 여기에서 사용한 (?...) 표현식은 정규 표현식의 확장구문이다. 이 확장 구문을 사용하기 시작하면 가독성이
# 상당히 떨어지긴 하지만 반면에 강력함을 갖게 된다.
# 그룹에 이름을 지어 주려면 다음과 같은 확장 구문을 사용해야 한다.
# (?P<그룹이름>...)
# 그룹에 이름을 지정하고 참조하는 다음 예를 보자

p6 = re.compile(r'(?P<name>\w+)\s+(?P<num>(?P<service>\d+)[-]\d+[-]\d+)')
m6 = p6.search('park 010-1234-5555').group("name")
m7 = p6.search('park 010-1234-5555').group("service")
m8 = p6.search('park 010-1234-5555').group("num")
print(m6) # park가 출력
print(m7) # 010가 출력
print(m8) # 010-1234-5555 출력

# 재참조 하는 것도 가능하다
# >>> p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')
# >>> p.search('Paris in the the spring').group()
# 'the the'
# 아까 그룹의 /1 1번 그룹 재참조와 같은 느낌
# 재 참조시에는 (?P=그룹이름)이라는 확장 구문을 사용해야한다.



# 전방 탐색
# 정규식에 막 입문한 사람들이 가장 어려워 하는 것이 바로 전방 탐색(Lockhead Assertions) 확장 구문이다.
# 정규식안에 이 확장 구문을 사용하면 순식간에 암호문처럼 알아보기 어렵게 바뀌기 때문이다.
# 하지만 이 전방 탐색이 꼭 필요한 경우가 있으며 매우 유용한 경우도 많으니 꼭 알아두자

p10 = re.compile(".+:") # 도트 모든 문자 + 1개 이상 반복
m10 = p10.search("http://google.com")
print(m10.group()) # http:

p11 = re.compile("(.+):") # 도트 모든 문자 + 1개 이상 반복
m11 = p11.search("http://google.com")
print(m11.group(1)) # http

# 정규식 .+: 과 일치하는 문자열로 http:를 돌려주었다. 만약 http:라는 검색 결과에서 :을 제외하고 출력하려면
# 어떻게 해야 할까 ? 위 예는 그나마간단하지만 훨씬 복잡한 정규식이어서 그루핑은 추가로 할 수 없다는 조건까지
# 더 해진다면 어떻게 해야 할까 ?
# 이럴 때 사용하는 것이 바로 전방 탐색이다. 전방 탐색에는 긍정(Positive)과 부정(Negative)의 2종류가 있다.

# 긍정형 전방탐색 ((?=...))- ... 에 해당되는 정규식과 매치되어야 하며 조건이 통과되어도 문자열이 소비되지 않는다.
# 부정형 전방탐색 ((?!...))- ... 에 해당되는 정규식과 매치되지 않아야 하며 조건이 통과되어도 문자열이 소비되지 않는다.

# 긍정형 전방 탐색

p12 = re.compile (".+(?=:)")
m12 = p12.search ("http://google.com")
print(m12.group()) # http
# 소비 되지 않는다 = 결과로 출력되지 않는다 ?

# 자 이번에는 다른 정규식을 보자

# .*[.].*$
# 이 정규식은 파일이름 + . + 확장자를 나타내는 정규식이다. 이 정규식은 foo.bar, autoexec.bat 같은 형식의 파일과 매치
# 이 정규식에 확장자가 "bat인 파일은 제외해야 한다"는 조건을 추가해보자. 가장 먼저 생각 할 수 있는 정규식은 다음과 같다.
# .*[.][^b].*$
# 이 정규식은 확장자가 b라는 문자로 시작하면 안된다는 의미이다.
# 어딜 봐서 안된다는 의미가 있는거지 ??
# 이 정규식은 b로 시작 하는 확장자 모두를 매치한다. bar 파일도..

# .*[.]([^b]..|.[^a].|..[^t])$
# 이 정규식은 | 메타 문자를 사용하여 확장자의 첫 번째 문자가 b가 아니거나 두 번째 문자가 a가 아니거나
# 세번째 문자가 t가 아닌 경우를 의미한다. 이 정규식에 의하여 foo.bar 는 매치가 되지 않고,
# autoexec.bat은 제외 되어 만족스러운 결과를 돌려준다. 하지만 이 정규식은 sendmail.cf처럼 확장자의 문자 개수가
# 2개인 케이스를 포함하지 못하는 오동작을 하기 시작한다.

# .*[.]([^b].?.?|.[^a]?.?|..?[^t]?)$
# 확장자의 문자 개수가 2개여도 통과되는 정규식이 만들어 졌다. 하지만 정규식은 점점 더 복잡해지고 이해하기 어려워진다.
# 그런데 여기에서 bat말고 exe파일도제외하라는 조건이추가로 생긴다면 어떻게 될까 ? 이 모든 조건을 만족하는
# 정규식을 구현하려면 패턴은 더욱더 복잡해질것이다.


# 부정형 전방 탐색
# 이러한 상황의 구원투수는 바로 부정형 전방 탐색이다. 위 예는 부정형 전방탐색을 사용하면 다음과 같이 간단히 처리된다.

# .*[.](?!bat$).*$ #

print ("*"*30)
# 직접 실행 해보자

p13 = re.compile('.*[.].*$', re.MULTILINE)
m13 = p13.findall('''
eoi.bat
foo.bar
auto.es
''')
print(m13) # eoi.bat 출력
# ['eoi.bat', 'foo.bar', 'auto.es']

p14 = re.compile('(.*[.]([^b]..|.[^a].|..[^t])$)', re.M)
m14 = p14.findall('''
eoi.bat
foo.bar
auto.es
''')
print(m14) # [('foo.bar', 'bar'), ('auto.es\n', 'es\n')] ??? 문자 개수가 2개인 케이스가 있기 때문에 오동작 ?

p15 = re.compile('(.*[.]([^b].?.?|.[^a]?.?|..?[^t]?))$', re.M)
m15 = p15.findall('''
eoi.bat
foo.bar
auto.es
''')
print(m15) # [('foo.bar', 'bar'), ('auto.es', 'es')] # 앞에 파일이름은 다 어디다 팔아 먹음
# 괄호 때문에 그루핑 된 것 같음.

p16 = re.compile('.*[.][^b].*$', re.M) #[^b] 의미가 ^b로 시작하는 게아니고 not b b가아닌것과매치.
m16 = p16.findall('''
eoi.bat
foo.bar
auto.es
''')
print(m16) # ['auto.es']

# 문자 클래스([ ]) 안에는 어떤 문자나 메타 문자도 사용할수 있지만 주의해야 할 메타 문자가 1가지 있다.
# 그것은 바로 ^인데, 문자 클래스 안에 ^ 메타 문자를 사용할 경우에는 반대(not)라는 의미를 갖는다.
# 예를 들어 [^0-9]라는 정규 표현식은 숫자가 아닌 문자만 매치된다.

# 부정형 전방 탐색
# .[.](?!bat$).*$
p17 = re.compile('.*[.](?!bat$).*$', re.M)
m17 = p17.findall('''
eoi.bat
foo.bar
auto.es
''')
print(m17)  # ['foo.bar', 'auto.es'] 깔끔하게 결과 도출

# 확장자가 bat가 아닌 경우에만 통과 된다는 의미이다. bat 문자열이 있는지 조사하는 과정에서 문자열이
# 소비되지 않으므로 bat가 아니라고 판단되면 그 이후 정규식 매치가 진행 된다.

# 정리해보면 긍정형은 (?=...) 일치하는애 걸러, 빼고 출력
# 부정형은 (?!...)  괄호 안에 있는거 걸러, 빼고 출력

# exe 역시 제외하라는 조건이 추가되더라도 다음과 같이 간단히 표현할 수 있다.
# 메타 문자 | 를 사용
# .*[.](?!bat$|exe$).*$

print("*"*30) # 줄바꿈
# 문자열 바꾸기

# sub 메서드를 사용하면 정규식과 매치되는 부분을 다른 문자로 쉽게 바꿀 수 있다.
p18 = re.compile('(blue|white|red)')
print(p18.sub('colour', 'blue socks and red shoes'))
# colour socks and colour shoes 로 바뀌어서 출력

# sub 메서드의 첫 번째 매개변수는 "바꿀 문자열(replacement)"이 되고, 두 번째 매개변수는
# "대상 문자열"이 된다. 위예에서 볼 수 있듯이 blue 또는 white 또는 red 라는 문자열이
# colour라는 문자열로 바뀌는 것을 확인 할 수 있다.

# 그런데 딱 한 번 만 바꾸고 싶은 경우도 있다.
# 이렇게 바꾸기 횟수를 제어하려면 다음과 같이 세 번째 매개변수로 count값을 넘기면 된다.
print(p18.sub('coulour','blue socks and red shoes',count=1))
# coulour socks and red shoes로 처음 일치하는 blue만 colour라는 문자열로 변경 되는 것을 확인

# sub 메서드와 유사한 subn 메서드
# sub + number (변경된 문자열, 변경 횟수)
# subn 역시 sub 와 동일한 기능을 하지만 반환 결과를 튜플로 돌려준다는 차이가 있다.
# 돌려준 튜플의 첫번째 요소는 변경된 문자열이고, 두 번째 요소는 바꾸기가 발생한 횟수이다.
print(p18.subn('coulour','blue socks and red shoes'))
# ('coulour socks and coulour shoes', 2) 출력 되는 것 확인
print(p18.subn('coulour','blue socks and red shoes',count=1))
# ('coulour socks and red shoes', 1) 출력 되는 것 확인 count도 sub와 마찬가지로 적용

# sub 메서드 사용 시 참조 구문 이용하기
# sub 메서드를 사용할 때 참조 구문을 사용 할 수 있다.

p19 = re.compile(r'(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)')
print(p19.sub("\g<phone> \g<name>", "park 010-1234-5555"))
# 010-1234-5555 park 이름 전화번호를 전화번호 이름을 변경
# sub의 바꿀 문자열 부분에 \g<그룹이름>을 사용하면 정규식의 그룹이름을 참조할 수 있게 된다.
print(p19.sub("\g<2> \g<1>", "park 010-1234-5555"))
# 010-1234-5555 park 그룹이름 대신 참조 번호(그루핑 인덱스)를 사용해도 같은 결과

# sub 메서드의 매개변수로 함수 넣기
# sub 메서드의 첫 번째 매개변수로 함수를 넣을 수도 있다.
def hexrepl(match1):
    value = (int(match1.group()))
    print(value)
    return hex(value)

p20 = re.compile(r'\d+') # r'\d+ 숫자만
print(p20.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.'))
# Call 0xffd2 for printing, 0xc000 for user code.
# sub의 첫 번째 매개변수로 함수를 사용할 경우 해당 함수의 첫 번째 매개 변수에는 정규식과
# 매치된 match 객체가 입력 된다. 그리고 매치되는 문자열은 함수의 반환 값으로 바뀌게 된다.

# 매치 된 객체가 함수의 입력으로 들어가고 return된 함수 출력값이 변경된 문자열로 들어가게 된다.
# 그리고 sub이 그렇듯이 대상 문자열의 모든 매치 되는 매개변수들이 함수로 들어 가게 된다.


# Greedy vs Non-Greedy

# 정규식에서 Greedy란 어떤 의미일까 ?

s = '<html><head><title>Title</title>'
print (len(s)) # 32

print(re.match('<.*>', s).span()) #(0, 32)
print(re.match('<.*>', s).group()) # <html><head><title>Title</title>

# <.*> 정규식의 매치 결과로 <html> 문자열을 돌려주기를 기대했을 것이다.
# 하지만 * 메타 문자는 매우 탐욕스러워서 매치할 수 있는 최대한의 문자열인
# <html><head><title>Title</title> 문자열을 모두 소비해 버렸다.
# 어떻게 하면 이 탐욕스러움을 제한하고 <html> 문자열까지만 소비하도록 막을 수 있을까?

print(re.match('<.*?>', s).group())  # <html>

# Non=greedy 문자인 ? 는 *?, +?, ??, {m,n}?와 같이 사용할 수 있다.
# 가능한 가장 최소한의 반복을 수행하도록 도와주는 역할을 한다.


# 자 이제 7장의 모든 내용을 익혔으니 7-1장의 코드를 다시 작성해본다.
# 다음과 같은 문제가 주어졌다고 가정해 보자.

# 주민등록번호를 포함하고 있는 텍스트가 있다. 이 텍스트에 포함된 모든 주민등록번호의
# 뒷자리를 * 문자로 변경해 보자.
# 우선 정규식을 전혀 모르면 다음과 같은 순서로 프로그램을 작성해야 할 것이다.

# 전체 텍스트를 공백 문자로 나눈다(split).
# 나뉜 단어가 주민등록번호 형식인지 조사한다.
# 단어가 주민등록번호 형식이라면 뒷자리를 *로 변환한다.
# 나뉜 단어를 다시 조립한다.

data = """
park 800905-1049118
kim  700905-1059119
"""

result = []
for i in data.split('\n') :
    result2 = []
    for ii in i.split(' ') :
        if len(ii) == 14 and ii[0:6].isdigit() and ii[7:].isdigit() :
            ii = ii[0:6]+"-"+"*******"
        result2.append(ii)
    result.append(" ".join(result2))
print("\n".join(result))
#
# park 800905-*******
# kim  700905-*******
#

pat33 =re.compile(r"(?P<name>\d+)[-](\d+)")

print(pat33.sub('\g<name>-*******', data))


# park 800905-*******
# kim  700905-*******

