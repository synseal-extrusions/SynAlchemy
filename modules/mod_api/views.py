import os
from flask import render_template, session, Blueprint, jsonify, request, json, url_for

from SynAlchemy import application, _basedir
from SynAlchemy.modules.mod_api.models import DeliveryNotes
from SynAlchemy.database import db_session

api_blueprint = Blueprint('api_blueprint', __name__,
						template_folder=os.path.join(_basedir, 'templates', 'api'))

@api_blueprint.route('/deliverynotes', methods=['GET'])
def get_deliverynotes():
	results = db_session.query(DeliveryNotes).all()
	deliverynotes = []
	for deliverynote in results:
		delivernotedata = {}
		delivernotedata['alchemy_id'] = deliverynote.alchemy_id
		delivernotedata['NextID'] = deliverynote.NextID
		delivernotedata['ParentID'] = deliverynote.ParentID
		delivernotedata['Folder'] = deliverynote.Folder
		delivernotedata['Document_ID'] = deliverynote.Document_ID
		delivernotedata['File_Name'] = deliverynote.File_Name
		delivernotedata['File_Directory'] = deliverynote.File_Directory
		delivernotedata['File_Size'] = deliverynote.File_Size
		delivernotedata['File_Format'] = deliverynote.File_Format
		delivernotedata['File_Date'] = deliverynote.File_Date
		delivernotedata['Folder_Title'] = deliverynote.Folder_Title
		delivernotedata['Account_Code'] = deliverynote.Account_Code
		delivernotedata['Delivery_Date'] = deliverynote.Delivery_Date
		deliverynotes.append(delivernotedata)
	return jsonify(deliverynotes)