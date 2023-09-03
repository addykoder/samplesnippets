import csv

#phone.txt must exist
file = open('phone.txt', 'r')
reader = csv.reader(file)

for consumer in reader:
    if consumer[0][0] in 'dD':
        print(f'{consumer[0]} {consumer[1]}')


file.close()