# Section09
# 파일 읽기, 쓰기

# 읽기모드 r, 쓰기모드 w(기존 동일 파일은 삭제 덮어쓰기), 추가모드 a (파일 생성 또는 추가)
# 기타 : https://docs.python.org/3.9/library/functions.html#open
# 상대 경로('../', './'), 절대 경로 확인('C:\...')

# 파일 읽기
# 예제1
f  = open('D:/coding/python/all/Ch1/resource/review.txt','r')
contests = f.read()
print(contests)
# The film, projected in the form of animation,
# imparts the lesson of how wars can be eluded through reasoning and peaceful dialogues,
# which eventually paves the path for gaining a fresh perspective on an age-old problem.
# The story also happens to centre around two parallel characters, Shundi King and Hundi King,
# who are twins, but they constantly fight over unresolved issues planted in their minds
# by external forces from within their very own units.
print(dir(f))
# f의 인스턴스 메서드들을 다 보여준다.
# ['_CHUNK_SIZE', '__class__', '__del__', '__delattr__', '__dict__', '__dir__',
#  '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', 
#  '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', 
#  '__le__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', 
#  '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_checkClosed',
#  '_checkReadable', '_checkSeekable', '_checkWritable', '_finalizing', 'buffer', 'close',
#  'closed', 'detach', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 'line_buffering',
#  'mode', 'name', 'newlines', 'read', 'readable', 'readline', 'readlines', 'reconfigure',
#  'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'write_through', 'writelines']
f.close()
print()

# 예제2
with open('D:/coding/python/all/Ch1/resource/review.txt','r') as f:
    # close() 생략가능
    c = f.read()
    d = [c] # c를 리스트로 만듬 list(c)와 동일
    print(c)
    print(d) # 글자 하나당 리스트에 넣어 준다.
    print()
    print()
    

# 예제3
with open('D:/coding/python/all/Ch1/resource/review.txt','r') as f:
    for c in f:
        print(c.strip()) # 라인 단위로 출력해준다.
        # .strip()은 좌우 공백 스페이스 제거
# The film, projected in the form of animation,
# imparts the lesson of how wars can be eluded through reasoning and peaceful dialogues,
# which eventually paves the path for gaining a fresh perspective on an age-old problem.
# The story also happens to centre around two parallel characters, Shundi King and Hundi King,
# who are twins, but they constantly fight over unresolved issues planted in their minds
# by external forces from within their very own units.

# 예제4
with open('D:/coding/python/all/Ch1/resource/review.txt','r') as f:
    content = f.read()
    print(">", content) 
    content = f.read() # 더이상 read 할 것이 없어서 빈 내용만 표시된다.
    print(">", content)
# > The film, projected in the form of animation,
# imparts the lesson of how wars can be eluded through reasoning and peaceful dialogues,
# which eventually paves the path for gaining a fresh perspective on an age-old problem.
# The story also happens to centre around two parallel characters, Shundi King and Hundi King,
# who are twins, but they constantly fight over unresolved issues planted in their minds
# by external forces from within their very own units.
# > ##내용없음

print()
# 예제5
with open('D:/coding/python/all/Ch1/resource/review.txt','r') as f:
    line = f.readline()
    # print(line) # The film, projected in the form of animation, 1줄만 호출됨
    while line: # 값이 없어질때 까지 반복
        print(line, end='####')
        line = f.readline()
# The film, projected in the form of animation,
####imparts the lesson of how wars can be eluded through reasoning and peaceful dialogues,
####which eventually paves the path for gaining a fresh perspective on an age-old problem.
####The story also happens to centre around two parallel characters, Shundi King and Hundi King,
####who are twins, but they constantly fight over unresolved issues planted in their minds
####by external forces from within their very own units.####

print()
# 예제6
with open('D:/coding/python/all/Ch1/resource/review.txt','r') as f:
    contents = f.readlines()
    print(contents)
# ['The film, projected in the form of animation,\n', 'imparts the lesson of how wars can be eluded through reasoning and peaceful dialogues,\n', 'which eventually paves the path for gaining a fresh perspective on an age-old problem.\n', 
# 'The story also happens to centre around two parallel characters, Shundi King and Hundi King,\n', 'who are twins, but they constantly fight over unresolved issues planted in their minds\n', 'by external forces from within their very own units.']
# 줄바꿈 형태를 모두 포함한 리스트 형태로 호출 된다.
    for c in contents:
        print(c, end="******")
#  The film, projected in the form of animation,
# ******imparts the lesson of how wars can be eluded through reasoning and peaceful dialogues,
# ******which eventually paves the path for gaining a fresh perspective on an age-old problem.
# ******The story also happens to centre around two parallel characters, Shundi King and Hundi King,
# ******who are twins, but they constantly fight over unresolved issues planted in their minds
# ******by external forces from within their very own units.******


print()
# 예제7
# resource파일의 score.txt에 있는 점수 평균 구하기
score = []
with open("D:/coding/python/all/Ch1/resource/score.txt",'r') as f:
    for line in f :
        score.append(int(line))
    print(score)
    
print("Average : {:6.3f}".format(sum(score)/len(score)))
print(f"Average : {sum(score)/len(score):6.3f}")
# Average : 86.667
# Average : 86.667








# 파일 쓰기


# 예제1
with open("D:/coding/python/all/ch1/resource/text1.txt", 'w') as f:
    f.write("Niceman\n")

# 예제2
with open("D:/coding/python/all/ch1/resource/text1.txt", 'a') as f:
    f.write("Niceman")

# 예제3
from random import randint

with open("D:/coding/python/all/ch1/resource/text2.txt", 'w') as f:
    for cnt in range(6) :# 0~ 5:
        f.write(str(randint(1,50))) # randit 정수 랜덤으로 생성
        f.write('\n')


# 예제4
# writelines : 리스트 - > 파일로 저장
with open("D:/coding/python/all/ch1/resource/text3.txt", 'w') as f:
    list = ["kim\n", "park\n","cho\n"]
    f.writelines(list)

# 예제5
# print 함수로 파일 저장 하기
with open("D:/coding/python/all/ch1/resource/text4.txt", 'w') as f:
    print("Test contest!", file=f)
    print("Test contest!", file=f)














