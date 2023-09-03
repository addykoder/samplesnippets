import csv

file = open('Phone.txt', 'w')
myWriter = csv.writer(file)

def Contact():
    myWriter.writerow(['Name', 'ContactNo'])
    
    myWriter.writerows([
					['Aditya', '1231231230',],
					['Akshat',  '1231231230'],
					['Ayush',  '1231231230'],
					['Ankush', '1231231230'],
					['Aman', '1231231230'],
		])

Contact()
file.close()