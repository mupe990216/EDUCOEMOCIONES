import sqlite3

def conecta_db(name):
	return sqlite3.connect(name)

def close_db(conexion):
	conexion.close()

def crea_tbs(conexion):
	cursor_tb = conexion.cursor()
	cursor_tb.execute(
			"""
				create table if not exists administrador(
					usuario text not null primary key,
					contrasenia text not null
				)				
			"""
		)
	cursor_tb.execute(
			"""
				create table if not exists infante(
					nombre text not null primary key,
					edad text not null,
					genero text not null,
					grado text not null
				)				
			"""
		)
	cursor_tb.execute(
			"""
				create table if not exists preguntas(
					nombre_infante text not null,
					modulo text not null,
					sesion text not null,
					submod text not null,
					numPre text not null,
					valor text not null,
					fecha timestamp default current_timestamp,
					foreign key(nombre_infante) references infante(nombre),
					primary key (nombre_infante,modulo,sesion,submod,numPre)
				)
			"""
		)
	cursor_tb.execute(
			"""
				create table if not exists ses_intervencion(
					nombre_infante text not null,
					modulo text not null,
					sesion text not null,
					submod text not null,
					numPre text not null,
					valor text not null,
					fecha timestamp default current_timestamp,
					foreign key(nombre_infante) references infante(nombre),
					primary key (nombre_infante,modulo,sesion,submod,numPre)
				)
			"""
		)

def valida_login(conexion,list_data):
	cursor_tb = conexion.cursor()
	sentencia = "select * from administrador where usuario=? and contrasenia=?"
	respuesta = cursor_tb.execute(sentencia,list_data)
	existencia = respuesta.fetchone()
	if existencia!=None:
		msj = "Bienvenida :)"
	else:
		msj = "Invalido"
	return msj

def valida_infa(conexion,nom):
	cursor_tb = conexion.cursor()
	sentencia = "select * from infante where nombre=?"
	respuesta = cursor_tb.execute(sentencia,(nom,))
	existencia = respuesta.fetchone()
	if existencia!=None:
		existe = 1		
	else:
		existe = 0
	return existe

def inserta_Infante(conexion,list_data):
	cursor_tb = conexion.cursor()
	valida = valida_infa(conexion,list_data[0])
	if valida == 0:
		sentencia = "insert into infante(nombre,edad,genero,grado) values(?,?,?,?)"
		cursor_tb.execute(sentencia,list_data)
		conexion.commit()
		return "Infante registrado"
	else:
		return "Infante existente"

def inserta_pregunta(conexion,list_data):
	try:
		cursor_tb = conexion.cursor()
		sentencia = "insert into preguntas(nombre_infante,modulo,sesion,submod,numPre,valor) values(?,?,?,?,?,?)"
		cursor_tb.execute(sentencia,list_data)
		conexion.commit()
		print("Pregunta Registrada")
	except Exception as e:
		print("Pregunta Previamente Insertada: \n {}".format(e))





