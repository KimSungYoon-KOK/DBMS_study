use university;

# 단순 곱집합
select *
from student S, enrol E;

select S.sname, S.dept, E.grade
from student S, enrol E;


# where 구문으로 기본키와 외래키 연결
select *
from student S, enrol E
where S.sno = E.sno;

select S.sname, S.dept, E.grade
from student S, enrol E
where S.sno = E.sno;

# 조인 검색하는 2가지 표기법
# C413 수업을 들은 학생에 대한 이름, 학과, 학점 정보
select S.sname, S.dept, E.grade
from student S, enrol E
where S.sno = E.sno and E.cno = 'C413';

select S.sname, S.dept, E.grade
from student S join enrol E on S.sno = E.sno
where E.cno = 'C413';

# 셀프 조인
# 같은 과 학생들의 학번 쌍을 중복없이 출력하라
select s1.sno, s2.sno, s1.dept, s2.dept
from student s1, student s2
where s1.dept = s2.dept and s1.sno < s2.sno;


# 조인과 Group by 결합
# 컴퓨터과 학생들이 수강하는 각 과목별 과목번호와 학생 수를 검색하라
select E.cno, count(*) as student_count
from student S, enrol E
where S.sno = E.sno and S.dept = '컴퓨터'
group by E.cno;

# LEFT / RIGHT / FULL (OUTER) JOIN
select sname, dept, grade
from student left outer join enrol on student.sno = enrol.sno;