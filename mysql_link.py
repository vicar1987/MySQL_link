import pymysql

host = 'localhost'
port = 3306
user = 'root'
passwd = 'root'
db = 'testdb'
charset = 'utf8'

conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
cursor = conn.cursor()

cursor.close()
conn.close()