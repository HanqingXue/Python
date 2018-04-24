#coding=utf-8

import MySQLdb
import sys, string, os 

class MySQLOperator(object):
	"""docstring for ClassName"""
	def __init__(self):
		super(MySQLOperator, self).__init__()
		'''
		Eestablish a connection.
		'''
		self.conn = MySQLdb.connect(host='localhost',
					user='root',
					db='test',
					passwd='hitxhq',
					port=3305)
		
	def create_table(self):
		try:
			'''
			Set a cursor
			'''
			cursor = self.conn.cursor()
			'''
			If there is an existed table, drop it. 
			'''
			cursor.execute('DROP TABLE IF EXISTS EMPLOYEE')
			'''
			Create a table named EMPLOYEE
			'''
			sql = """CREATE TABLE EMPLOYEE (
				FIRST_NAME CHAR(20) NOT NULL,
				LAST_NAME CHAR(20),
				AGE INT,
				SEX CHAR(1),
				INCOME FLOAT)"""		

			cursor.execute(sql)		

			'''
			Close a connection
			'''
			print 'The table EMPLOYEE is established!'
			cursor.close()

		except Exception as e:
			print e
			sys.exit()

	def insert(self, person):
		'''
		sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ({0}, '{1}', {2}, {3}, {4})""".format(
         person['FIRST_NAME'], person['LAST_NAME'], person['AGE'], person['SEX'], person['INCOME'])
        '''
		sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
		LAST_NAME, AGE, SEX, INCOME)
		VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""

		cursor = self.conn.cursor()
		try:
			cursor.execute(sql)
			self.conn.commit()
		except Exception as e:
			self.conn.rollback()
			raise e
		
		print 'Insert Successfully!'
		cursor.close()

	def update(self):
		sql = "DELETE FROM EMPLOYEE WHERE AGE >= '%d'" % (20)

		cursor = self.conn.cursor()
		try:
			cursor.execute(sql)
			self.conn.commit()
			self.search()
		except Exception as e:
			self.rollback()
			print 'Update fail'
			raise e

		cursor.close()
		pass

	def search(self):
		sql = "SELECT * FROM EMPLOYEE"

		cursor = self.conn.cursor()
		cursor.execute(sql)

		try:
			results = cursor.fetchall()
			for row in results:
				fname = row[0]
				lname = row[1]
				age = row[2]
				sex = row[3]
				income = row[4]

				print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
				(fname, lname, age, sex, income )

		except Exception as e:
			print 'Cannot fetch data!'
		pass

	def close_connection(self):
		self.conn.close()
		print 'Connection closed'

def main():
	db_operator = MySQLOperator()
	db_operator.create_table()
	person = { 'FIRST_NAME': "Mac",
				'LAST_NAME': "Mohan",
				'AGE': 20,
				'SEX': "M",
				'INCOME': 2000
	}
	db_operator.insert(person)
	db_operator.search()
	db_operator.update()
	db_operator.search()
	db_operator.close_connection()
	pass
if __name__ == '__main__':
	main()