# Section 12-3
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 데이터 수정 및 삭제

# CRUD
# Create(생성), Retrieve(조회), Update(수정), Delete(삭제)

import sqlite3

# DB 생성 (파일)
conn = sqlite3.connect('D:/coding/python/all/ch1/resource/database.db')
# 실행 시 에러 없는지 확인

# Cursor 연결
c = conn.cursor()

# 데이터 수정1

# 데이터 수정시에는 Unique 한 중복 될 수 없는 값으로 검색한다.

# c.execute("UPDATE users SET username = ? WHERE id =?", ("niceman",2))
# # 이렇게만 수행하면 데이터가 바뀌지 않는다.
# # commit 해줘야 함
# # conn.commit()
# # 2번의 username이 niceman으로 변경 

# # 데이터 수정2
# c.execute("UPDATE users SET username = :name WHERE id =:id", {"name":"goodman", "id": 2})
# # conn.commit()
# # # 2번의 username이 niceman - >goodman으로 변경 

# # 데이터 수정3
# c.execute("UPDATE users SET username = '%s' WHERE id = '%s'" % ("happyman", 3))
# # conn.commit()
# # 3번의 username이 happyman으로 변경 

# 중간 데이터 확인1
for users in c.execute("SELECT * FROM users"):
    print(users)

#(1, 'KIM', 'dk@naver.com', '010-4564-2524', 'KIMKIM.com', '2021-04-01 16:37:53')
# (2, 'goodman', 'park@daum.net', '010-5478-5554', 'we3.com', '2021-04-01 16:37:53')
# (3, 'happyman', 'Lee@naver.com', '010-4545-5442', 'LEE.com', '2021-04-01 16:37:53')
# (4, 'Cho', 'Cho@naver.com', '010-4821-8763', 'Cho.com', '2021-04-01 16:37:53')
# (5, 'Yoo', 'Yoo@naver.com', '010-5432-8777', 'Yoo.com', '2021-04-01 16:37:53')


# Row Delete1
c.execute("DELETE FROM users WHERE id = ?", (2,))
conn.commit()
# 2번 Row 삭제

# Row Delete2
c.execute("DELETE FROM users WHERE id = :id", {"id": 5})
conn.commit()
# 5번 Row 삭제

# Row Delete3
c.execute("DELETE FROM users WHERE id = '%s'" % 4)
conn.commit()
# 4번 Row 삭제

# Row Delete3-1
c.execute("DELETE FROM users WHERE id = '%d'" % 3)
conn.commit()
# 3번 Row 삭제

# 포매팅 연산자 %s 에는 str, int, float 형 모두 올 수 있다.


# 중간 데이터 확인2
for users in c.execute("SELECT * FROM users"):
    print(users)
# (1, 'KIM', 'dk@naver.com', '010-4564-2524', 'KIMKIM.com', '2021-04-01 16:37:53')
# 1번 1줄 남음

# 테이블 전체 데이터 삭제
print("users db deleted : " , conn.execute("DELETE FROM users").rowcount, "rows")
# users db deleted :  1 rows 1줄 남은게 삭제 된 것을 확인.

# 커밋 
conn.commit()

# 접속해제
conn.close()



