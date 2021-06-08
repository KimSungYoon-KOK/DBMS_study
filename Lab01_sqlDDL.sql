create database university;

use university;

create table student (
	sno int primary key,
    sname varchar(10) not null,
    syear int not null default 1,
    dept varchar(5),
    enter_date datetime default now(),
    update_date datetime on update now(),
    constraint year_const check(syear >= 1 and syear <= 4)
);

insert into student(sno, sname, syear, dept)
values 
(100, '나수영', 4, '컴퓨터'),
(200, '이찬수', 3, '전기'),
(300, '정기태', 1, '컴퓨터'),
(400, '송병길', 4, '컴퓨터'),
(500, '박종화', 2, '산공');


create table course (
	cno char(4) primary key,
    cname varchar(10) not null,
    credit int not null default 1,
    dept varchar(5),
    prname varchar(5),
    enter_date datetime default now(),
    update_date datetime on update now(),
    constraint credit_const check(credit >= 1 and credit <= 3)
);

insert into course(cno, cname, credit, dept, prname)
values
('C123', '프로그래밍', 3, '컴퓨터', '김성국'),
('C312', '자료구조', 3, '컴퓨터', '황수관'),
('C324', '화일구조', 3, '컴퓨터', '이규찬'),
('C413', '데이타베이스', 3, '컴퓨터', '이일로'),
('E412', '반도체', 3, '전자', '홍봉진');

create table enrol(
	sno int,
    cno char(4),
    grade char(1),
    midterm int,
    finalterm int,
    enter_date datetime default now(),
    update_date datetime on update now(),
    primary key (sno, cno),
    foreign key (sno) references student(sno) on update cascade on delete cascade,
    foreign key (cno) references course(cno) on update cascade on delete cascade,
    check (grade >= 'A' and grade <= 'F')
);

insert into enrol(sno, cno, grade, midterm, finalterm)
values
(100, 'C413', 'A', 90, 95),
(100, 'E412', 'A', 95, 95),
(200, 'C123', 'B', 85, 80),
(300, 'C312', 'A', 90, 95),
(300, 'C324', 'C', 75, 75),
(300, 'C413', 'A', 95, 90),
(400, 'C312', 'A', 90, 95),
(400, 'C324', 'A', 95, 90),
(400, 'C413', 'B', 80, 85),
(500, 'C312', 'B', 85, 80);







