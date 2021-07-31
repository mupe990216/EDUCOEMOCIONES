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
	cursor_tb.execute(
			"""
				create table if not exists avance_infante(
					nombre_infante text not null,
					modulo text not null,
					sesion text not null,
					primary key(nombre_infante,modulo,sesion)
				)				
			"""
		)

def inserta_avance(conexion,nom):
	try:
		cursor_tb = conexion.cursor()
		sentencia = "insert into avance_infante(nombre_infante,modulo,sesion) values(?,1,1)"
		cursor_tb.execute(sentencia,(nom,))
		sentencia = "insert into avance_infante(nombre_infante,modulo,sesion) values(?,2,1)"
		cursor_tb.execute(sentencia,(nom,))
		sentencia = "insert into avance_infante(nombre_infante,modulo,sesion) values(?,3,1)"
		cursor_tb.execute(sentencia,(nom,))		
		print("Avance Registrado")
	except Exception as e:
		print(" ** Error Insertar avance: \n {}".format(e))

def consulta_avance(conexion,infante,modulo):
	try:
		cursor_tb = conexion.cursor()
		sentencia = "select sesion from avance_infante where nombre_infante=? and modulo=?"
		respuesta = cursor_tb.execute(sentencia,(infante,modulo))
		existencia = respuesta.fetchone()
		return existencia[0]
	except Exception as e:
		print(" ** Error Consulta Avance: \n {}".format(e))

def actualiza_avance(conexion,infante,modulo):
	try:
		cursor_tb = conexion.cursor()
		sentencia = "select sesion from avance_infante where nombre_infante=? and modulo=?"
		respuesta = cursor_tb.execute(sentencia,(infante,modulo))
		sesion = respuesta.fetchone()[0]
		sentencia = "update avance_infante set sesion=? where nombre_infante=? and modulo=?"
		cursor_tb.execute(sentencia,(int(sesion)+1,infante,modulo))
		conexion.commit()
	except Exception as e:
		print(" ** Error Actualiza Avance: \n {}".format(e))

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
		inserta_avance(conexion,list_data[0])
		conexion.commit()
		return "Infante registrado"
	else:
		return "Infante existente"

def valida_pregunta(conexion,list_data):
	try:
		cursor_tb = conexion.cursor()		
		sentencia = "select count(*) from preguntas where nombre_infante=? and modulo=? and sesion=? and submod=? and numPre=?"
		respuesta = cursor_tb.execute(sentencia,list_data[:-1])
		existe = respuesta.fetchone()[0]
		return existe
	except Exception as e:
		print("** Error valida pregunta: \n {} \n\n".format(e))

def inserta_pregunta(conexion,list_data):
	try:
		valida = valida_pregunta(conexion,list_data)
		if valida == 0:
			cursor_tb = conexion.cursor()
			sentencia = "insert into preguntas(nombre_infante,modulo,sesion,submod,numPre,valor) values(?,?,?,?,?,?)"
			cursor_tb.execute(sentencia,list_data)
			conexion.commit()
			print("Pregunta Registrada")
	except Exception as e:
		print("** Error inserta pregunta: \n {} \n\n".format(e))

def valida_intervencion(conexion,list_data):
	try:
		cursor_tb = conexion.cursor()		
		sentencia = "select count(*) from ses_intervencion where nombre_infante=? and modulo=? and sesion=? and submod=? and numPre=?"
		respuesta = cursor_tb.execute(sentencia,list_data[:-1])
		existe = respuesta.fetchone()[0]
		return existe
	except Exception as e:
		print("** Error valida pregunta: \n {} \n\n".format(e))

def inserta_intervencion(conexion,list_data):
	try:
		valida = valida_intervencion(conexion,list_data)
		if valida == 0:
			cursor_tb = conexion.cursor()
			sentencia = "insert into ses_intervencion(nombre_infante,modulo,sesion,submod,numPre,valor) values(?,?,?,?,?,?)"
			cursor_tb.execute(sentencia,list_data)
			conexion.commit()
			print("Pregunta Registrada")
		else:
			print("\t --- Error al volver registrar pregunta ---")
	except Exception as e:
		print("** Error inserta pregunta: \n {} \n\n".format(e))

# print(consulta_avance(conecta_db("EDUCOEMOCIONES.db"),'elias','1'))
# actualiza_avance(conecta_db("EDUCOEMOCIONES.db"),'elias','3')

