# Section12-1
# 파이썬 데이터베이스 연동(SQLite)
# Structed Query language
# 기초적인 데이터 삽입 수정 삭제 조회

# cmd 실행할때 관리자 권한으로 실행하기

import sqlite3 # 기본 설치
import datetime

# 삽입 날짜 생성
now = datetime.datetime.now()
print(now)
# 2021-04-01 15:43:38.979971 현재일자 시간 호출
nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print('nowDatetime : ' , nowDatetime) # nowDatetime :  2021-04-01 15:45:21
# sqlite3
print('sqlite3.version: ', sqlite3.version ) # sqlite3.version:  2.6.0
print('sqlite3.sqlite.version: ', sqlite3.sqlite_version ) # sqlite3.sqlite.version:  3.33.0



# DB 생성 & Auto commit  (Rollback : 삽입 이전으로 시점을 되돌리는 것)

# commit은 우리가 입력한 데이터를 메모리에 반영하는 것.

conn = sqlite3.connect('D:/coding/python/all/ch1/resource/database.db', isolation_level=None)

# Cursor 
c = conn.cursor()
print('Cursor type : ', type(c)) # Cursor type :  <class 'sqlite3.Cursor'>


# 테이블 생성 (Data Type : TEXT, NUMERIC, INTIGER, REAL, BLOB)
c.execute("CREATE TABLE IF NOT EXISTS users(id INTIGER PRIMARY KEY, username text, email text, \
    phone text, website text, regidate text)")



# 데이터 삽입 (한 번에 하나 씩 입력하는 방법)

c.execute("INSERT INTO users VALUES(1, 'KIM', 'dk@naver.com', '010-4564-2524', 'KIMKIM.com', ?)", (nowDatetime,))

c.execute("INSERT INTO users(id, username, email, phone, website, regidate) VALUES(?,?,?,?,?,?)",
(2, "park", "park@daum.net",'010-5478-5554',"we3.com", nowDatetime))

# # Many 삽입 (튜플, 리스트)
userlist = (
    (3, 'Lee', 'Lee@naver.com', "010-4545-5442", 'LEE.com', nowDatetime),
    (4, 'Cho', 'Cho@naver.com', "010-4821-8763", 'Cho.com', nowDatetime),
    (5, 'Yoo', 'Yoo@naver.com', '010-5432-8777', 'Yoo.com', nowDatetime),
)

c.executemany("INSERT INTO users(id, username, email, phone, website, regidate)\
    VALUES (?,?,?,?,?,?)", userlist)

# 앞으로는 web 에서 다운 받은 입력받은 데이터를 sqlite를 통하여, database에 저장



# 테이블 데이터 삭제
# conn.execute("DELETE FROM users") # 모든 데이터 삭제
# 테이블 삭제하면서 몇개를 지웠는지 지워진 행수 호출하는 기능
# print("users db deleted : " , conn.execute("DELETE FROM users").rowcount,"rows") 
# users db deleted :  5 rows



# 커밋 : isoation_level=None 일 경우 자동 반영(Auto Commit)
# conn.commit() 직접 커밋입력

# 롤백 # 롤백은 오토실행이 안됨
# conn.rollback()

# 접속해제
# conn.close()

# 리소스를 썻으면 항상 닫아줘야 한다.







