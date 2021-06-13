import pymysql
import time

class Search:
    
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='db2021', password='db2021', db='imdb', unix_socket='/tmp/mysql.sock')
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
        
    def exit_fun(self):
        self.curs.close()
        self.conn.close()
        return False

    # 필수1 : 영화제목을 입력하여, 이에 매칭되는 영화를 검색
    def movieTitle(self):
        title = input("검색할 영화 제목을 입력하세요 : ")

        start_time = time.time()

        sql = """select m.*, GROUP_CONCAT(g.genre) as genres
                from movie m, genres g
                where m.primaryTitle = '%s' and m.titleType = 'movie' and m.tconst = g.tconst
                group by m.tconst
                order by tconst""" %(title)
        self.curs.execute(sql)
        rows = self.curs.fetchall()

        if len(rows) == 0:
            print("찾으시는 영화가 없습니다. 제목을 다시 확인하세요.")

        for row in rows:
            isAdult = "(청소년 관람 불가)" if row['isAdult'] == 1 else "(청소년 관람 가능)"
            print("제목 : %s %s, 개봉기간 : %s ~ %s, 러닝 타임 : %s분, 장르 : %s" %(row['primaryTitle'], isAdult, row['startYear'], row['endYear'], row['runtimeMinutes'], row['genres']))
        
        elapsed_time = time.time() - start_time     
        print(elapsed_time, 'seconds\n')
        return True   


    # 필수2 : 특정 배우가 등장하는 영화를 별점이 높은 순으로 검색
    def actor(self):
        name = input("검색할 배우 이름을 입력하세요 : ")
        start_time = time.time()
        sql = """select m.primaryTitle, pr.characters, r.averageRating, r.numVotes
                from person p, knownForTitles k, ratings r, movie m, principals pr
                where p.primaryName = '%s' and k.nconst = p.nconst and k.tconst = r.tconst 
                    and k.tconst = m.tconst and (pr.tconst, pr.nconst) = (k.tconst, p.nconst)
                order by r.averageRating desc;""" %(name)

        self.curs.execute(sql)
        rows = self.curs.fetchall()

        if len(rows) == 0:
            print("찾으시는 배우가 없습니다. 이름을 다시 확인하세요.")

        for row in rows:
            characters = row['characters'][2:-2]
            print("출연 영화 : %s, 배역 : %s, 별점 : %s" %(row['primaryTitle'], characters, row['averageRating']))
        
        elapsed_time = time.time() - start_time     
        print(elapsed_time, 'seconds')
        return True       
    
    # 필수3 : 특정 감독이 제작한 영화를 개봉연도순으로 검색
    def director(self):
        director = input("검색할 감독 이름을 입력하세요 : ")

        start_time = time.time()

        sql = """select m.*
                from person p, directors d, movie m
                where p.primaryName = '%s' and p.nconst = d.director and d.tconst = m.tconst
                order by m.startYear""" %(director)
        self.curs.execute(sql)
        rows = self.curs.fetchall()

        if len(rows) == 0:
            print("찾으시는 감독이 없습니다. 이름을 다시 확인하세요.")

        for row in rows:
            isAdult = "(청소년 관람 불가)" if row['isAdult'] == 1 else "(청소년 관람 가능)"
            print("제목 : %s %s, 개봉기간 : %s ~ %s, 러닝 타임 : %s분" %(row['primaryTitle'], isAdult, row['startYear'], row['endYear'], row['runtimeMinutes']))
        
        elapsed_time = time.time() - start_time     
        print(elapsed_time, 'seconds\n')
        return True   
    
    
    # 필수4 : Drama 장르의 영화를 리뷰가 많은 순 또는 별점이 높은순으로 검색
    def genre(self):
        select = input("정렬 기준을 입력하세요 (1.리뷰 개수 2. 별점): ")
        sorting = "r.numVotes" if (select == "1") else "r.averageRating"

        start_time = time.time()

        sql = """select g.genre, m.*, r.averageRating, r.numVotes
                from ratings r, genres g, movie m
                where g.genre = 'Drama' and g.tconst = m.tconst and m.titleType = 'movie' and m.tconst = r.tconst
                order by %s desc limit 100""" %(sorting)
        self.curs.execute(sql)
        rows = self.curs.fetchall()

        for row in rows:
            print("제목 : %s, 평점 : %s, 리뷰 개수 : %s" %(row['primaryTitle'], row['averageRating'], row['numVotes']))

        
        elapsed_time = time.time() - start_time     
        print(elapsed_time, 'seconds\n')
        return True  

    # 선택1 : 특정 연도에 개봉한 영화중 가장 인기 있는 영화 랭킹 Top10
    # 인기 기준 : 리뷰 수가 500개 이상인 영화 중 평점이 높은 순위
    def startYear(self):
        year = input("검색할 연도를 입력하세요 : ")
        start_time = time.time()

        sql = """select r.averageRating, r.numVotes, m.*
                from ratings r join movie m on m.tconst = r.tconst
                where m.startYear = %s and r.numVotes >= 500 and m.titleType = 'movie'
                order by r.averageRating desc limit 10""" %(year)
        self.curs.execute(sql)
        rows = self.curs.fetchall()

        for i, row in enumerate(rows):
            print("%s. 제목 : %s, 평점 : %s, 리뷰 개수 : %s" %(i+1, row['primaryTitle'], row['averageRating'], row['numVotes']))

        
        elapsed_time = time.time() - start_time     
        print(elapsed_time, 'seconds\n')
        return True



if __name__ == '__main__':
    search = Search()
    functions = {
            '0': search.exit_fun,
            '1': search.movieTitle, '2': search.actor, '3': search.director,
            '4': search.genre ,  '5': search.startYear
        }  
    flag = True
    while flag:
        print("[IMDB 검색 프로그램]")
        print("0. 프로그램 종료\n1. 영화 제목으로 검색\n2. 배우 이름으로 검색\n3. 감독으로 검색\n4. 드라마 장르 영화 Top100\n5. 연도별 영화 랭킹 Top10")
        insert = input("사용할 메뉴를 입력하세요: ")
        flag = functions[insert]()
        


"""
1. 영화 제목 검색
Titanic
Dingle, Dangle (성인영화)
asdfasd

2. 영화 배우 검색
Carrie-Anne Moss

3. 감독 검색
Christopher Nolan
"""