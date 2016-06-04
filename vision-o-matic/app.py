#!/usr/bin/env python
import os
from clarifai.client import ClarifaiApi
from flask import Flask, flash, request, jsonify, redirect, url_for
import MySQLdb
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads').replace('\\','/')
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])
clarifai_api = ClarifaiApi() # assumes environment variables are set.


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "supersecretkey"

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def get_nutri_facts(lst):
	# Open database connection
	db = MySQLdb.connect(host="192.168.99.100", port=32768 ,user="root",db="scanomatic" )

	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	# Prepare SQL query to INSERT a record into the database.
	sql = "SELECT * FROM alimentos \
		   WHERE Alimento='%s' OR  Alimento='%s' \
		   OR Alimento='%s' " %(str(lst[0]), str(lst[1]), str(lst[2]))
	try:
		# Execute the SQL command
	   	cursor.execute(sql)
	   	# Fetch all the rows in a list of lists.
	   	results = cursor.fetchall()
	   	for row in results:
	   		res = {
            'id': row[0],
	      	'Alimento': row[1],
	      	'Calorias': row[2],
	      	'Grasas_total': row[3],
	      	'Acidos_grasos_saturados': row[4],
	     	'Acidos_grasos_poliinsaturados': row[5],
	     	'Acidos_grasos_monoinsaturados': row[6],
	    	'Colesterol': row[7],
	   	   	'Sodio': row[8],
	      	'Potasio': row[9],
	      	'Carbohidratos': row[10],
	      	'Fibra': row[11],
	 	    'Azucares': row[12],
	      	'Proteinas': row[13],
	     	'Hierro': row[14],
	      	'Calcio': row[15],
	      	'Magnesio': row[16],
		    'VitaminA': row[17],
	      	'VitaminB6': row[18],
	      	'VitaminB12': row[19],
		    'VitaminC': row[20],
	      	'VitaminD': row[21],
	      	'VitaminE': row[22],
	      	'VitaminF': row[23]
			}
	except:
		print "No pudimos encontrar tu alimento."

	# disconnect from server
	db.close()
	return res

def is_healthy(res):
	nutri = {}
	nutri["Alimento"] = res['Alimento']
	if res['Calorias'] < 80:
		nutri['Calorias'] = 1
	else :
		nutri['Calorias'] = 0
	if res['Grasas_total'] < 0.5:
		nutri['Grasas_total'] = 1
	else:
		nutri['Grasas_total'] = 0
	if ( res['VitaminB6'] + res['Potasio'] + res['VitaminF'] + res['VitaminD'] + res['VitaminE']+ res['VitaminC'] + res['VitaminA'] + res['VitaminB12'] + res['Sodio'] + res['Hierro'] + res['Magnesio'] + res['Calcio'] ) > 200:
		nutri["Vitaminas"] = 1
	else:
		nutri["Vitaminas"] = 0
	if res['Proteinas'] > 0.55:
		nutri['Proteinas'] = 1
	else:
		nutri['Proteinas'] = 0
	return nutri



@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            print request
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            result = clarifai_api.tag_images(open(os.path.join('/Users/iorch/misc/scan-o-matic/vision-o-matic/uploads', filename), 'rb'))
            mylist = result['results'][0]['result']['tag']['classes']
            result = get_nutri_facts(mylist)
            hly = is_healthy(result)
            message = {
                'status': 200,
                'message': hly,
            }
            resp = jsonify(message)
            resp.status_code = 200
            return resp #redirect(url_for('upload_file',
                        #            filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
