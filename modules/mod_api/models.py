from sqlalchemy import Column, Integer, String, DateTime
from SynAlchemy.database import Base
import datetime

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