import json
from flask import Flask,request, render_template, url_for, redirect, flash, session, jsonify
app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def inicio():
	return render_template('ind_init.html',seleccion=0)

@app.route('/login')
def login():
	return render_template('ind_init.html',seleccion=1)

# Funcion que registra al usuario, mostrando un menu de inicio
@app.route('/index_usr', methods=['POST','GET'])
def menu_modulos():
	return render_template('usr_index.html',nombre="Inicio")

# Funcion que redirecciona con base en la opcion del usuario
@app.route('/mod<int:num_m>', methods=['POST','GET'])
def select_mod(num_m):
	if((num_m==1) or (num_m==2) or (num_m==3)):
		return render_template('usr_mod.html',nombre="Modulo",modulo=num_m)	
	else:
		return render_template('ind_init.html',seleccion=0)

# Funcion que redirecciona con base en la sesion indicada
@app.route('/mod<int:num_m>/sesion<int:num_s>/subm<int:num_sub>')
def select_sesi(num_m,num_s,num_sub):
	if((num_m==1) or (num_m==2) or (num_m==3)):
		if((num_s==1) or (num_s==2)):
			return render_template('usr_ses.html',nombre="Sesion",modulo=num_m,sesion=num_s,submodulo=num_sub)
		else:
			return render_template('ind_init.html',seleccion=0)
	else:
		return render_template('ind_init.html',seleccion=0)

# Funcion que redirecciona con base en la sesion realizada
@app.route('/mod<int:num_m>/sesion<int:num_s>/subm<int:num_sub>/test')
def select_test(num_m,num_s,num_sub):
	if((num_m==1) or (num_m==2) or (num_m==3)):
		if((num_s==1) or (num_s==2)):
			return render_template('usr_tes.html',nombre="Cuestionario",modulo=num_m,sesion=num_s,submodulo=num_sub)
		else:
			return render_template('ind_init.html',seleccion=0)
	else:
		return render_template('ind_init.html',seleccion=0)

@app.route('/SaveTest',methods=['POST'])
def guarda_test():
	msj = ""
	arreglo = json.loads(request.form['arreglo'])
	if '0' in arreglo:
		msj = "comic"
	else:
		msj = "siguiente"
	return msj


if __name__=='__main__':
	app.run(host='0.0.0.0',debug=True)