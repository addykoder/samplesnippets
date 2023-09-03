import csv

#contact txt needs to exist
file = open('contact.txt', 'r')
myReader = csv.reader(file, delimiter=' ')

def Read():

	for i in myReader:
		print(i)

Read()
file.close()