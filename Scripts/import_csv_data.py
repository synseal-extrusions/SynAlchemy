# script to import data from csv and import into SQLite db

# import libs
import csv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:////home/ashleyc/Desktop/SynAlchemyApp/SynAlchemy/Scripts/dev.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class DeliveryNotes(Base):
	__tablename__ = "deliverynotes"

	id = Column(Integer, primary_key=True)
	alchemy_id = Column(Integer)
	NextID = Column(Integer)
	ParentID = Column(Integer)
	Folder = Column(Integer)
	Document_ID = Column(String)
	File_Name = Column(String)
	File_Directory = Column(String)
	File_Size = Column(Integer)
	File_Format = Column(String)
	File_Date = Column(String)
	Folder_Title = Column(String)
	Account_Code = Column(String)
	Delivery_Date = Column(String)
	Full_Text = Column(String)
	OCR = Column(String)

def import_data():
	"""
	Import the csv data and return the raw csv data
	"""
	csv_data = []
	with open('csv_data.csv') as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for row in readCSV:
			csv_data.append(row)
	return csv_data

def import_csv_to_sql(data):
	"""
	Take raw CSV data and import into SQL
	Returns list of failed records
	"""
	session = Session()
	new_record = DeliveryNotes(alchemy_id = data[0],
							   NextID = data[1],
							   ParentID = data[2],
							   Folder = data[3],
							   Document_ID = data[4],
							   File_Name = data[5],
							   File_Directory = data[6],
							   File_Size = data[7],
							   File_Format = data[8],
							   File_Date = data[9],
							   Folder_Title = data[10],
							   Account_Code = data[11],
							   Delivery_Date = data[12])
	session.add(new_record)
	session.commit()

Base.metadata.create_all(engine)
raw_data = import_data()
for i in raw_data:
	import_csv_to_sql(i)