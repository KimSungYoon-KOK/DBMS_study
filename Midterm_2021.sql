# 2021 1학기 중간고사
# DATETIME, DATE
create database midterm;
use midterm;

create table user (
	uid int,
	status varchar(5),
	enter_date DATE
);
insert into user(uid, status, enter_date)
values
(1, "이용가능", "2021-01-02"),
(2, "이용가능", "2020-01-01"),
(3, "이용정지", "2021-01-01"),
(4, "이용정지", "2019-01-01");

insert into user(uid, status, enter_date)
values
(5, "이용가능", "2021-03-02");

drop table user_name;
create table user_name (
	uid int,
    uname varchar(5),
    main_flag int
);
insert into user_name(uid, uname, main_flag)
values
(1, "Steve", 1),
(1, "bbb", 0),
(1, "ccc", 0),
(2, "ddd", 1),
(3, "eee", 1),
(4, "fff", 1),
(4, "ggg", 0);

insert into user_name(uid, uname, main_flag)
values
(5, "eks", 1);

create table follow (
	src_uid int,
    tar_uid int,
    enter_date DATETIME
);
insert into follow(src_uid, tar_uid, enter_date)
values
(1, 2, "2021-03-02"),
(1, 3, "2021-03-02"),
(1, 4, "2021-03-02"),
(2, 1, "2021-03-02"),
(2, 4, "2021-03-02"),
(3, 1, "2021-03-02"),
(4, 1, "2021-03-02"),
(4, 2, "2021-03-02");

# 1.
SELECT u.uid, un.uname
FROM user u join user_name un on u.uid=un.uid
where un.main_flag = 1 and u.status = '이용정지';

# 2.
SELECT uid, count(*)
FROM user u join follow f on u.uid = f.tar_uid
WHERE u.enter_date >= '2021-01-01'
group by uid
ORDER by count(*) desc;

# 3. 
select un.uname
from user_name un
where un.uid in (select uid from user_name un  where uname='Steve' and un.main_flag=1);

# 4. 
SELECT u.uid, u.enter_date
FROM user u
WHERE NOT EXISTS (select * from follow f where u.uid = f.src_uid);


# 5. 대표이름 ‘Steve’ 인 사용자를 팔로우하는 사용자들의 아이디와 가입날짜를 검색하라.
SELECT u.uid, u.enter_date
FROM user u
WHERE u.uid IN (select f.src_uid from follow f
				where f.tar_uid IN (select un.uid from user_name un
									where un.main_flag = 1 and uname='Steve'));
