def echo( user, lang, sys ):
    print('\n','User:',user, 'Language:', lang, 'Platform', sys ,'\n')

echo('Mike', 'Python', 'Windows')

echo(lang ='Python', sys= 'Mac OS', user = 'Anne')

def mirror( user ='Carole', lang = 'Python'):
    print('\nUser:', user, 'Language', lang, '\n')

mirror()
mirror(lang = 'Java')
mirror('Tony')
mirror('Susan', 'C++')

