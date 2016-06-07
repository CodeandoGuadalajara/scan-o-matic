from clarifai.client import ClarifaiApi
from flask import jsonify
import MySQLdb
import os

clarifai_api = ClarifaiApi() # assumes environment variables are set.

thisdir = os.path.dirname(os.path.realpath(__file__))

def get_nutri_facts(lst):
	# Open database connection
	db = MySQLdb.connect(host="192.168.99.100", port=32768 ,user="root",db="scanomatic" )

	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	# Prepare SQL query to INSERT a record into the database.
	sql = "SELECT * FROM alimentos \
		   WHERE Alimento='%s' OR  Alimento='%s' \
		   OR Alimento='%s' " %(str(lst[0]), str(lst[1]), str(lst[2]))
	print sql
	try:
		# Execute the SQL command
	   	cursor.execute(sql)
	   	# Fetch all the rows in a list of lists.
	   	results = cursor.fetchall()
	   	for row in results:
	   		res = {
	      	'Alimento': row[0],
	      	'Calorias': row[1],
	      	'Grasas_total': row[2],
	      	'Acidos_grasos_saturados': row[3],
	     	'Acidos_grasos_poliinsaturados': row[4],
	     	'Acidos_grasos_monoinsaturados': row[5],
	    	'Colesterol': row[6],
	   	   	'Sodio': row[7],
	      	'Potasio': row[8],
	      	'Carbohidratos': row[9],
	      	'Fibra': row[10],
	 	    'Azucares': row[11],
	      	'Proteinas': row[12],
	     	'Hierro': row[13],
	      	'Calcio ': row[14],
	      	'Magnesio': row[15],
		    'VitaminA': row[16],
	      	'VitaminB6': row[17],
	      	'VitaminB12': row[18],
		    'VitaminC': row[19],
	      	'VitaminD': row[20],
	      	'VitaminE': row[21],
	      	'VitaminF': row[22]
			}
	except:
		print "No pudimos encontrar tu alimento."

	# disconnect from server
	db.close()
	print res
	return res


print "-------- Coca"
result = clarifai_api.tag_images(open(thisdir + '/fotos/coca.jpg', 'rb'))
print result['results'][0]['result']['tag']['classes']
print result['results'][0]['result']['tag']['probs']

print "-------- Galleta"
result = clarifai_api.tag_images(open(thisdir + '/fotos/galleta.jpg', 'rb'))
print result['results'][0]['result']['tag']['classes']
print result['results'][0]['result']['tag']['probs']

print "-------- Manzana"
result = clarifai_api.tag_images(open(thisdir + '/fotos/manzana.jpg', 'rb'))
print result['results'][0]['result']['tag']['classes']
print result['results'][0]['result']['tag']['probs']

print "-------- Banana"
result = clarifai_api.tag_images(open(thisdir + '/fotos/banana.jpg', 'rb'))
print result['results'][0]['result']['tag']['classes']
print result['results'][0]['result']['tag']['probs']

mylist = result['results'][0]['result']['tag']['classes']
get_nutri_facts(mylist)

print "-------- Zanahoria"
result = clarifai_api.tag_images(open(thisdir + '/fotos/zanahoria.jpg', 'rb'))
print result['results'][0]['result']['tag']['classes']
print result['results'][0]['result']['tag']['probs']

print "-------- Lechuga"
result = clarifai_api.tag_images(open(thisdir + '/fotos/lechuga.jpg', 'rb'))
print result['results'][0]['result']['tag']['classes']
print result['results'][0]['result']['tag']['probs']



import pdb; pdb.set_trace()
