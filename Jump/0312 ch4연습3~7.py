# (연습문제 풀이 : https://wikidocs.net/12769#04)

# Question3  다음은 두 개의 숫자를 입력받아 더하여 돌려주는 프로그램이다.

input1 = input("첫번째 숫자를 입력 하세요 : ")
input2 = input("두번째 숫자를 입력 하세요 : ")

print(f'두 수의 합은 {input1 + input2}입니다.')
# input1 = 3 , input2 = 6 을 입력하면 36이 출력 된다.
# why ? 3과 6은 str 타입 이기 때문.
# 항상 input 함수로 입력 된 값은 str type인 것을 명심.

input3 = int(input1)
input4 = int(input2)
print(f'두 수의 합은 {input3 + input4}입니다.')
#9가 출력 되는 것을 확인.


# Question4 다음 중 출력 결과가 다른 것 한 개를 골라 보자.

print("you" "need" "python") # youneedpython
print("you"+"need"+"python") # youneedpython
print("you", "need", "python") #you need python 쉼표는 띄어쓰기
print("".join(["you", "need", "python"])) # youneedpython

# Question5 다음은 "test.txt"라는 파일에 "Life is too short" 문자열을 저장한 후 다시 그 파일을 읽어서 출력하는 프로그램이다.

f1 = open("test.txt", 'w') #이거는 기존에 같은 이름의 파일이 있으면 덮어 쓰기
f1.write("Life is too short")
f1.write("\nyou need java")
f1.close() #파일을 open 한 뒤에는 꼭 close를 시켜 줘야 다음 작업이 진행 된다.

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()
#이 프로그램은 우리가 예상한 "Life is too short"라는 문장을 출력하지 않는다. 우리가 예상한 값을 출력할 수 있도록 프로그램을 수정해 보자.

# Question6 사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해 보자. 
# #(단 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야 한다.)
f3 = open("test.txt",'a')
f3.write("\n")
f3.write(input("입력해봐"))
f3.close

#Q7 다음과 같은 내용을 지닌 파일 test.txt가 있다. 이 파일의 내용 중 "java"라는 문자열을 "python"으로 바꾸어서 저장해 보자.
#Life is too short
#you need java
#※ replace 함수를 사용해 보자.
f4= open("test.txt",'r')
body = f4.read()
f4.close()

body = body.replace("java","python") 

f4= open("test.txt",'w')
f4.write(body)
f4.close()
# 간단히 정리하면 우선 기존의 파일을 읽고, read()함수로 그값을 변수에 저장.
# 변수 값을 .replace("")로 치환, 다시 wrie 모드로 파일 열고 치환된 값 작성 후 저장.
