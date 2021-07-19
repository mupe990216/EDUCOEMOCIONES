import json
from flask import Flask,request, render_template, url_for, redirect, flash, session, jsonify
from scripts.db import *

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['SECRET_KEY'] = '12345678'

@app.route('/', methods=['POST','GET'])
def inicio():
	try:
		if request.method == "POST":
			list_data = list()
			nom = request.form['nom']
			eda = request.form['eda']
			gen = request.form['gen']
			gra = request.form['gra']
			session["nom"] = nom.capitalize()
			session["gen"] = gen
			list_data.append(nom.lower())
			list_data.append(eda)
			list_data.append(gen)
			list_data.append(gra)
			conexion = conecta_db("EDUCOEMOCIONES.db")
			respuesta = inserta_Infante(conexion,list_data)
			close_db(conexion)
			return respuesta
		else:
			session.clear()
			return render_template('ind_init.html',seleccion=0)
	except Exception as e:
		print(e)
		session.clear()
		return render_template('ind_init.html',seleccion=0)


@app.route('/login', methods=['POST','GET'])
def login():
	try:
		if request.method == "POST":
			list_data = list()
			usr = request.form['usr']
			psw = request.form['psw']
			list_data.append(usr)
			list_data.append(psw)
			conexion = conecta_db("EDUCOEMOCIONES.db")
			respuesta = valida_login(conexion,list_data)
			close_db(conexion)
			return respuesta
		else:
			session.clear()
			return render_template('ind_init.html',seleccion=1)
	except Exception as e:
		print(e)
		session.clear()		
		return render_template('ind_init.html',seleccion=1)

# Funcion que registra al usuario, mostrando un menu de inicio
@app.route('/index_usr', methods=['POST','GET'])
def menu_modulos():	
	return render_template('usr_index.html',nombre=session["nom"],gen=session["gen"])

# Funcion que redirecciona con base en la opcion del usuario
@app.route('/mod<int:num_m>', methods=['POST','GET'])
def select_mod(num_m):
	if((num_m==1) or (num_m==2) or (num_m==3)):
		return render_template('usr_mod.html',nombre=session["nom"],gen=session["gen"],modulo=num_m)	
	else:
		return render_template('ind_init.html',seleccion=0)

# Funcion que redirecciona con base en la sesion indicada
@app.route('/mod<int:num_m>/sesion<int:num_s>/subm<int:num_sub>')
def select_sesi(num_m,num_s,num_sub):
	if((num_m==1) or (num_m==2) or (num_m==3)):
		if((num_s==1) or (num_s==2)):
			return render_template('usr_ses.html',nombre=session["nom"],gen=session["gen"],modulo=num_m,sesion=num_s,submodulo=num_sub)
		else:
			return render_template('ind_init.html',seleccion=0)
	else:
		return render_template('ind_init.html',seleccion=0)

# Funcion que redirecciona con base en la sesion realizada
@app.route('/mod<int:num_m>/sesion<int:num_s>/subm<int:num_sub>/test')
def select_test(num_m,num_s,num_sub):
	if((num_m==1) or (num_m==2) or (num_m==3)):
		if((num_s==1) or (num_s==2)):
			return render_template('usr_tes.html',nombre=session["nom"],gen=session["gen"],modulo=num_m,sesion=num_s,submodulo=num_sub)
		else:
			return render_template('ind_init.html',seleccion=0)
	else:
		return render_template('ind_init.html',seleccion=0)

@app.route('/SaveTest',methods=['POST'])
def guarda_test():
	list_data = list()	
	msj = ""
	nombre = session["nom"].lower()
	arregl = json.loads(request.form['arreglo'])
	modulo = request.form['modulo']
	sesion = request.form['sesion']
	submod = request.form['submod']
	tam = len(arregl)
	conexion = conecta_db("EDUCOEMOCIONES.db")	
	for numPre in range(0,tam):
		list_data.clear()
		list_data.append(nombre)
		list_data.append(modulo)
		list_data.append(sesion)
		list_data.append(submod)
		list_data.append(numPre)
		list_data.append(arregl[numPre]) #valor
		inserta_pregunta(conexion,list_data)		
		numPre+=1
	close_db(conexion)
	# print("modulo {} sesion {} submodulo {}".format(modulo,sesion,submod))
	if '0' in arregl:
		msj = "comic"
	else:
		msj = "siguiente"
	return msj


if __name__=='__main__':
	conexion = conecta_db("EDUCOEMOCIONES.db")
	crea_tbs(conexion)
	close_db(conexion)
	app.run(host='0.0.0.0',port=80,debug=True)
	# app.run(host='192.168.1.16',port=80,debug=True)
	# app.run(host='127.0.0.1',port=80,debug=True)