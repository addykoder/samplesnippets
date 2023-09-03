file = open('Note.txt' , 'w')

def Multiple():
	while True:
					text  = input()
					if text == '0':
									break;
					file.write(text)
					file.write('\n')

Multiple()
file.close()