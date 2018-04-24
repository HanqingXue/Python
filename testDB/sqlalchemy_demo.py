#coding=utf-8

from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Employee(Base):
	"""docstring for Employee"""
	__tablename__ = 'employee'

	first_name = Column(String(20), primary_key=True)
	last_name = Column(String(20)) 
	age = Column(Integer)
	sex = Column(String(20))
	income = Column(Integer)

if __name__ == '__main__':
	engine = create_engine('mysql+mysqlconnector://root:hitxhq@localhost:3305/test')
	'''
	Setup a new session
	'''
	DBSession = sessionmaker(bind=engine)
	'''
	New a employee
	'''
	new_employee = Employee(first_name='Mike', last_name='Jack', age=22, sex='M', income=100)

	'''
	add a new record.
	'''
	session = DBSession()
	session.add(new_employee)
	session.commit()
	session.close()
	'''
	Search a employee record.
	'''
	session = DBSession()
	user = session.query(Employee).filter(Employee.age == 22).one()
	print 'First_name:{0}\t Last_name:{1}\t Age:{2}\t Sex:{3}\t Income:{4}'.format( \
		user.first_name, user.last_name, user.age, user.sex, user.income)
	pass
	session.commit()
	session.close()		