# 사이냅소프트 면접문제
# 17
# 출처 : http://okjsp.net/bbs?seq=92230

# 주어진 문자열(공백 없이 쉼표로 구분되어 있음)을 가지고 아래 문제에 대한 프로그램을 작성하세요.

# 이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌

# 김씨와 이씨는 각각 몇 명 인가요?
# "이재영"이란 이름이 몇 번 반복되나요?
# 중복을 제거한 이름을 출력하세요.
# 중복을 제거한 이름을 오름차순으로 정렬하여 출력하세요.
# 면접문제

name = "이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌"
name = name.split(",")
print(name)
name1 = set(name)
print(name1)

a = name.count("이재영")
print(a)
count1 = 0
count2 = 0
for i in name:
    if i[0] == "김":
        count1 = count1 + 1
    if i[0] == "이":
        count2 = count2 + 1
print("김씨는", count1, "이씨는", count2)
name2 = list(name1)
name2.sort()
print(name2)

# 다른 문제 풀이

arr = "이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌".split(
    ",")

print('김씨:', len(list(filter(lambda x: x[0] == '김', arr))))
print('이씨:', len(list(filter(lambda x: x[0] == '이', arr))))
print('이재영:', len(list(filter(lambda x: x == '이재영', arr))))
arr1 = list(set(arr))
print('중복을 제거한 이름:', arr1)
arr1.sort()
print('중복을 제거한 이름을 오름차순으로 정렬:', arr1)
