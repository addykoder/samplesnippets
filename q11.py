#source.txt needs to exist
source = open('source.txt', 'r')
target = open('target.txt', 'w')

lines = source.readlines()

for line in lines:
		if line[0] != '@':
			target.write(line)

source.close()
target.close()