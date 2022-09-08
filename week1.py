import pymysql
db = pymysql.Connect(host='localhost', user='root', password='root', database='test')
cursor = db.cursor()
query1 = "SELECT * FROM TEST"
cursor.execute(query1)
result = cursor.fetchall()
print(result)

query2 = "SELECT * FROM TEST WHERE code = 201710771"
cursor.execute(query2)
result2 = cursor.fetchall()
print(result2)
