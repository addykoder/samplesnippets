
#Notebook.txt needs to exist
file = open('Notebook.txt', 'r')

lines = file.readlines()
print(f'{len(lines)} Lines in the file\n')

for no, line in enumerate(lines):
    print(f'{no+1} {line}', end='')


# other part of 12th question is same as 9th and 10th