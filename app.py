import json
from flask import Flask,request, render_template, url_for, redirect, flash, session, jsonify
from scripts.db import *

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['SECRET_KEY'] = '12345678'

"""
Funcion donde los infantes registran sus datos al inicio de cada sesion.
Se recomienda normalizar la base de datos y generar un usuario y contraseña a cada infante, asi como aplicar la arquitectura de diseño enfocada en agregar y no en modificar relaciones.
Se uso este diseño ya que fue el solicitado por los especialistas, dicho diseño se encuentra en la carpeta "docs" y lleva por nombre "EDUCOEMOCIONES DISEÑO v1.pdf"
"""
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
		return redirect(url_for("inicio"))

""" 
	Por el tiempo no fue posible desarrollar este modulo, 
	Este esta pensando para el menu de administradores,
	La forma de graficacion de la informacion asi como el aspecto visual si se desarrollaron pero unicamente la parte funcional en JS.
	Los archivos se llaman "grafica1.js" , "grafica2.js", "grafica3.js" y "grafica4.js"
	Estos archivos contienen el codigo fuente necesario para desplegar la informacion a traves de 4 diferentes graficas con opciones para descargar dicho grafico en PDF, SVG, PNG y mandar a imprimir.
"""
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
		return redirect(url_for("inicio"))

# Funcion que registra al usuario, mostrando un menu de inicio
@app.route('/index_usr', methods=['POST','GET'])
def menu_modulos():	
	try:
		if session["nom"]!=None:
			return render_template('usr_index.html',nombre=session["nom"],gen=session["gen"])
	except Exception as e:
		print(e)		
		return redirect(url_for("inicio"))


# Funcion que redirecciona con base en la opcion del usuario
@app.route('/mod<int:num_m>', methods=['POST','GET'])
def select_mod(num_m):
	try:
		if((num_m==1) or (num_m==2) or (num_m==3)):
			conexion = conecta_db("EDUCOEMOCIONES.db")
			tam = consulta_avance(conexion,(session["nom"]).lower(),num_m)
			close_db(conexion)		
			return render_template('usr_mod.html',nombre=session["nom"],gen=session["gen"],modulo=num_m, control=int(tam))
		else:
			return redirect(url_for("inicio"))
	except Exception as e:
		print(e)
		return redirect(url_for("inicio"))

# Funcion que redirecciona con base en la sesion indicada
@app.route('/mod<int:num_m>/sesion<int:num_s>/subm<int:num_sub>')
def select_sesi(num_m,num_s,num_sub):
	try:
		if((num_m==1) or (num_m==2) or (num_m==3)):
			if((num_s==1) or (num_s==2)):
				return render_template('usr_ses.html',nombre=session["nom"],gen=session["gen"],modulo=num_m,sesion=num_s,submodulo=num_sub)
			else:
				return render_template('ind_init.html',seleccion=0)
		else:
			return redirect(url_for("inicio"))
	except Exception as e:
		print(e)		
		return redirect(url_for("inicio"))

# Funcion que redirecciona con base en la sesion realizada para que realice un cuestionario
@app.route('/mod<int:num_m>/sesion<int:num_s>/subm<int:num_sub>/test')
def select_test(num_m,num_s,num_sub):
	try:
		if((num_m==1) or (num_m==2) or (num_m==3)):
			if((num_s==1) or (num_s==2)):
				return render_template('usr_tes.html',nombre=session["nom"],gen=session["gen"],modulo=num_m,sesion=num_s,submodulo=num_sub)
			else:
				return render_template('ind_init.html',seleccion=0)
		else:
			return redirect(url_for("inicio"))
	except Exception as e:
		print(e)		
		return redirect(url_for("inicio"))

