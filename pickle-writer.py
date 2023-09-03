
import pickle

file = open('data.dat', 'wb')

mylist = [
['abc', 'def', 'ghi', 'sddfljsdfdflj'],
['abc', 'def', 'ghi', 'sddfljsdfdflj'],
['abc', 'def', 'ghi', 'sddfljsdfdflj'],
['abc', 'def', 'ghi', 'sddfljsdfdflj'],
['abc', 'def', 'ghi', 'sddfljsdfdflj'],
['abc', 'def', 'ghi', 'sddfljsdfdflj'],
['abc', 'def', 'ghi', 'sddfljsdfdflj'],
['abc', 'def', 'ghi', 'sddfljsdfdflj'],
['abc', 'def', 'ghi', 'sddfljsdfdflj'],
['abc', 'def', 'ghi', 'sddfljsdfdflj'],
['abc', 'def', 'ghi', 'sddfljsdfdflj'],
['abc', 'def', 'ghi', 'sddfljsdfdflj'],
]

pickle.dump(mylist, file)


file.close()
