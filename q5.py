
# bigFile.txt needs to be already created
# otherwise this will give an error
with open('bigFile.txt', 'a') as file:
	file.write('\n This is the new sentence')