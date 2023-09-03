import pickle

file = open('data.dat', 'rb')

otherlist = pickle.load(file)

print(otherlist)

