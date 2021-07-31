import csv

personas = [
	
]

with open("Prueba.csv","w",newline="") as file:
	writer = csv.writer(file, delimiter=",")
	writer.writerows(personas)