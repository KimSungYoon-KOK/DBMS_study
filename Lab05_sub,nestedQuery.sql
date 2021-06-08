# from 부속 질의문
select *
from (select* from student where dept='컴퓨터')cs
where syear = 4;

# where 부속 질의문
select sno
from enrol
where finalterm = (select max(finalterm) from enrol where cno='C413');

# select 부속 질의문
select sno, (select count(cno) from enrol e where s.sno=e.sno) as course_count
from student s
where syear = 4;

# IN 중첩 질의문 -> JOIN 질의 문으로 표현이 가능하다.	
select sname
from student
where sno IN(select sno from enrol where cno='C413');

# EXISTS -> Join 질의문으로 변경 가능!
select sno, sname
from student s
where EXISTS (select * from enrol e where e.sno=s.sno AND cno = 'C413');

select sname
from student s, enrol e
where s.sno = e.sno and e.cno = 'C413';

# NOT IN 중첩 질의문 -> JOIN 질의 문으로 표현 불가!
# C413을 수강하지 않은 학생 검색
select sno, sname
from student
where sno NOT IN(select sno from enrol where cno='C413');

# C413 들었지만 다른 과목도 들었으면 검색이 된다.
select s.sno, sname
from student s, enrol e
where s.sno = e.sno and e.cno <> 'C413';


# EXISTS -> Join 질의문으로 변경 가능!
select sno, sname
from student s
where EXISTS (select * from enrol e where e.sno=s.sno AND cno = 'C413');

select sno, sname
from student s
where EXISTS (select * from enrol e where cno = 'C413' and s.sno=e.sno);

select s.sno, sname
from student s, enrol e
where s.sno = e.sno and cno = 'C413';


# NOT EXISTS -> join 질의문으로 변경 불가!
select sno, sname
from student s
where NOT EXISTS (select * from enrol e where cno = 'C413' and s.sno=e.sno);

# UNION (UNION ALL 은 중복 포함)
(select sno
from student
where syear = 1)
UNION
(select sno
from enrol
where cno = 'C413');

# 교집합 (intersect 지원 안하므로 부속 질의문으로 구현)
# 1학년 이면서 C413 수업을 들은 학생
select distinct t1.sno
from (select sno from student where syear=1) t1,
(select sno from enrol where cno='C413') t2
where t1.sno = t2.sno;