chars = ['A', 'B', 'C']
fruit = ('Apple','Banana','Cherry')
info = {'name ': ' Mike', 'ref ': ' Python', 'sys' : 'Win'}

print('Elements: \t', end = '')
for i in chars:
    print(i, end = ' ')

print('\nEnumerated:\t', end = '')
for item in enumerate( chars ):
    print(item, end = ' ')

print('\nZipped: \t' , end = ' ')
for item in zip(chars , fruit) :
    print( item ,  end = ' ')