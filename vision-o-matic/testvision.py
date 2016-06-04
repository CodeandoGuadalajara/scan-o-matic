from clarifai.client import ClarifaiApi
import MySQLdb
import os

clarifai_api = ClarifaiApi() # assumes environment variables are set.
#path = '/Users/marcelarosales/Repos/scan-o-matic/vision-o-matic/fotos'

thisdir = os.path.dirname(os.path.realpath(__file__))

def get_nutri_facts(lst):
	# Open database connection
	db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	# Prepare SQL query to INSERT a record into the database.
	sql = "SELECT * FROM alimentos \
		   WHERE Alimento=%s OR  Alimento=%s \
		   OR Alimento=%s " %(lst[0], lst[1], lst[2])
	try:
		# Execute the SQL command
	   	cursor.execute(sql)
	   	# Fetch all the rows in a list of lists.
	   	results = cursor.fetchall()
	   	res = ""
	   	for row in results:
	   		"""
	      	Alimento = row[0]
	      	Calorias = row[1]
	      	Grasas_total = row[2]
	      	Acidos_grasos_saturados = row[3]
	     	Acidos_grasos_poliinsaturados = row[4]
	     	Acidos_grasos_monoinsaturados = row[5]
	    	Colesterol = row[6]
	   	   	Sodio = row[7]
	      	Potasio = row[8]
	      	Carbohidratos = row[9]
	      	Fibra = row[10]
	 	    Azucares = row[11]
	      	Proteinas = row[12]
	     	Hierro = row[13]
	      	Calcio  = row[14]
	      	Magnesio = row[15] 
		    VitaminA = row[16]
	      	VitaminB6 = row[17]
	      	VitaminB12 = row[18]
		    VitaminC = row[19]
	      	VitaminD = row[20]
	      	VitaminE = row[21]
	      	VitaminF = row[22]
	      	"""
	      	res = "{ Alimento:%s, Calorias:%s , Grasas_total:%s ,Acidos_grasos_saturados:%s,\
	     			 Acidos_grasos_poliinsaturados:%s, Acidos_grasos_monoinsaturados:%s,\
	    			 Colesterol:%s, Sodio:%s, Potasio:%s, Carbohidratos:%s, Fibra:%s, Azucares:%s,\
	      			 Proteinas:%s, Hierro:%s, Calcio:%s, Magnesio:%s, VitaminA:%s, VitaminB6:%s,\
	      			 VitaminB12:%s, VitaminC:%s, VitaminD:%s, VitaminE:%s, VitaminF:%s} " 
	      			 %(row[0],row[1],row[2], row[3],row[4],row[5],row[6],row[7],row[8],row[9],
	      			 	row[10],row[11],row[12], row[13],row[14],row[15],row[16],row[17],row[18],row[19],
	      			 	row[20],row[21],row[22])
	    except:
	    	print "No pudimos encontrar tu alimento."

	# disconnect from server
	db.close()


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

print "-------- Zanahoria"
result = clarifai_api.tag_images(open(thisdir + '/fotos/zanahoria.jpg', 'rb'))
print result['results'][0]['result']['tag']['classes']
print result['results'][0]['result']['tag']['probs']

print "-------- Lechuga"
result = clarifai_api.tag_images(open(thisdir + '/fotos/lechuga.jpg', 'rb'))
print result['results'][0]['result']['tag']['classes']
print result['results'][0]['result']['tag']['probs']


import pdb; pdb.set_trace()




