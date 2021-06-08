create database test;

use test;

create table R (
	A varchar(3),
    B varchar(3),
    C varchar(3)
);

insert into R(A, B, C)
values 
("a1", "b1", "c1"),
("a1", "b1", "c2"),
("a2", "b3", "c1"),
("a3", "b4", "c3");

create table S (
	C varchar(3),
    D varchar(3)
);

insert into S (C, D)
values 
("c1", "d1"),
("c2", "d2"),
("c2", "d3");

# R 조인 R (셀프 조인)
select *
from R r1, R r2
where r1.C = r2.C;

# R 세미 조인 S
SELECT *
FROM R
WHERE R.C IN (SELECT S.C
                    FROM S
                    WHERE R.C = S.C);

# R 아우터 조인 S
SELECT R.*, S.*
FROM R
LEFT OUTER JOIN S ON R.C = S.C
UNION
SELECT R.*, S.* FROM S
LEFT OUTER JOIN R ON R.C = S.C;