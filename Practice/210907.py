# 피보나치 수열이란, 첫 번째 항의 값이 0이고 두 번째 항의 값이 1일 때, 이후의 항들은 이전의 두 항을 더한 값으로 이루어지는 수열을 말한다.

# 예) 0, 1, 1, 2, 3, 5, 8, 13

# 인풋을 정수 n으로 받았을때, n 이하까지의 피보나치 수열을 출력하는 프로그램을 작성하세요

# ### 나의 풀이
# n = int(input("정수를 입력하세요 :         "))
# print(n,type(n))
# l = []
# for i in range(n):
#     if i == 0 or i == 1:
#         l.append(i)
#     else :
#         ii = l[i-1] + l[i-2]
#         l.append(ii)
# print(l)

# 디지털 시계에 하루동안(00:00~23:59) 3이 표시되는 시간을 초로 환산하면 총 몇 초(second) 일까요?

# 디지털 시계는 하루동안 다음과 같이 시:분(00:00~23:59)으로 표시됩니다.

# 00:00 (60초간 표시됨)
# 00:01
# 00:02
# ...
# 23:59

# 나의 풀이
# Keypoint는 str() 변환 후 in 문자열 확인
# a = 0
# for hour in range(24):
#     for min in range(60):
#     # print(hour, end=" ")
#         if "3" in str(hour) or "3" in str(min):
#             print(hour, min , end= " ")
#             a += 1
# print()
# print(a, a*60)


# 메모리공간을 동적으로 사용하여 데이터 관리하기

# 프로그램 실행 순서

# 입력할 정수의 개수를 사용자로부터 입력 받는다.
# 입력받은 정수의 개수만큼 정수를 입력받는다.
# 입력받은 정수의 합과 평균 값을 출력한다.
# 할당된 메모리공간을 비운다.
# 요구사항

# 메모리공간은 사용자의 입력 수의 따라 변동된다.
# 사용한 공간은 마지막에 비워야 한다.
# 배열을 사용하면 안된다.


num = int(input("입력할 정수의 개수 :   "))
i = 1
sum = 0
while True:

    if i <= num:
        a = int(input("정수 :   "))
        i += 1
        sum += a
    else:
        break
avr = sum / num
print(sum, avr)
del sum, avr, a, i


num_of_n = int(input("입력할 정수 개수: "))

Sum = 0
for x in range(num_of_n):
    Sum += int(input("Enter num%d: " % (x+1)))

print("Sum: %d" % Sum)
print("Avg:  %.2f" % (Sum / num_of_n))

del num_of_n, Sum, x

num_of_n = int(input("입력할 정수 개수: "))

Sum = 0
for x in range(num_of_n):
    Sum += int(input("Enter num%d: " % (x+1)))

print(f'Sum: {Sum}')
print("Avg:  %.2f" % (Sum / num_of_n))

del num_of_n, Sum, x
