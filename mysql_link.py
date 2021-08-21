import pymysql

host = 'localhost' or 'IP address'
port = 3306
user = 'username'
passwd = 'password'
db = 'db_name'
charset = 'utf8'

conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
cursor = conn.cursor()

cursor.close()
conn.close()
