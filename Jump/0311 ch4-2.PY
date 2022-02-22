# 4장-2 사용자 입력과 출력
# 사용자 입력
# input 함수의 사용
#a_input = input() # input은 입력 되는 모든 것을 문자열로 취급
#print(a_input)
print("*"*30) # 줄바뀜 표시

# print 자세히 알기
# 큰 따옴표("")로 둘러 싸인 문자열은 + 연산과 동일하다
print ("Life" "is" "too" "short")
print("Life"+"is"+"too"+"short")
# 문자열 띄어쓰기는 콤마로 한다
print("Life","is","too","short")
print("Life" , "is" , "too" , "short") # 13번 라인과 같은 결과 출력, 컴마 사이의 띄어쓰기는 출력에 영향 없음
print("*"*30) # 줄바뀜 표시
#한줄에 결과값 출력하기
for i78978 in range(0,19):
    print(i78978, end=' ')
print("*"*30) # 줄바뀜 표시  

# 파일 읽고 쓰기
f=open("newfile.txt",'w')
f.close() #파일 작업 후에는 항상 f.close()로 닫아 줄것.
# r 일기모드 - 파일을 읽기만 할 때 사용
# w 쓰기모드 - 파일에 내용을 쓸 때 사용
# a 추가모드 - 파일 마지막에 새로운 내용 추가

#디렉터리 지정 하고싶으면
f1=open("d:/코딩/연습/newfile1.txt",'w') # 이런식으로 경로 지정
f1.close()

# 그 다음 test11.txt 파일안에 구구단 계산 결과를 입력.
f=open("D:/코딩/연습/test11.txt",'w')
# 파일 쓰기
for i in range(2,10):
    data = "\n%d 단 \n" % i
    f.write(data)
    
    for j in range (1,10):
        data2 = f'{i} * {j} = {i*j}, '
        f.write(data2)

f.close()

# 파일 읽기 readline 한 줄 씩 읽어 드리기
f=open("D:/코딩/연습/test11.txt",'r')
while True:
    line=f.readline()# readline 함수 ()안의 숫자의 의미는 1줄 당 몇 글자 표시 할 건지를 지정. 공란이면 줄전체 표시.
    #위에 라인 한 번 실행 될때마다 1줄을 가져온다는 의미.
    if not line: break
    print(line)
f.close  
print("*"*30) # 줄바뀜 표시 
 
# 파일 읽기 readlines 모든 줄을 읽어서 각 줄을 요소로 갖는 리스트로 돌려준다.
f=open("D:/코딩/연습/test11.txt",'r')
line1=f.readlines()
print(line1) #리스트 안에 모든 요소가 포함
for line2 in line1:
    print(line2)
f.close  
print("*"*30) # 줄바뀜 표시  

# 파일 읽기 read 함수 사용하기
f=open("D:/코딩/연습/test11.txt",'r')
data123 = f.read() # 파일 내용 전체를 문자열로 돌려 준다. 파일 전체 내용.
print(data123)
f.close()
print("*"*30) # 줄바뀜 표시  

# 파일에 새로운 내용 추가하기
f=open("D:/코딩/연습/test11.txt",'a')
for ii in range (1,10):
    data22 = f'\n{ii}입니다'
    f.write(data22)
f.close()
# 추가 된 내용 확인
f=open("D:/코딩/연습/test11.txt",'r')
data555=f.read()
print(data555)
f.close()
print("*"*30) # 줄바뀜 표시 

# with 문 사용하기 파일 쓰기 읽기를 편하게 쓸수 있다. with문이 끝나면 자동으로 close 해줌
with open("D:/코딩/연습/test11.txt",'r') as f:
    print(f.read()) # 더욱 더 간단하게 코딩 가능
    
# sys모듈로 매개변수 주기/ 명령프롬프트에서 입력 받기
import sys

args = sys.argv[1:] #슬라이싱 [1:] 1부터 마지막까지 인수를 받겠다.
for i3 in args:
    print(i3)
    print(i3.upper()) # 이건 대문 자로 바꿔주는 간단 한 프로그램
    
# cmd 에서 D:/코딩/연습/3월11일.py aaa bbb ccc 라고 입력하면 [0]는 D:/코딩/연습/3월11일.py 경로니까 슬라이싱
#[1] aaa, [2] bbb, [3] ccc 가 print 된다.