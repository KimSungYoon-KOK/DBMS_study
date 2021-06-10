import pymysql
import time

# =========================== Load title.akas.tsv ===========================
def load_title_akas():

    conn = pymysql.connect(host='localhost', user='db2021', 
                password='db2021', db='imdb', unix_socket='/tmp/mysql.sock' )
    
    cur = conn.cursor(pymysql.cursors.DictCursor)    
    
    filename = 'IMDB/title.akas.tsv'
    f = open(filename, "r")
    
    insert_sql = """insert into title_akas (titleid, ordering, title, region, language, types, attributes, isOriginalTitle)
                    values (%s, %s, %s, %s, %s, %s, %s, %s)"""
    
    header = f.readline()

    oneline = f.readline()[:-1]

    rows = []
    i = 0
    
    while oneline:
        attrs = tuple(oneline.split('\t'))
        rows.append(attrs)
        i += 1
        if i % 10000 == 0:
            cur.executemany(insert_sql, rows)
            conn.commit()
            rows = []
            print("%d rows" %i)
        
        oneline = f.readline()[:-1]
        
    if rows:
        cur.executemany(insert_sql, rows)
        conn.commit()
        print("%d rows" %i)
        
    
    f.close()
    cur.close()
    conn.close()

    # 26527937 rows
    # 543.3900921344757 seconds


