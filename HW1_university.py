# 수강신청 프로그램
import pymysql

class application_class:

    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', user='db2021', password='db2021', db='university', unix_socket='/tmp/mysql.sock')
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
        
    def exit_fun(self):
        return False

    def insert_student(self):
        print("메뉴1: 학생 등록")
        insert = input("등록할 학생의 학번, 이름, 학과를 입력하세요: ").split(",")       # 201811162,김성윤,컴퓨터
        sql = 'insert into student(sno, sname, dept) values (%s, %s, %s)'
        self.curs.execute(sql, tuple(insert))
        self.conn.commit()
        return True   

    def delete_student(self):
        print("메뉴2: 학생 삭제")
        sno = input("삭제할 학생의 학번을 입력하세요: ")                # 6000
        sql = "delete from student where sno = %s" %(sno)
        self.curs.execute(sql)
        self.conn.commit()
        return True

    def search_student(self):
        print("메뉴3: 학생 조회")
        # 전체 학생 학번순 조회
        sql = 'select * from student order by sno'
        self.curs.execute(sql)
        row = self.curs.fetchone()
        while row:
            print("학번 : %s, 이름 : %s" %(row['sno'], row['sname']))
            row = self.curs.fetchone()

        # 특정 학번 조회
        sno = input("조회할 학생의 학번을 입력하세요(취소:N): ")     # 201811162
        if sno == "N":
            return True
        sql = "select * from student where sno = %s" %(sno)
        self.curs.execute(sql)
        row = self.curs.fetchone()
        print("학번 : %s, 이름 : %s" %(row['sno'], row['sname']))
        return True

    def insert_course(self):
        print("메뉴4: 과목 등록")
        insert = input("등록할 과목의 과목번호, 이름, 학점, 학과, 교수님 이름을 입력하세요: ").split(",")      # 3196,데이터베이스,3,컴퓨터,신효섭
        sql = "insert into course(cno, cname, credit, dept, prname) values (%s, %s, %s, %s, %s)"
        self.curs.execute(sql, tuple([insert[0], insert[1], int(insert[2]), insert[3], insert[4]]))
        self.conn.commit()
        return True

    def delete_course(self):
        print("메뉴5: 과목 삭제")
        cno = input("삭제할 과목의 과목번호를 입력하세요: ")     #E412
        sql = "delete from course where cno = '%s'" %(cno)
        self.curs.execute(sql)
        self.conn.commit()
        return True

    def search_course(self):
        print("메뉴6: 과목 조회")
        # 전체 과목 과목번호순 조회
        sql = 'select * from course order by cno'
        self.curs.execute(sql)
        row = self.curs.fetchone()
        while row:
            print("과목번호 : %s, 이름 : %s, 학점 : %s, 개설학과 : %s, 담당교수: %s" %(row['cno'], row['cname'], row['credit'], row['dept'], row['prname']))
            row = self.curs.fetchone()

        # 특정 과목번호 조회
        cno = input("조회할 과목의 과목 번호를 입력하세요(취소:N): ")     # 3196
        if cno == "N":
            return True
        sql = "select * from course where cno = '%s'" %(cno)
        self.curs.execute(sql)
        row = self.curs.fetchone()
        print("과목번호 : %s, 이름 : %s, 학점 : %s, 개설학과 : %s, 담당교수: %s" %(row['cno'], row['cname'], row['credit'], row['dept'], row['prname']))
        return True

    def insert_enrol(self):
        print("메뉴7: 수강신청")
        # 학번 및 과목번호 입력받음.
        insert = input("신청자의 학번과 신청할 과목번호를 입력하세요: ").split(",")    # 201811162,3196
        sql = "insert into enrol(sno, cno) values (%s, %s)"
        self.curs.execute(sql, tuple(insert))
        self.conn.commit()
        return True

    def delete_enrol(self):
        print("메뉴8: 수강취소")
        insert = input("학번과 수강 취소할 과목의 과목번호를 입력하세요: ").split(",")  # 201811162,3196
        sql = "delete from enrol where sno = %s and cno = %s"
        self.curs.execute(sql, tuple(insert))
        self.conn.commit()
        return True

    def search_enrol(self):
        print("메뉴9: 수강조회")
        # 전체 수강정보 조회
        sql = 'select * from enrol order by cno'
        self.curs.execute(sql)
        row = self.curs.fetchone()
        while row:
            print("학번 : %s, 과목번호 : %s, 학점 : %s, 중간 점수 : %s, 기말 점수 : %s" %(row['sno'], row['cno'], row['grade'], row['midterm'], row['finalterm']))
            row = self.curs.fetchone()

        # 학번으로 조회
        sno = input("수강 조회할 학번을 입력하세요(취소:N): ")       # 201811162
        if sno == "N":
            return True
        
        sql = "select * from enrol where sno = %s" %(sno)
        self.curs.execute(sql)
        row = self.curs.fetchone()
        while row:
            print("학번 : %s, 과목번호 : %s, 학점 : %s, 중간 점수 : %s, 기말 점수 : %s" %(row['sno'], row['cno'], row['grade'], row['midterm'], row['finalterm']))
            row = self.curs.fetchone()

        # 과목으로 조회
        cno = input("수강 조회할 과목번호을 입력하세요(취소:N): ")    # 3196
        if cno == "N":
            return True
        sql = "select * from enrol where cno = '%s'" %(cno)
        self.curs.execute(sql)
        row = self.curs.fetchone()
        while row:
            print("학번 : %s, 과목번호 : %s, 학점 : %s, 중간 점수 : %s, 기말 점수 : %s" %(row['sno'], row['cno'], row['grade'], row['midterm'], row['finalterm']))
            row = self.curs.fetchone()
        
        return True


if __name__ == "__main__":
    c = application_class()
    functions = {
            '0': c.exit_fun,
            '1': c.insert_student, '2': c.delete_student, '3': c.search_student,
            '4': c.insert_course,  '5': c.delete_course,  '6': c.search_course,
            '7': c.insert_enrol,   '8': c.delete_enrol,   '9': c.search_enrol
        }  
    flag = True
    while flag:
        print("0. 프로그램 종료\n1. 학생 등록\n2. 학생 삭제\n3. 학생 조회\n4. 과목 등록\n5. 과목 삭제\n6. 과목 조회\n7. 수강신청\n8. 수강취소\n9.수강조회")
        insert = input("사용할 메뉴를 입력하세요: ")
        flag = functions[insert]()
        
