# Section12-2
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 조회

import sqlite3

# DB 파일 조회 (없으면 새로 생성)

conn = sqlite3.connect('D:/coding/python/all/ch1/resource/database.db') # connect가 파일을 가져오는것
# 실행해서 에러 나면 안됨

# 커서 바인딩
c = conn.cursor()

# 데이터 조회 (전체)
c.execute("SELECT * FROM users") # *은 전체 선택
# 실행만 한거고 아무것도 일어나지 않음
# 실행을 하면 첫번째 데이터에 커서가 있고, 가져올수록 커서는 계속 이동
# 결국 데이터가 없으면 None 또는 예외를 표시

# 커서 위치가 변경, 1줄 단위로 이동

# # 1개 로우 선택

# print('One -> \n', c.fetchone())

# (1, 'KIM', 'dk@naver.com', '010-4564-2524', 'KIMKIM.com', '2021-04-01 16:37:53')


# 지정 로우 선택

# print('Three -> \n', c.fetchmany(size=3)) # size = 원하는 row 설정

# [
#  (2, 'park', 'park@daum.net', '010-5478-5554', 'we3.com', '2021-04-01 16:37:53'), 
#  (3, 'Lee', 'Lee@naver.com', '010-4545-5442', 'LEE.com', '2021-04-01 16:37:53'), 
#  (4, 'Cho', 'Cho@naver.com', '010-4821-8763', 'Cho.com', '2021-04-01 16:37:53')
# ]

# 그럼 이제 커서위치는 5 row에 위치하게 된다.


# 전체 로우 선택

# print('All - > \n', c.fetchall())

 #[(5, 'Yoo', 'Yoo@naver.com', '010-5432-8777', 'Yoo.com', '2021-04-01 16:37:53')]

# 커서 위치가 5row라서 fetchall() 메서드를 사용해도 마지막 줄만 호출된다.

# 전체 로우 선택 (한 번 더)

# print('All - > \n', c.fetchall())

# All - >
#  [] # 5번 row 이후에 데이터가 없기 때문에 빈 리스트만 출력 된다.



print("*"*50)

# 외부 파일을 읽어오는 것에서 커서의 위치에 대한 이해가 중요하다.




# 순회1

# rows = c.fetchall() # 모든 커서 정보가 담겨지게 된다.
# for row in rows:
#     print('retrieve1 - > ',row)

# retrieve1 - >  (1, 'KIM', 'dk@naver.com', '010-4564-2524', 'KIMKIM.com', '2021-04-01 16:37:53')
# retrieve1 - >  (2, 'park', 'park@daum.net', '010-5478-5554', 'we3.com', '2021-04-01 16:37:53')
# retrieve1 - >  (3, 'Lee', 'Lee@naver.com', '010-4545-5442', 'LEE.com', '2021-04-01 16:37:53')
# retrieve1 - >  (4, 'Cho', 'Cho@naver.com', '010-4821-8763', 'Cho.com', '2021-04-01 16:37:53')
# retrieve1 - >  (5, 'Yoo', 'Yoo@naver.com', '010-5432-8777', 'Yoo.com', '2021-04-01 16:37:53')


# 순회2
# 변수 선언 없이 c.fetchall()에서 바로 row 호출함 더 많이 사용되는 방법
# for row in c.fetchall():
#     print('retrieve2 - > ',row)
    
# retrieve2 - >  (1, 'KIM', 'dk@naver.com', '010-4564-2524', 'KIMKIM.com', '2021-04-01 16:37:53')
# retrieve2 - >  (2, 'park', 'park@daum.net', '010-5478-5554', 'we3.com', '2021-04-01 16:37:53')
# retrieve2 - >  (3, 'Lee', 'Lee@naver.com', '010-4545-5442', 'LEE.com', '2021-04-01 16:37:53')
# retrieve2 - >  (4, 'Cho', 'Cho@naver.com', '010-4821-8763', 'Cho.com', '2021-04-01 16:37:53')
# retrieve2 - >  (5, 'Yoo', 'Yoo@naver.com', '010-5432-8777', 'Yoo.com', '2021-04-01 16:37:53')


# 순회3
for row in c.execute('SELECT * FROM users ORDER BY id desc'):
    print('retrieve3 - > ',row)
# c.excute에서 바로 row로 호출하는 것, 쿼리문이 길어져 가독성이 떨어져서 비추
    
