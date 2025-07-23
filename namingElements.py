info = { 'name' : 'Bob', 'ref':'Python', 'sys':'Win'}
print('\ninfo:', type(info))
print('\nDictionary:',info,)

print('\nReference:',info['ref'])

print('\nKeys:', info.keys())

del info['name']
print('\nNewDisctionary', info,'\n')# I added this to show where one of the key value pairs in the dictionary has been deleted
info['user'] = 'Tom'
print('\nDictionary:' , info)

print('\nIs There is A name key?:', 'name' in info, '\n')




