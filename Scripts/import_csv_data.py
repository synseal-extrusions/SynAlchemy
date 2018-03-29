# script to import data from csv and import into SQLite db

# import libs
import sys

sys.dont_write_bytecode = True
import csv
import ntpath
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import shutil

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
	New_File_Path = Column(String)

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

def process_files(data):
	"""
	Copy file for given record to new location,
	generate new file path and return it to be added
	to SQL. 
	"""
	root_dir = "X:\\Alchemy Data\\"
	new_root_dir = "E:\\Data\\" # where all of the file structure needs to be moved to
	file_name = data[5]
	file_dir = data[6][2:]
	old_fq_path = "{}{}\\{}".format(root_dir,file_dir,file_name)
	fq_path = "{}{}\\{}".format(new_root_dir,file_dir,file_name)
	data.append(fq_path)

	#shutil.copy2(old_fq_path, fq_path) still needs testing
	return data

def import_csv_to_sql(data):
	"""
	Take raw CSV data and import into SQL
	Returns list of failed records
	"""
	try:
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
									Delivery_Date = data[12],
									New_File_Path = data[13])
		session.add(new_record)
		session.commit()
	except:
		print "There has been an issue with alchemy_id = {}".format(data[0])

Base.metadata.create_all(engine)
raw_data = import_data()
for i in raw_data:
	if len(i) == 14:
		i = i[:-2] # remove last two fields of data as useless 
	if len(i) == 16:
		i = i[:-4]
	processed = process_files(i)
	import_csv_to_sql(processed)
