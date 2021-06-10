import pymysql
import time

def insert_movie_genre():

    conn1 = pymysql.connect(host='localhost', user='db2021', password='db2021', db='imdb', unix_socket='/tmp/mysql.sock' )
    curs1 = conn1.cursor(pymysql.cursors.DictCursor)    

    conn2 = pymysql.connect(host='localhost', user='db2021', password='db2021', db='imdb', unix_socket='/tmp/mysql.sock' )
    curs2 = conn2.cursor(pymysql.cursors.DictCursor)    
    
    conn3 = pymysql.connect(host='localhost', user='db2021', password='db2021', db='imdb', unix_socket='/tmp/mysql.sock' )
    curs3 = conn3.cursor(pymysql.cursors.DictCursor)  

    load_sql = """select * from title_basics"""
    curs1.execute(load_sql)

    rows = curs1.fetchmany(10000)
    insertCount = 0
    while rows:
        
        inserts_movie = []
        inserts_genres = []
        for row in rows:
            isAdult = 0 if (row['isAdult'] == '0') else 1
            startYear = int(row['startYear']) if (row['startYear'] != '\\N') else None
            endYear = int(row['endYear']) if (row['endYear'] != '\\N') else None
            runtimeMinutes = int(row['runtimeMinutes']) if (row['runtimeMinutes'] != '\\N') else None
            genres = row['genres'].split(',') if (row['genres'] != '\\N') else None
            
            if genres != None:
                for genre in genres:
                    inserts_genres.append([row['tconst'], genre])    

            inserts_movie.append([row['tconst'], row['titleType'], row['primaryTitle'], row['originalTitle'], 
                            isAdult, startYear, endYear, runtimeMinutes])

        insert_sql = """insert into movie (tconst, titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes)
                        values (%s, %s, %s, %s, %s, %s, %s, %s)"""
        curs2.executemany(insert_sql, inserts_movie)
        conn2.commit()
        
        insert_genres_sql = """insert into genres (tconst, genre) values (%s, %s)"""
        curs3.executemany(insert_genres_sql, inserts_genres)
        conn3.commit()

        insertCount += len(inserts_movie)
        print("%d rows commit" %(insertCount))

        rows = curs1.fetchmany(10000)

    curs3.close()
    conn3.close()
    curs2.close()
    conn2.close()
    curs1.close()
    conn1.close()

def insert_akas_type_attribute():

    conn = []
    curs = []
    for i in range(4):
        conn.append(pymysql.connect(host='localhost', user='db2021', password='db2021', db='imdb', unix_socket='/tmp/mysql.sock' ))
        curs.append(conn[i].cursor(pymysql.cursors.DictCursor) )
        

    # tt0000001 ~ tt7972848
    load_sql = """select * from title_akas where 'tt9000000' <= titleid"""
    curs[0].execute(load_sql)

    rows = curs[0].fetchmany(10000)
    while rows:
        
        insert_akas = []
        insert_types = []
        insert_attributes = []
        for row in rows:

            region = row['region'] if (row['region'] != '\\N') else None
            language = row['language'] if (row['language'] != '\\N') else None
            isOriginalTitle = int(row['isOriginalTitle']) if (row['isOriginalTitle'] != '\\N') else None

            insert_akas.append([row['titleid'], row['ordering'], row['title'], region, language, isOriginalTitle])

            types = row['types'].split(',') if (row['types'] != '\\N') else None
            if types != None:
                for mtype in types:
                    insert_types.append([row['titleid'], row['ordering'], mtype])    

            attributes = row['attributes'].split(',') if (row['attributes'] != '\\N') else None
            if attributes != None:
                for attribute in attributes:
                    insert_attributes.append([row['titleid'], row['ordering'], attribute])
                            
        insert_sql = """insert into akas (tconst, ordering, title, region, language, isOriginalTitle)
                        values (%s, %s, %s, %s, %s, %s)"""
        curs[1].executemany(insert_sql, insert_akas)
        conn[1].commit()
        
        insert_sql = """insert into akas_types (tconst, ordering, type) values (%s, %s, %s)"""
        curs[2].executemany(insert_sql, insert_types)
        conn[2].commit()

        insert_sql = """insert into akas_attributes (tconst, ordering, attribute) values (%s, %s, %s)"""
        curs[3].executemany(insert_sql, insert_attributes)
        conn[3].commit()

        print(rows[-1]['titleid'], " commit")

        rows = curs[0].fetchmany(10000)

    for i in range(4):
        curs[i].close()
        conn[i].close()

