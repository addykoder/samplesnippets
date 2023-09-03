
fileName = input('Enter file name: ')

try:
    file = open(fileName, 'r')
    lines = file.readlines()
    for line in lines:
            if '#' in line: print(line, end='')
except:
		print('file not found')