# Funcion que redirecciona a la retroalimentacion, si es que el infante se equivoco en el test
@app.route('/mod<int:num_m>/sesion<int:num_s>/subm<int:num_sub>/retro')
def select_retro(num_m,num_s,num_sub):
	try:
		if((num_m==1) or (num_m==2) or (num_m==3)):
			if((num_s==1) or (num_s==2)):
				return render_template('usr_ret.html',nombre=session["nom"],gen=session["gen"],modulo=num_m,sesion=num_s,submodulo=num_sub)
			else:
				return render_template('ind_init.html',seleccion=0)
		else:
			return redirect(url_for("inicio"))
	except Exception as e:
		print(e)		
		return redirect(url_for("inicio"))

# Funcion que redirecciona a las sesiones de intervencion a traves de preguntas abiertas
@app.route('/mod<int:num_m>/sesion<int:num_s>/s-preguntas')
def intervencion_preguntas(num_m,num_s):
	try:
		if((num_m==1) or (num_m==2) or (num_m==3)):
			if((num_s==1) or (num_s==2) or (num_s==3)):
				return render_template('usr_int.html',nombre=session["nom"],gen=session["gen"],modulo=num_m,sesion=num_s)
			else:
				return redirect(url_for("inicio"))
		else:
			return redirect(url_for("inicio"))
	except Exception as e:
		print(e)		
		return redirect(url_for("inicio"))

# Guarda las respuestas de los cuestionarios de cada infante, cero-incorrecto, uno-correcto
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
	for numPre in range(0,tam):
		conexion = conecta_db("EDUCOEMOCIONES.db")
		list_data.clear()
		list_data.append(nombre)
		list_data.append(modulo)
		list_data.append(sesion)
		list_data.append(submod)
		list_data.append(numPre)
		list_data.append(arregl[numPre]) #valor
		inserta_pregunta(conexion,list_data)
		close_db(conexion)
		numPre+=1
	# print("modulo {} sesion {} submodulo {}".format(modulo,sesion,submod))
	if '0' in arregl:
		msj = "comic"
	else:
		msj = "siguiente"
	return msj

# Guarda las respuestas abiertas que contesten los infantes en las sesiones de intervencion
@app.route('/SaveInter',methods=['POST'])
def guarda_intervencion():
	list_data = list()
	msj = ""
	nombre = session["nom"].lower()
	arregl = json.loads(request.form['arreglo'])
	modulo = request.form['modulo']
	sesion = request.form['sesion']
	submod = request.form['submod']
	tam = len(arregl)
	for numPre in range(0,tam):
		conexion = conecta_db("EDUCOEMOCIONES.db")
		list_data.clear()
		list_data.append(nombre)
		list_data.append(modulo)
		list_data.append(sesion)
		list_data.append(submod)
		list_data.append(numPre)
		list_data.append(arregl[numPre]) #valor
		inserta_intervencion(conexion,list_data)
		close_db(conexion)
		numPre+=1
	# print(type(sesion))
	if sesion == '2':
		msj = "Fin"
	else:
		msj = "Listo"
	return msj

"""
Modifica el flujo de los elementos que se van a mostrar
Dependiendo el siguiente modulo o sesion que vaya pasando el infante
Se configura conforme lo solicitado por los especialistas
"""
@app.route('/modControl',methods=['POST'])
def modControl():
	modulo = request.form['mod']
	conexion = conecta_db("EDUCOEMOCIONES.db")
	actualiza_avance(conexion,session["nom"].lower(),modulo)
	close_db(conexion)
	return "Control Modificado"

# Pantalla final de cada sesion o modulo programado de acuerdo al especialista
@app.route('/gracias',methods=['get'])
def gracias():
	return render_template('usr_thks.html',nombre=session["nom"],gen=session["gen"])

# Main principal de la app en flask
if __name__=='__main__':
	conexion = conecta_db("EDUCOEMOCIONES.db")
	crea_tbs(conexion)
	close_db(conexion)
	app.run(host='0.0.0.0',port=80,debug=True)
	# app.run(host='192.168.1.16',port=80,debug=True)
	# app.run(host='127.0.0.1',port=80,debug=True)