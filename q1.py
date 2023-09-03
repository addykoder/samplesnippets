import csv

file = open('student.txt', 'w', newline='')
myWriter = csv.writer(file)

def result():
    myWriter.writerow(['Name', 'English', 'Math', 'CS'])
    
    myWriter.writerows([
					['Aditya', '10', '12', '14'],
					['Akshat', '10', '12', '14'],
					['Ayush', '10', '12', '14'],
					['Ankush', '10', '12', '14'],
					['Aman', '10', '12', '14'],
		])

result()
file.close()