def insert_directors_writers():
    conn = []
    curs = []
    for i in range(3):
        conn.append(pymysql.connect(host='localhost', user='db2021', password='db2021', db='imdb', unix_socket='/tmp/mysql.sock' ))
        curs.append(conn[i].cursor(pymysql.cursors.DictCursor) )    
    
    load_sql = """select * from title_crew"""
    curs[0].execute(load_sql)

    rows = curs[0].fetchmany(10000)

    while rows:

        insert_directors = []
        insert_writers = []
        for row in rows:
            directors = row['directors'].split(',') if (row['directors'] != '\\N') else None
            writers = row['writers'].split(',') if (row['writers'] != '\\N') else None

            if directors != None:
                for director in directors:
                    insert_directors.append([row['tconst'], director])

            if writers != None:
                for writer in writers:
                    insert_writers.append([row['tconst'], writer])

        insert_sql = 'insert into directors (tconst, director) values (%s, %s)'
        curs[1].executemany(insert_sql, insert_directors)
        conn[1].commit()
        
        insert_sql = 'insert into writers (tconst, writer) values (%s, %s)'
        curs[2].executemany(insert_sql, insert_writers)
        conn[2].commit()

        print(rows[-1]['tconst'], " commit")
        rows = curs[0].fetchmany(10000)

    for i in range(3):
        curs[i].close()
        conn[i].close()

def insert_person_profession_title():
    conn = []
    curs = []
    for i in range(4):
        conn.append(pymysql.connect(host='localhost', user='db2021', password='db2021', db='imdb', unix_socket='/tmp/mysql.sock' ))
        curs.append(conn[i].cursor(pymysql.cursors.DictCursor) )
        
    load_sql = 'select * from name_basics'
    curs[0].execute(load_sql)

    rows = curs[0].fetchmany(10000)
    while rows:
        
        insert_person = []
        insert_professions = []
        insert_titles = []
        for row in rows:

            primaryName = row['primaryName'] if (row['primaryName'] != '\\N') else None
            birthYear = int(row['birthYear']) if (row['birthYear'] != '\\N') else None
            deathYear = int(row['deathYear']) if (row['deathYear'] != '\\N') else None

            insert_person.append([row['nconst'], primaryName, birthYear, deathYear])

            professions = row['primaryProfession'].split(',') if (row['primaryProfession'] != '\\N') else None
            if professions != None:
                for profession in professions:
                    insert_professions.append([row['nconst'], profession])    

            titles = row['knownForTitles'].split(',') if (row['knownForTitles'] != '\\N') else None
            if titles != None:
                for title in titles:
                    insert_titles.append([row['nconst'], title])    
                            
        insert_sql = """insert into person (nconst, primaryName, birthYear, deathYear)
                        values (%s, %s, %s, %s)"""
        curs[1].executemany(insert_sql, insert_person)
        conn[1].commit()
        
        insert_sql = """insert into professions (nconst, profession) values (%s, %s)"""
        curs[2].executemany(insert_sql, insert_professions)
        conn[2].commit()

        insert_sql = """insert into knownForTitles (nconst, tconst) values (%s, %s)"""
        curs[3].executemany(insert_sql, insert_titles)
        conn[3].commit()

        print(rows[-1]['nconst'], " commit")

        rows = curs[0].fetchmany(10000)

    for i in range(4):
        curs[i].close()
        conn[i].close()


if __name__ == '__main__':
    start_time = time.time()
    # insert_movie_genre()          7972266 rows commit / 617.7457420825958 seconds
    # insert_akas_type_attribute()
    # insert_directors_writers()
    # insert_person_profession_title()
    elapsed_time = time.time() - start_time     
    print(elapsed_time, 'seconds')

