import csv

personas = [
	['hola','queXD'],
	['adios','jeje'],
	['xD','kha'],
	[],
	['jajaja'],
	[],
	[],
	["holi"]
]

with open("Prueba.csv","w",newline="") as file:
	writer = csv.writer(file, delimiter=",")
	writer.writerows(personas)