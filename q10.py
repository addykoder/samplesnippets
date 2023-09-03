

# MYNOTES.txt needs to exist
file = open('MYNOTES.txt', 'r')

def Read():
	lines = file.readlines()
	for line in lines:
		if line[0] in 'kK':
			print(line, end='')

Read()
file.close()