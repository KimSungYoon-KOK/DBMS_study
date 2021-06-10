use imdb;

# Strong Entity : 영화 기본 정보
create table movie (
	tconst varchar(20) primary key,
	titleType varchar(20),
    primaryTitle varchar(2048),
    originalTitle varchar(2048),
    isAdult boolean,
    startYear int,
    endYear int,
    runtimeMinutes int
);

# Weak Entity : 영화 장르 정보
create table genres (
	tconst varchar(20),
    genre varchar(200),
    primary key (tconst, genre),
    foreign key (tconst) references movie(tconst)
);

# Weak Entity : TV 시리즈 에피소드 정보
create table episode (
	tconst varchar(20) primary key,
    parentTconst varchar(20),
    seasonNumber int,
    episodeNumber int,
    foreign key (tconst) references movie(tconst)
);

# title_episode table을 변형해서 사용
ALTER TABLE episodet RENAME itle_episode;
ALTER TABLE episode ADD PRIMARY KEY (tconst);
ALTER TABLE episode ADD CONSTRAINT FOREIGN KEY (tconst) REFERENCES movie(tconst);

# Weak Entity : 지역별 영화 정보
create table akas (
	tconst varchar(20),
    ordering int,
    title varchar(2048),
    region varchar(30),
    language varchar(30),
    attributes varchar(200),
    isOriginalTitle boolean,
    primary key (tconst, ordering)
);

# Weak Entity : 지역별 영화 타입 정보
create table akas_types (
	tconst varchar(20),
    ordering int,
    type varchar(200),
    primary key (tconst, ordering, type),
    foreign key (tconst, ordering) references akas(tconst, ordering)
);

# Weak Entity : 지역별 영화 어트리뷰트 정보
create table akas_attributes (
	tconst varchar(20),
    ordering int,
    attribute varchar(200),
    primary key (tconst, ordering, attribute),
    foreign key (tconst) references movie(tconst),
    foreign key (tconst, ordering) references akas(tconst, ordering)
);

# Weak Entity : 감독 정보
create table directors (
	tconst varchar(20),
    director varchar(200),
    primary key (tconst, director),
    foreign key (tconst) references movie(tconst)
);

# Weak Entity : 작가 정보
create table writers (
	tconst varchar(20),
    writer varchar(200),
    primary key (tconst, writer),
    foreign key (tconst) references movie(tconst)
);

# Weak Entity : 주요 인물 정보
create table principals (
	tconst varchar(20),
	ordering int,
    nconst varchar(20),
    category varchar(200),
    job varchar(2000),
    characters varchar(2000),
    primary key (tconst, ordering, nconst),
    foreign key (tconst) references movie(tconst),
    foreign key (tconst, ordering) references akas(tconst, ordering)
);

# title_principals table을 변형해서 사용
ALTER TABLE title_principals RENAME principals;
ALTER TABLE principals ADD PRIMARY KEY (tconst, ordering, nconst);
-- foreign key (tconst, ordering) references akas(tconst, ordering);


# Strong Entity : 사람 정보
create table person (
	nconst varchar(20) primary key,
    primaryName varchar(200),
    birthYear int,
    deathYear int
);


# Weak Entity : profession 정보
create table professions (
	nconst varchar(20),
    profession varchar(300),
    primary key (nconst, profession),
    foreign key (nconst) references person(nconst)
);

# Conntect movie and person
create table knownForTitles (
	nconst varchar(20),
    tconst varchar(20),
    primary key (tconst, nconst),
    -- foreign key (tconst) references movie(tconst),
    foreign key (nconst) references person(nconst)
);

# Strong Entity : Ratings
create table ratings (
	tconst varchar(20) primary key,
    averageRating double,
    numVotes int,
    foreign key (tconst) references movie(tconst)
);

# title_ratings table을 변형해서 사용
ALTER TABLE title_ratings RENAME ratings;
ALTER TABLE ratings ADD PRIMARY KEY (tconst);



# 테이블 데이터 삭제하는 코드
SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE person;
TRUNCATE TABLE professions;
TRUNCATE TABLE knownForTitles;
SET FOREIGN_KEY_CHECKS = 1;


# Foreign key 삭제
alter table akas_attributes drop foreign key akas_attributes_ibfk_1;

# Foreign key 삭제하고 on delete cascade 추가
ALTER TABLE akas_types DROP FOREIGN KEY feed_ibfk_3;
ALTER TABLE feed ADD CONSTRAINT FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE;









