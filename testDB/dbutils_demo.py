import sys
import threading
import MySQLdb
import DBUtils.PooledDB

def test(conn):
    try:
        cursor = conn.cursor()
        sql = "SELECT * FROM geneinfo_ncbihgnc  WHERE Gene_Symbol = 'A2M'"
        count = cursor.execute(sql)
        rows = cursor.fetchall()
        for r in rows: pass
    finally:
        conn.close()
        
def testloop():
    print ("testloop")
    for i in range(10):
        conn = MySQLdb.connect(**connargs)
        test(conn)
        
def testpool():
    print ("testpool")
    pooled = DBUtils.PooledDB.PooledDB(MySQLdb, **connargs)
    for i in range(10):
        conn = pooled.connection()
        test(conn)
        
def main():
    t = testloop if len(sys.argv) == 1 else testpool
    for i in range(10):
        threading.Thread(target = t).start()
        
if __name__ == "__main__":
    main()