# retrieve3 - >  (5, 'Yoo', 'Yoo@naver.com', '010-5432-8777', 'Yoo.com', '2021-04-01 16:37:53')
# retrieve3 - >  (4, 'Cho', 'Cho@naver.com', '010-4821-8763', 'Cho.com', '2021-04-01 16:37:53')
# retrieve3 - >  (3, 'Lee', 'Lee@naver.com', '010-4545-5442', 'LEE.com', '2021-04-01 16:37:53')
# retrieve3 - >  (2, 'park', 'park@daum.net', '010-5478-5554', 'we3.com', '2021-04-01 16:37:53')
# retrieve3 - >  (1, 'KIM', 'dk@naver.com', '010-4564-2524', 'KIMKIM.com', '2021-04-01 16:37:53')


print("*"*50)

# WHERE 는 조건 절

# WHERE Retrieve1
param1 = (3,)
c.execute('SELECT * FROM users WHERE id=?', param1)
# id=? 인걸 param 1 튜플에 번호로 찾겟다는 것.
# 즉 id=3 인 데이터를 찾겠다는 excute문

print('param1', c.fetchone()) 
# param1 (3, 'Lee', 'Lee@naver.com', '010-4545-5442', 'LEE.com', '2021-04-01 16:37:53')
print('param1', c.fetchall()) # 데이터가 없어서 빈 리스트 호출 id=3번데이터는 1개 뿐
# param1 []


# WHERE Retrieve2
param2 = 4
c.execute('SELECT * FROM users WHERE id="%d"' % param2)
print('param2', c.fetchone()) 
print('param2', c.fetchall())

# param2 (4, 'Cho', 'Cho@naver.com', '010-4821-8763', 'Cho.com', '2021-04-01 16:37:53')
# param2 []

# WHERE Retrieve3
# 딕셔너리 id 에 ID의 value값인 5를 넣겟다는 뜻
c.execute('SELECT * FROM users WHERE id= :ID', {"ID":5}) 
print('param3', c.fetchone()) 
print('param3', c.fetchall())

# param3 (5, 'Yoo', 'Yoo@naver.com', '010-5432-8777', 'Yoo.com', '2021-04-01 16:37:53')
# param3 []


# WHERE Retrieve4

# IN 은 합집합 둘다 가져와
# 하나이상을 fetch 할때는 fetchall() 메서드 사용

param4 = (1, 4)
c.execute('SELECT * FROM users WHERE id IN (? , ?)', param4)
print('param4', c.fetchall()) 
# param4 [(1, 'KIM', 'dk@naver.com', '010-4564-2524', 'KIMKIM.com', '2021-04-01 16:37:53'),
# (4, 'Cho', 'Cho@naver.com', '010-4821-8763', 'Cho.com', '2021-04-01 16:37:53')]


# WHERE Retrieve5
c.execute('SELECT * FROM users WHERE id IN ("%d","%d")' % (3, 5))
print('param5', c.fetchall()) 
# param5 [(3, 'Lee', 'Lee@naver.com', '010-4545-5442', 'LEE.com', '2021-04-01 16:37:53'), 
#         (5, 'Yoo', 'Yoo@naver.com', '010-5432-8777', 'Yoo.com', '2021-04-01 16:37:53')]


# WHERE Retrieve6

# OR도 합집합 둘다 가져와

# 딕셔너리 id 에 ID의 value값인 5를 넣겟다는 뜻
c.execute('SELECT * \
    FROM users \
    WHERE id= :ID1 OR id= :ID2', {"ID1":5 , "ID2":2}) 
print('param6', c.fetchall())
# param6 [(2, 'park', 'park@daum.net', '010-5478-5554', 'we3.com', '2021-04-01 16:37:53'), 
#         (5, 'Yoo', 'Yoo@naver.com', '010-5432-8777', 'Yoo.com', '2021-04-01 16:37:53')]

# ID1이 5였는데도 순서대로 2가 먼저 출력된다.



# SQL 쿼리 기초문법
# https://velog.io/@josworks27/%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4-%EA%B8%B0%EC%B4%88-Query-%EB%AC%B8%EB%B2%95


# Dump 출력 Database를 Backup하는 것

with conn: # 데이터 베이스랑 연결된 # 이것도 자동으로 close
    with open("D:/coding/python/all/ch1/resource/dump.sql","w") as f :
        for line in conn.iterdump():
            f.write("%s\n" % line)
        print("Dump print Complete.")
        
    # f.close () 자동호출
# conn.close() 자동호출