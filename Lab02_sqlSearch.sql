use university;

show tables;

select *
from student;

select sno, sname
from student
where dept='컴퓨터';

select *
from student
where not (dept = '컴퓨터' or syear = 3);

select sno, sname
from student
where syear=4
order by sname desc;	# default : 오름 차순 / desc : 내림 차순 정렬

select sno, sname
from student
where sname<'정기태';		# 문자열도 대소 비교가 가능

select sno, sname
from student
where sname like '_기_';	# _ 는 한 문자 대체, %는 여러 문자 대체

select distinct syear	# distinct : 중복 제외
from student
where dept='컴퓨터';

# 한 명의 학생 학과를 null로 바꾸고, dept가 null인 학생 검색
update student
set dept = null
where sno=200;

select sno, sname
from student
where dept is null;

# <> : != (참고, null은 모든 조건에 대해 Flase)
select sno, sname
from student
where dept <> '컴퓨터';

# 집계 함수
select count(*) as enrol_count, avg(finalterm) as avgFinal, min(finalterm) as minFinal, max(finalterm) as maxFinal
from enrol
where cno = 'C413';