# =========================== Load title.basics.tsv ===========================
def load_title_basics():
    
    conn = pymysql.connect(host='localhost', user='db2021', 
                password='db2021', db='imdb', unix_socket='/tmp/mysql.sock' )
    
    cur = conn.cursor(pymysql.cursors.DictCursor) 

    filename = 'IMDB/title.basics.tsv'
    f = open(filename, "r")

    insert_sql = """insert into title_basics (tconst, titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, genres)
                    values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    header = f.readline()

    oneline = f.readline()[:-1]

    rows = []
    i = 0
    
    while oneline:
        attrs = tuple(oneline.split('\t'))
        rows.append(attrs)
        i += 1
        if i % 10000 == 0:
            cur.executemany(insert_sql, rows)
            conn.commit()
            rows = []
            print("%d rows" %i)
        
        oneline = f.readline()[:-1]
        
    if rows:
        cur.executemany(insert_sql, rows)
        conn.commit()
        print("%d rows" %i)

    f.close()
    cur.close()
    conn.close()
    # 7972266 rows
    # 191.37886309623718 seconds


# =========================== Load title.crew.tsv ===========================
def load_title_crew():
    
    conn = pymysql.connect(host='localhost', user='db2021', 
                password='db2021', db='imdb', unix_socket='/tmp/mysql.sock' )
    
    cur = conn.cursor(pymysql.cursors.DictCursor)

    filename = 'IMDB/title.crew.tsv'
    f = open(filename, "r")

    insert_sql = """insert into title_crew (tconst, directors, writers)
                    values (%s, %s, %s)"""

    header = f.readline()

    oneline = f.readline()[:-1]

    rows = []
    i = 0
    
    while oneline:
        attrs = tuple(oneline.split('\t'))
        rows.append(attrs)
        i += 1
        if i % 10000 == 0:
            cur.executemany(insert_sql, rows)
            conn.commit()
            rows = []
            print("%d rows" %i)
        
        oneline = f.readline()[:-1]
        
    if rows:
        cur.executemany(insert_sql, rows)
        conn.commit()
        print("%d rows" %i)

    f.close()
    cur.close()
    conn.close()
    # 7972266 rows
    # 101.66893601417542 seconds


# =========================== Load title.episode.tsv ===========================
def load_title_episode():
    
    conn = pymysql.connect(host='localhost', user='db2021', 
                password='db2021', db='imdb', unix_socket='/tmp/mysql.sock' )
    
    cur = conn.cursor(pymysql.cursors.DictCursor)

    filename = 'IMDB/title.episode.tsv'
    f = open(filename, "r")

    insert_sql = """insert into title_episode (tconst, parentTconst, seasonNumber, episodeNumber)
                    values (%s, %s, %s, %s)"""

    header = f.readline()

    oneline = f.readline()[:-1]

    rows = []
    i = 0
    
    while oneline:
        attrs = tuple(oneline.split('\t'))
        rows.append(attrs)
        i += 1
        if i % 10000 == 0:
            cur.executemany(insert_sql, rows)
            conn.commit()
            rows = []
            print("%d rows" %i)
        
        oneline = f.readline()[:-1]
        
    if rows:
        cur.executemany(insert_sql, rows)
        conn.commit()
        print("%d rows" %i)


    f.close()
    cur.close()
    conn.close()    
    # 5819401 rows
    # 76.50134491920471 seconds


# =========================== Load title.principals.tsv ===========================
def load_title_principals():
    
    conn = pymysql.connect(host='localhost', user='db2021', 
                password='db2021', db='imdb', unix_socket='/tmp/mysql.sock' )
    
    cur = conn.cursor(pymysql.cursors.DictCursor)  

    filename = 'IMDB/title.principals.tsv'
    f = open(filename, "r")

    insert_sql = """insert into title_principals (tconst, ordering, nconst, category, job, characters)
                    values (%s, %s, %s, %s, %s, %s)"""

    header = f.readline()

    oneline = f.readline()[:-1]

    rows = []
    i = 0
    
    while oneline:
        attrs = tuple(oneline.split('\t'))
        rows.append(attrs)
        i += 1
        if i % 10000 == 0:
            cur.executemany(insert_sql, rows)
            conn.commit()
            rows = []
            print("%d rows" %i)
        
        oneline = f.readline()[:-1]
        
    if rows:
        cur.executemany(insert_sql, rows)
        conn.commit()
        print("%d rows" %i)

    f.close()
    cur.close()
    conn.close()
    # 45134176 rows
    # 782.6083562374115 seconds


# =========================== Load title.ratings.tsv ===========================
def load_title_ratings():
    
    conn = pymysql.connect(host='localhost', user='db2021', 
                password='db2021', db='imdb', unix_socket='/tmp/mysql.sock' )
    
    cur = conn.cursor(pymysql.cursors.DictCursor)

    filename = 'IMDB/title.ratings.tsv'
    f = open(filename, "r")

    insert_sql = """insert into title_ratings (tconst, averageRating, numVotes)
                    values (%s, %s, %s)"""

    header = f.readline()

    oneline = f.readline()[:-1]

    rows = []
    i = 0
    
    while oneline:
        attrs = tuple(oneline.split('\t'))
        rows.append(attrs)
        i += 1
        if i % 10000 == 0:
            cur.executemany(insert_sql, rows)
            conn.commit()
            rows = []
            print("%d rows" %i)
        
        oneline = f.readline()[:-1]
        
    if rows:
        cur.executemany(insert_sql, rows)
        conn.commit()
        print("%d rows" %i)

    f.close()
    cur.close()
    conn.close()
    # 1160085 rows
    # 13.532559871673584 seconds


# =========================== Load name.basics.tsv ===========================
def load_name_basics():
    
    conn = pymysql.connect(host='localhost', user='db2021', 
                password='db2021', db='imdb', unix_socket='/tmp/mysql.sock' )
    
    cur = conn.cursor(pymysql.cursors.DictCursor)   

    filename = 'IMDB/name.basics.tsv'
    f = open(filename, "r")

    insert_sql = """insert into name_basics (nconst, primaryName, birthYear, deathYear, primaryProfession, knownForTitles)
                    values (%s, %s, %s, %s, %s, %s)"""

    header = f.readline()

    oneline = f.readline()[:-1]

    rows = []
    i = 0
    
    while oneline:
        attrs = tuple(oneline.split('\t'))
        rows.append(attrs)
        i += 1
        if i % 10000 == 0:
            cur.executemany(insert_sql, rows)
            conn.commit()
            rows = []
            print("%d rows" %i)
        
        oneline = f.readline()[:-1]
        
    if rows:
        cur.executemany(insert_sql, rows)
        conn.commit()
        print("%d rows" %i)

    f.close()
    cur.close()
    conn.close()  
    # 10986793 rows
    # 205.14772987365723 seconds  


if __name__ == '__main__':
    start_time = time.time()
    load_title_akas()         # 26527937 rows
    load_title_basics()       #  7972266 rows
    load_title_crew()         #  7972266 rows
    load_title_episode()      #  5819401 rows
    load_title_principals()   # 45134176 rows
    load_title_ratings()      #  1160085 rows
    load_name_basics()        # 10986793 rows
    elapsed_time = time.time() - start_time     
    print(elapsed_time, 'seconds')
    