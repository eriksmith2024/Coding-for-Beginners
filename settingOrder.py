a = 2
b = 4
c = 8

# Forcing addition before multiplication
print('\nDefault Order:\t', a, '*', c, '+', b, '=', a * c + b)
print('Forced Order:\t', a, '* (',c,'+', b,') =', a * (c + b))

# Forcing subtraction before divsion
print('\nDefault Order:\t', c, '//', b, '-', a, '=', c // b - a)
print('Forced order:\t', c, '//(', b,'-', a, ') s=', c // ( b - a))

print('\nDefault Order:\t', c, '%', a, '+', b, '=', c % a + b)
print('Forced Order:\t', c, '% (', a, '+', b,') =', c % (a + b))

print('\nDefault Order:\t', c, '**', a, '+', b, '=', c ** a + b)
print('Forced Order:\t', c, '** (', a, '+', b,') =', c ** (a + b))

