create database test1;
use test1;

create table User (
	uid int,
    uname varchar(3),
    dept varchar(3),
    salary int
);

insert into User(uid, uname, dept, salary)
values
(1, "aaa", "회계", 20000),
(2, "bbb", "개발", 30000),
(3, "ccc", "개발", 30000),
(4, "ddd", "회계", 20000),
(5, "eee", "청소", 15000);


create table Mroom (
	mid int,
    mname varchar(3),
    capacity int
);

insert into Mroom(mid, mname, capacity)
values
(1, "c1", 4),
(2, "c2", 2),
(3, "c3", 5),
(4, "c4", 3),
(5, "c5", 4),
(6, "c6", 2),
(7, "c7", 6),
(8, "c8", 8);

create table Reserve (
	mid int,
    uid int,
    begin_time DATETIME,
    end_time DATETIME
);
drop table Reserve;
insert into Reserve(mid, uid, begin_time, end_time)
values
(2, 1, "2019-12-15 15:00", "2019-12-15 16:00"),
(3, 1, "2019-12-11 15:00", "2019-12-11 16:00"),
(6, 1, "2019-12-13 15:00", "2019-12-14 16:00"),
(1, 1, "2019-12-20 10:00", "2019-12-20 11:00"),
(2, 1, "2019-12-21 15:00", "2019-12-21 16:00"),
(5, 2, "2019-12-16 13:00", "2019-12-16 16:00"),
(3, 3, "2019-12-01 15:00", "2019-12-01 16:00"),
(2, 3, "2019-12-03 15:00", "2019-12-03 16:00"),
(2, 3, "2019-12-04 15:00", "2019-12-04 16:00"),
(8, 3, "2019-12-05 15:00", "2019-12-05 16:00"),
(8, 3, "2019-12-21 15:00", "2019-12-21 16:00");


# 1번, 12월 한달동안 사용시간이 높은 순으로 회의실의 아이디와 사용시간을 출력하라.
SELECT mid, sum(timestampdiff(HOUR, begin_time, end_time))
FROM Reserve
WHERE begin_time >= '2019-12-01' AND end_time < '2020-01-01'
GROUP BY mid
ORDER BY sum(timestampdiff(HOUR, begin_time, end_time)) desc;

# 2번, '2019-12-16 15:00' 부터 1시간 동안, 4인이 사용할 수 있는,
# 		예약 가능한 회의실의 아이디, 이름, 최대수용인원을 출력하라.
SELECT M.*
FROM Mroom M
WHERE M.capacity >= 4 
	AND NOT EXISTS (SELECT *
					FROM Reserve R
					WHERE M.mid = R.mid
					AND (R.end_time > '2019-12-16 15:00' AND R.begin_time < '2019-12-16 16:00'));
                    
                    
# 3번, 회의실을 한번이라도 예약한 기록이 있는 사용자의 급여를 100000원 인상하라.
UPDATE User U INNER JOIN Reserve R ON U.uid = R.uid
SET salary = salary + 100000;

SELECT * FROM User;

# 4번, 회의실을 5번 이상 예약한 기록이 있는 사용자에 대해서,
#	각 회의실 별 예약 횟수를 출력하되,
# 	사용자 아이디, 사용자 이름, 회의실 아이디, 최대수용인원, 예약횟수를 표시하라.
SELECT U.uid, U.uname, M.mid, M.capacity, count(*)
FROM (SELECT uid FROM Reserve GROUP BY uid HAVING count(uid) >= 5) uR,
		User U, Mroom M, Reserve R
WHERE U.uid = uR.uid AND R.uid = uR.uid AND R.mid = M.mid
GROUP BY U.uid, U.uname, M.mid, M.capacity
ORDER BY R.uid;
