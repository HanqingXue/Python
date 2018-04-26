#coding=utf-8

import logging
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Employee(Base):
	__tablename__ = 'employee'

	first_name = Column(String(20), primary_key=True)
	last_name = Column(String(20)) 
	age = Column(Integer)
	sex = Column(String(20))
	income = Column(Integer)

def main():
	user_name = "root"
	passwd = "hitxhq"
	addr = "localhost"
	port = "3305"
	database = "test"
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


class Geneinfo(Base):
	__tablename__ = "geneinfo_ncbihgnc"

	table_ID = Column(Integer, primary_key=True)
	gene_id = Column(String(64))
	entrez_id = Column(Integer)
	Gene_Symbol = Column(String(32))
	HGNC_id = Column(String(32))
	synonyms = Column(String(64))
	Chr =  Column(String(32))
	chromosome_band = Column(String(32))
	type_of_gene = Column(String(32))
	description = Column(String(128))

def test_fudan_mysql():
	user_name = "lijie"
	passwd = "lijie_kb5"
	host = "111.198.139.95"
	port = "3306"
	database = "medicine_database"
	engine = create_engine('mysql+mysqlconnector://{0}:{1}@{2}:{3}/{4}'.format(
		user_name, passwd, host, port, database))

	#db_session = sessionmaker(bind=engine)

	db_session  = scoped_session(sessionmaker(bind=engine,
                        autocommit=True, autoflush=True, expire_on_commit=False))

	session = db_session()

	gene_info = {}

	try:
		gene = session.query(Geneinfo).filter(Geneinfo.Gene_Symbol == 'ABAT').one()

		gene_info = {
			'entrez': gene.entrez_id,
			'HGNC': gene.HGNC_id,
			'synonyms': gene.synonyms,
			'chr':gene.Chr,
			'chromosome_band': gene.chromosome_band,
			'type':gene.type_of_gene,
			'description': gene.description
		}

	except Exception as ex:
		logging.error('Error occurred: %s' % ex)

	return gene_info
	

if __name__ == '__main__':
	test_fudan_mysql()