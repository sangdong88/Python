# Section11
# 파이썬 외부 파일 처리
# 파이썬 Excel, CSV 파일 읽기 및 쓰기

# CSV : MIME형식이 -> text/csv

# 예제1
import csv
with open('D:/coding/python/all/ch1/resource/sample1.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # 첫줄 패스 Header 스킵 생략
    #확인 
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader :
        print(c)


# 예제2
with open('D:/coding/python/all/ch1/resource/sample2.csv', 'r') as f:
    reader = csv.reader(f, delimiter = '|') # 구분자 delimiter 를 사용
    next(reader) # 첫줄 패스 Header 스킵 생략
    #확인 
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader :
        print(c)




print()

# 예제3(Dict변환)

with open('D:/coding/python/all/ch1/resource/sample1.csv', 'r') as f:
    reader = csv.DictReader(f)

    for c in reader:
        for k,v in c.items():
            print(k,v)
        print('___________')



# 예제4

w = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]]

with open('D:/coding/python/all/ch1/resource/sample3.csv','w',newline='' ) as f :
    wt = csv.writer(f)

    for v in w:
        wt.writerow(v)
# 이렇게 write 되면 한줄 씩 자동 줄 바꿈이 된다.
# 이를 방지 하기 위해서 open 함수에 , newline = '' 줄바꿈 처리를 선언 해줄 수 있다. 

# 1,2,3

# 4,5,6

# 7,8,9

# 10,11,12

# 13,14,15

# 16,17,18
# newline='' 후
# 1,2,3
# 4,5,6
# 7,8,9
# 10,11,12
# 13,14,15
# 16,17,18


# 예제5
with open('D:/coding/python/all/ch1/resource/sample4.csv','w',newline='' ) as f :
    wt = csv.writer(f)
    wt.writerows(w)
# 모든 row들을 한번에 부른다.
# 1,2,3
# 4,5,6
# 7,8,9
# 10,11,12
# 13,14,15
# 16,17,18


#################
# writerow()는 데이터 검수를 할 때 한 줄씩 불러 검수후 사용 할 수 있고,
# writerows()는 이미 검수가 끝난 데이터를 한번에 불러서 사용할 때 쓴다.



print()
# XSL, XLSX
# openpyxl, xlsxwriter, xlrd, xlwt, xlutils 등 있으나 pandas를 주로 사용(openpyxl, xlrd) 포함
# pandas 데이터 과학이나 분석의 전단계에서 열과 행의 데이터 셋 프레임 셋을 만들어서 통계를 추출하기 위한 셋을 만들어 준다.
# pandas(openpyxl, xlrd)로 사용 가능하다.


import pandas as pd

# sheetname = '시트명' 또는 숫자, 순서대로 1번 2번 3번 이런식
# header=숫자, 몇 번째 열을 header로 지정 할 것인지 설정
# skiprow=숫자 숫자행은 가져오지 않겠다.

xlsx = pd.read_excel('D:/coding/python/all/ch1/resource/sample.xlsx')

# 상위 데이터 확인
print(xlsx.head()) # 처음 5줄만 호출 # header는 자동으로 표기
#   Sap Co.      대리점 영업사원       전월       금월  TEAM  총 판매수량
# 0  KI1316  경기수원대리점  이기정  1720000  2952000     1     123
# 1  KI1451  충청홍성대리점  정미진  4080000  2706000     2     220
# 2  KI1534  경기화성대리점  경인선   600000  2214000     1     320
# 3  KI1636  강원속초대리점  이동권  3720000  2870000     3     110
# 4  KI1735  경기안양대리점  강준석  4800000  2296000     1     134

print(xlsx.tail()) # 마지막 5줄만 호출 # header는 자동으로 표기
#    Sap Co.       대리점 영업사원       전월       금월  TEAM  총 판매수량
# 15  KI2870  경기구리시대리점  박진형  6000000  3400000     2     143
# 16  KI2910   강원춘천대리점  김은향  4800000  4896000     1     176
# 17  KI3030   강원영동대리점  전수창  4560000  3128000     2      98
# 18  KI3131   경기하남대리점  김민정  2750000  7268000     3     293
# 19  KI3252   강원포천대리점  서가은  2420000  4740000     4     240

print(xlsx.shape) # 행 , 열 표시
# (20, 7) # 총 20행, 7열


# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_excel.html
# pandas 엑셀 파일 참고자료

# 엑셀 or CSV 다시 쓰기

xlsx.to_excel('D:/coding/python/all/ch1/resource/result.xlsx', index=False)
xlsx.to_csv('D:/coding/python/all/ch1/resource/result.csv', index=False)
