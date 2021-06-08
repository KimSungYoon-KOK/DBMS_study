create table student10M (
	sno int primary key,
    sname varchar(10) not null,
    dept varchar(5) not null,
    year int,
    enter_date datetime default now()
);

drop procedure if exists load_student_data_10M;

delimiter #
create procedure load_student_data_10M()
begin

declare i int default 0;
declare sno int;
declare sname varchar(10);
declare dept varchar(5);
declare year int;


while i < 10000000 do
    set i = i+1;
    
    set sname = lpad(conv(floor(rand()*pow(36,10)), 10, 36), 10, 0);
    set dept = lpad(conv(floor(rand()*pow(36,5)), 10, 36), 5, 0);
    set year = FLOOR( 1 + RAND( ) *4 );
    
    insert into student10M (sno, sname, dept, year) values ( i, sname, dept, year);
  end while;

end #

delimiter ;

call load_student_data_10M();