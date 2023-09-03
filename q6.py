import csv

# employee.txt needs to exist with already existing data

file = open('exployee.txt', 'a')
myWriter = csv.writer(file)

def result():
    myWriter.writerow(['New Emp 1', '18000', 'IT', 'Kanpur'])
    myWriter.writerow(['New Emp 2', '22000', 'Sales', 'Lucknow'])

result()
file.close()