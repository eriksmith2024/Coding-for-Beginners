chars = ['A', 'B', 'C']
fruit = ('Apple','Banana','Cherry')
info = {'name ': ' Mike', 'ref ': ' Python', 'sys' : 'Win'}

print('\nElements: \t', end = '')
for i in chars:
    print(i, end = ' ')

print('\nEnumerated:\t', end = '')
for item in enumerate( chars ):
    print(item, end = ' ')

print('\nZipped: \t' , end = ' ')
for item in zip(chars , fruit) :
    print( item ,  end = ' ')

print('\n\nPaired:')
for key , value in info.items():
    print(key, '=', value, '\n')


