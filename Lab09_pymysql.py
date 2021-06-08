import pymysql

"""
DB 응용 프로그램 API 호출 순서
1. DB connection 설정
2. Cursor 생성
3. SQL문 실행
4. SQL 검색 결과 가져오기
5. Cursor 닫기
6. DB connection 닫기
"""


conn = pymysql.connect(host='127.0.0.1', user='db2021', password='db2021', db='university', unix_socket='/tmp/mysql.sock')

# DictCursor : 애트리뷰트 이름으로 데이터 접근 가능
curs = conn.cursor(pymysql.cursors.DictCursor)      

sql = 'select * from student'
curs.execute(sql)

# 한 번에 다 가져 오기 - 비추천
# rows = curs.fetchall()
# print(rows)

# 하나씩 가져 오기 - 추천
row = curs.fetchone()
while row:
    # print(row)
    print("학번 : %d, 이름 : %s" %(row['sno'], row['sname']))
    row = curs.fetchone()


# Insert
sql = 'insert into student(sno, sname, dept) values (%s, %s, %s)'
a = (5000, '홍길동', '컴퓨터')
curs.execute(sql, a)        # sql 실행
conn.commit()               # sql 저장


# 한번에 여러개 Insert
sql = 'insert into student(sno, sname, dept) values (%s, %s, %s)'
a = (6000, '김동일', '컴퓨터')
b = (7000, '박수용', '전자')
c = (8000, '장용성', '산업공학')
st_list = [a,b,c]
curs.executemany(sql,st_list)
conn.commit()

# Delete
sno = 6000
sql = "delete from student where sno = %d" %(sno)
curs.execute(sql)
conn.commit()

# Update
sno, dept = 7000, '컴퓨터'
sql = "update student set dept = '%s' where sno = %d" %(dept, sno)
curs.execute(sql)
conn.commit()

curs.close()
conn.close()

# Multi Connection
conn1 = pymysql.connect(host='127.0.0.1', user='db2021', password='db2021', db='university', unix_socket='/tmp/mysql.sock')
curs1 = conn1.cursor(pymysql.cursors.DictCursor) 

conn2 = pymysql.connect(host='127.0.0.1', user='db2021', password='db2021', db='university', unix_socket='/tmp/mysql.sock')
curs2 = conn2.cursor(pymysql.cursors.DictCursor)

# Goal : 컴퓨터과 학생들 중에서 2과목 이상 수강한 학생들의 기말고사 점수를 7점씩 올려라
# sql1 : 컴퓨터과 학생들 중에서 2과목 이상 수강한 학생들의 학번을 검색하라
sql1 = """select s.sno
        from student s, enrol e
        where s.sno = e.sno
        and s.dept = '컴퓨터'
        group by e.sno
        having count(*) >= 2"""
curs1.execute(sql1)

# sql2 : 각 해당 학생들이 수강한 등록정보에서 기말고사 점수를 7점씩 올려라
row = curs1.fetchone()
while row:
    sql2 = """update enrol
            set final = final + 7
            where sno = %d""" %(row['sno'])
    curs2.execute(sql2)
    conn2.commit()

    row = curs1.fetchone()

curs1.close()
curs2.close()
conn1.close()
conn2.close()

