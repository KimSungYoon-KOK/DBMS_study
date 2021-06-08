import pymysql
import time

def load_title_akas():

    conn = pymysql.connect(host='localhost', user='db', 
                password='db', db='university', unix_socket='/tmp/mysql.sock' )
    
    cur = conn.cursor(pymysql.cursors.DictCursor)    
    
    filename = 'title.akas.tsv'
    f = open(filename, "r")
    
    insert_sql = """insert into title_akas (titleid, ordering, title, region, language, types, attributes, isOriginalTitle)
                    values (%s, %s, %s, %s, %s, %s, %s, %s)"""
    
    oneline = f.readline()

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


if __name__ == '__main__':
    start_time = time.time()
    load_title_akas()
    elapsed_time = time.time() - start_time
    print(elapsed_time, 'seconds')
    