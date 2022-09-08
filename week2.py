import pymysql

db = pymysql.Connect(host='localhost', user='root', password='root', database='human')

cursor = db.cursor()

# query = "SELECT * FROM TEST WHERE grade=3"
query1 = "SELECT name FROM HUMAN where blood = 'A'"
query2 = "SELECT name FROM HUMAN where blood = 'A' and age > 23"

cursor.execute(query1)
# cursor.execute(query2)
result = cursor.fetchall()

for re in result:
    print(re)