import sqlite3

def conecta_db(name):
	return sqlite3.connect(name)

def close_db(conexion):
	conexion.close()

def crea_tbs(conexion):
	cursor_tb = conexion.cursor()
	cursor_tb.execute(
			"""
				create table if not exists credenciales(
					usr text not null primary key,
					psw text not null
				)				
			"""
		)
	cursor_tb.execute(
			"""
				create table if not exists tipoUsr(
					idTipoUsr integer not null primary key,
					descrip text not null
				)
			"""
		)
	# Ingresamos los tipos de usuario que tendra el sistema
	llena_cats(conexion,"tipoUsr","idTipoUsr","1",[1,'Administrador'],'idTipoUsr,descrip')
	llena_cats(conexion,"tipoUsr","idTipoUsr","2",[2,'Cliente'],'idTipoUsr,descrip')

def valida_login(conexion,usr,psw,opc):
	cursor_tb = conexion.cursor()
	if(opc==1):
		sentencia = "select * from credenciales where usr=? and psw=?"
		respuesta = cursor_tb.execute(sentencia,(usr,psw))
	if(opc==2):
		sentencia = "select * from credenciales where usr=?"
		respuesta = cursor_tb.execute(sentencia,(usr,))
	existencia = respuesta.fetchone()
	if existencia != None:				
		sentencia = "select idTipoUsr from persona where usr=?"
		respuesta = cursor_tb.execute(sentencia,(usr,))
		if(respuesta.fetchone()[0]==1):
			return "Administrador"
		else:
			return "Cliente"
	else:
		return "Invalido"


def alta_usur(conexion,email,usr,psw,nom,apep,apem,sexo,tipo):
	msj = ""
	credenciales = valida_login(conexion,usr,psw,2)
	if(credenciales=="Invalido"):
		correo = valida_email(conexion,email)
		if(correo==0):
			cursor_tb = conexion.cursor()
			sentencia = "insert into credenciales values(?,?)"
			respuesta = cursor_tb.execute(sentencia,(usr,psw))
			sentencia = "insert into persona values(?,?,?,?,?,?,?)"
			respuesta = cursor_tb.execute(sentencia,(email,usr,nom,apep,apem,sexo,tipo))
			conexion.commit()
			if(tipo==1):
				msj = "Administrador registrado"
			elif(tipo==2):
				msj = "Cliente registrado"
		elif(correo==1):
			msj = "Existe una persona con ese correo"
	elif(credenciales=="Administrador"):
		msj = "Existe un administrador con ese usuario"
	elif(credenciales=="Cliente"):
		msj = "Existe un cliente con ese usuario"	

	return msj

def consulta_usur(conexion,tipo):
	cursor_tb = conexion.cursor()
	if(tipo==1):
		sentencia = "select * from persona where idTipoUsr=1"
	elif(tipo==2):
		sentencia = "select * from persona where idTipoUsr=2"
	return cursor_tb.execute(sentencia)


def consulta_usur_esp(conexion,usr):
	cursor_tb = conexion.cursor()
	sentencia = "select * from persona where usr=?"
	return cursor_tb.execute(sentencia,(usr,))









