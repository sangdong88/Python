# 입력을 어떻게 받을 것인가 ? input()
# 출력은 어떻게 줄 것인가 ? print()

# step 1 입력

a = input("몇 단을 계산 할까요 ? ")
a = int(a)
print(type(a))  # 추후 곱셉 연산을 위해 str에서 int 형으로 변경 되었는지 확인

# 입력은 a 라는 변수에 int 형으로 저장 까지 완료.

result = []
result.append(a*1)
result.append(a*2)
result.append(a*3)
result.append(a*4)
result.append(a*5)
result.append(a*6)
result.append(a*7)
result.append(a*8)
result.append(a*9)
print(result)

