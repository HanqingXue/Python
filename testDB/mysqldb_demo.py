import MySQLdb
from DBUtils.PooledDB import PooledDB
pool = PooledDB(MySQLdb,5,host='localhost',user='root',passwd='pwd',db='myDB',port=3306) #5为连接池里的最少连接数

 
conn = pool.connection()  #以后每次需要数据库连接就是用connection（）函数获取连接就好了
cur=conn.cursor()
SQL="select * from table1"
r=cur.execute(SQL)
r=cur.fetchall()
cur.close()
conn.close()