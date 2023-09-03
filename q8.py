import csv

file = open('student.txt', 'r')
myReader = csv.reader(file)

def Read():

	for i in myReader:
		print(i)

Read()
file.close()