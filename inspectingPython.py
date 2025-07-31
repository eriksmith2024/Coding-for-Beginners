import sys, keyword

print('\nPython Version:', sys.version )

print('\nPython Interpreter Location', sys.executable)

print('\nPython module path:')
for folder in sys.path :
    print( folder )

print('Python Keywords:')
for word in keyword.kwlist :
    print( word )