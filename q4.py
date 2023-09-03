lower = open('lower.txt' , 'w')
upper = open('upper.txt' , 'w')
other = open('other.txt' , 'w')

def Multiple():
	while True:
					text  = input()
					if text == '0':
									break;
					
					if text.isupper():
						upper.write(text)
					if text.islower():
						lower.write(text)
					if not text.isalpha():
						other.write(text)

Multiple()

lower.close()
upper.close()
other.close()