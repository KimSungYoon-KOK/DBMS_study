create database imdb;
use imdb;

# title.akas.tsv
-- titleId (string) - a tconst, an alphanumeric unique identifier of the title
-- ordering (integer) – a number to uniquely identify rows for a given titleId
-- title (string) – the localized title
-- region (string) - the region for this version of the title
-- language (string) - the language of the title
-- types (array) - Enumerated set of attributes for this alternative title. One or more of the following: "alternative", "dvd", "festival", "tv", "video", "working", "original", "imdbDisplay". New values may be added in the future without warning
-- attributes (array) - Additional terms to describe this alternative title, not enumerated
-- isOriginalTitle (boolean) – 0: not original title; 1: original title
create table title_akas (
	titleid varchar(20),
    ordering int,
    title varchar(2048),
    region varchar(30),
    language varchar(30),
    types varchar(200),
    attributes varchar(200),
    isOriginalTitle varchar(10)
);

select count(*) from title_akas;	# 26527937 rows
select * from title_akas where titleid = 'tt0000001';

# title.basics.tsv
-- tconst (string) - alphanumeric unique identifier of the title
-- titleType (string) – the type/format of the title (e.g. movie, short, tvseries, tvepisode, video, etc)
-- primaryTitle (string) – the more popular title / the title used by the filmmakers on promotional materials at the point of release
-- originalTitle (string) - original title, in the original language
-- isAdult (boolean) - 0: non-adult title; 1: adult title
-- startYear (YYYY) – represents the release year of a title. In the case of TV Series, it is the series start year
-- endYear (YYYY) – TV Series end year. ‘\N’ for all other title types
-- runtimeMinutes – primary runtime of the title, in minutes
-- genres (string array) – includes up to three genres associated with the title
create table title_basics (
	tconst varchar(20),
    titleType varchar(20),
    primaryTitle varchar(2048),
    originalTitle varchar(2048),
    isAdult varchar(10),
    startYear varchar(10),
    endYear varchar(10),
    runtimeMinutes varchar(10),
    genres varchar(2000)
);

# title.crew.tsv
-- tconst (string) - alphanumeric unique identifier of the title
-- directors (array of nconsts) - director(s) of the given title
-- writers (array of nconsts) – writer(s) of the given title
create table title_crew (
	tconst varchar(20),
    directors varchar(5000),
    writers text(20000)
);

# title.episode.tsv
-- tconst (string) - alphanumeric identifier of episode
-- parentTconst (string) - alphanumeric identifier of the parent TV Series
-- seasonNumber (integer) – season number the episode belongs to
-- episodeNumber (integer) – episode number of the tconst in the TV series
create table title_episode (
	tconst varchar(20),
    parentTconst varchar(20),
    seasonNumber varchar(20),
    episodeNumber varchar(20)
);

# title.principals.tsv
-- tconst (string) - alphanumeric unique identifier of the title
-- ordering (integer) – a number to uniquely identify rows for a given titleId
-- nconst (string) - alphanumeric unique identifier of the name/person
-- category (string) - the category of job that person was in
-- job (string) - the specific job title if applicable, else '\N'
-- characters (string) - the name of the character played if applicable, else '\N'
create table title_principals (
	tconst varchar(20),
    ordering int,
    nconst varchar(20),
    category varchar(200),
    job varchar(2000),
    characters varchar(2000)
);

# title.ratings.tsv
-- tconst (string) - alphanumeric unique identifier of the title
-- averageRating – weighted average of all the individual user ratings
-- numVotes - number of votes the title has received
create table title_ratings (
	tconst varchar(20),
    averageRating double,
    numVotes int
);

# name.basics.tsv
-- nconst (string) - alphanumeric unique identifier of the name/person
-- primaryName (string)– name by which the person is most often credited
-- birthYear – in YYYY format
-- deathYear – in YYYY format if applicable, else '\N'
-- primaryProfession (array of strings)– the top-3 professions of the person
-- knownForTitles (array of tconsts) – titles the person is known for
create table name_basics (
	nconst varchar(20),
    primaryName varchar(200),
    birthYear varchar(10),
    deathYear varchar(10),
    primaryProfession varchar(300),
    knownForTitles varchar(2048)
);
