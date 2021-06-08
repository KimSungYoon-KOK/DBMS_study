# INSERT
insert
into student(sno, sname, syear, dept)
values (1000, '박정식' ,1, '컴퓨터');

insert
into student(sno, sname, dept)
values (2000, '박상수', '전자');

insert
into student(sno, sname)
values(3000,'김디비');

insert
into student(sno, sname)
values (4000, '김디'),
(5000, '김다정');


# 테이블 검색하면서 저장
create table student1 (
	sno int primary key,
    sname varchar(20),
    dept varchar(5)
);

insert into student1(sno, sname, dept)
select sno, sname, dept
from student
where syear = 1;

create table student2
select sno, sname, dept
from student
where syear = 4;

select * from student2;


# UPDATE
update student
set syear = 3, dept = '컴퓨터'
where sno = 3000;

update enrol
set finalterm = finalterm + 5
where sno in (select sno from student where dept='컴퓨터');

update enrol e inner join student s on e.sno = s.sno
set e.finalterm = e.finalterm - 50
where e.cno = 'C413' and s.dept='컴퓨터';

select * from enrol where cno='C413';


# DELETE
delete from student
where syear = 1;

select * from student;

delete from enrol e
where e.cno = 'C413' and e.finalterm <= 45
and e.sno in (select sno from student where dept = '컴퓨터');

select * from enrol;

delete e
from enrol e inner join student s on e.sno = s.sno
where s.sname = '이찬수';

select * from enrol;