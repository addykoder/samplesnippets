
# DIARY.txt needs to exist
file = open('DIARY.txt', 'r')

def Read():
	lines = file.readlines()
	for line in lines:
		if line[0] in 'pP':
			print(line, end='')

Read()
file.close()