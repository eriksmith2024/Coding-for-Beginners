# title = 'Coding for Beginners in easy steps'

# try:

#     print(titel)

# except NameError as msg:
#     print( msg )


day = 32

try : 
    if day > 31 :
        raise ValueError( 'Invalid Day Number')
        #More statements to execute get added here. 

except ValueError as msg :
    print( 'The program found An', msg)

finally: 
    print('But today is a beautiful day anyway')