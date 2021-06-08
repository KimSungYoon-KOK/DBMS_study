create database test1;
use test1;

create table Company(
	cid int,
    cname varchar(5),
    fyear YEAR
);

insert into Company(cid, cname, fyear)
values
(1, '스마일', '2013'),
(2, '스노잉', '2012'),
(3, '마노일', '2015'),
(4, '회사일', '2015');

create table Product(
	pid int,
    pname varchar(5),
    price int,
    category varchar(5)
);
drop table Product;
insert into Product(pid, pname, price, category)
values
(1, 'aa', 100, '전자'),
(2, 'bb', 200, '전자'),
(3, 'cc', 100, '전자'),
(4, 'dd', 150, '전자'),
(5, 'ee', 400, '기계'),
(6, 'ff', 300, '기계'),
(7, 'gg', 200, '기계'),
(8, 'hh', 100, '인형');

create table Manufacture(
	cid int,
    pid int,
    mdate DATE
);

insert into Manufacture(cid, pid, mdate)
values
(1, 1, '2018-07-08'),
(1, 1, '2019-07-08'),
(2, 1, '2018-08-08'),
(3, 1, '2019-09-08'),
(1, 2, '2019-07-08'),
(1, 3, '2019-06-08'),
(1, 4, '2019-07-08'),
(2, 5, '2017-07-08'),
(2, 6, '2016-07-08'),
(2, 7, '2015-07-08'),
(3, 8, '2014-07-08'),
(4, 8, '2014-07-08'),
(1, 7, '2014-07-08');


# 1번. 둘 이상의 회사에서 생산한 적이 있는 제품에 대하여
#	제품 아이디, 생산회사수를 출력하되 생산 회사수 내림차순으로 표시하라.
SELECT M.pid, count(M.pid)
FROM Manufacture M
GROUP BY M.pid
HAVING count(M.pid) >= 2
ORDER BY count(M.pid) desc;

# 2번. 1번을 참고하여, 둘 이상의 회사에서 생산한 적이 있는 
#	제품의 아이디, 이름, 카테고리를 출력하라.
SELECT M.pid, P.pname, P.category
FROM Manufacture M, Product P
WHERE M.pid = P.pid
GROUP BY M.pid, P.pname, P.category
HAVING count(M.pid) >= 2;

# 3번. '스마일' 회사에서 생산한 적이 있는 제품의 아이디와 이름을 출력하라.
#	단, "IN" 키워드를 사용하라. 스마일은 회사 이름임.
SELECT P.pid, P.pname
FROM Product P, Manufacture M
WHERE M.pid = P.pid
	AND M.cid IN (SELECT C.cid FROM Company C WHERE C.cname = '스마일');

# 4번. (3)번 질의문을 "EXISTS"를 사용하여 표현하라.
SELECT P.pid, P.pname
FROM Product P, Manufacture M
WHERE EXISTS (SELECT *
				FROM Company C
                WHERE M.pid = P.pid AND C.cid = M.cid AND C.cname = '스마일');
                
# 5번. (3)번 질의문을 IN, EXISTS 없이 조인으로 표현하라.
SELECT P.pid, P.pname
FROM Product P, Manufacture M, Company C
WHERE M.pid = P.pid AND C.cid = M.cid AND C.cname = '스마일';

# 6번. '전자' 카테고리에 있는 제품을 생산한 적이 있는 회사의 아이디와 이름을 출력하라.
SELECT distinct C.cid, C.cname
FROM Company C, Manufacture M
WHERE C.cid = M.cid AND M.pid IN (SELECT P.pid FROM Product P WHERE P.category = '전자');

# 7번. '전자' 카테고리에 있는 제품을 생산한 적이 없는 회사의 아이디와 이름을 출력하라.
SELECT C.cid, C.cname
FROM Company C
WHERE C.cid NOT IN (SELECT M.cid 
					FROM Manufacture M
					WHERE EXISTS (SELECT *
									FROM Product P
									WHERE P.pid = M.pid
										AND P.category = '전자'));

# 8번. '전자' 카테고리에 있는 모든 제품을 생산한 회사의 아이디와 이름을 출력하라.
# 해석 : '전자'카테고리의 모든 제품을 생산하지 않은 회사를 제거
SELECT C.cid, C.cname
FROM Company C
WHERE NOT EXISTS (SELECT P.pid
					FROM Product P
					WHERE P.category = '전자'
						AND NOT EXISTS (SELECT * 
										FROM Manufacture M
										WHERE P.pid = M.pid AND M.cid = C.cid));

SELECT c.cid, c.cname
FROM Company c JOIN (SELECT distinct cid, pid FROM Manufacture) m ON c.cid = m.cid
WHERE m.pid IN (SELECT p.pid FROM product p WHERE p.category='전자')
GROUP BY c.cid, c.cname
HAVING count(*) = (SELECT count(*) FROM product p WHERE p.category='전자');

# 9번. '스마일' 회사는 생산하고, '스노잉'회사는 생산한 적이 없는 제품의 아이디와 이름을 출력하라.
# 교집합
SELECT p1.pid, p1.pname
FROM (SELECT P.pid, P.pname
		FROM Company C, Product P, Manufacture M
		WHERE M.pid = P.pid AND M.cid = C.cid AND C.cname = '스마일') p1,
	(SELECT P.pid, P.pname
		FROM Product P
		WHERE P.pid NOT IN (SELECT M.pid
							FROM Manufacture M, Company C
							WHERE M.cid = C.cid AND C.cname = '스노잉')) p2
WHERE p1.pid = p2.pid;


# 10번. '스마일'회사에서 생산한 제품 중 같은 카테고리에서 속하는 제품들의 아이디 쌍을 출력할.
#	단, 쌍이 중복출력되지 않게 할 것
SELECT distinct P1.pid, P2.pid
FROM Product P1, Product P2, Company C, Manufacture M
WHERE P1.category = P2.category AND P1.pid < P2.pid 
	AND M.pid = P1.pid AND C.cid = M.cid AND C.cname = '스마일';

# 11번. 2019년도에 생산된 모든 제품들의 가격을 모두 10% 인상하라.
SET SQL_SAFE_UPDATES = 0;

UPDATE Product P
SET P.price = P.price * 1.1
WHERE P.pid IN (SELECT M.pid FROM Manufacture M WHERE M.mdate >= '2019-01-01' AND M.madate < '2020-01-01');

SELECT * FROM Product;

# 12번. '스마일' 회사의 모든 생산 이력을 삭제하라.
DELETE M
FROM  Manufacture M INNER JOIN Company C ON M.cid = C.cid
WHERE C.cname = '스마일';
SELECT * FROM Manufacture



