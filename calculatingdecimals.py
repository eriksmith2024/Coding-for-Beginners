from decimal import *

item = 0.70
rate = 1.05

tax = item * rate
total = item + tax

print('Item:\t', '{:.2f}'.format( item ))
print('Tax:\t', '{:.2f}'.format( tax ))
print('Total:\t', '{:.2f}'.format( total ))

print()

print('Item:\t', '{:.20f}'.format( item ))
print('Tax:\t', '{:.20f}'.format( tax ))
print('Total:\t', '{:.20f}'.format( total ))

item = Decimal(0.70)
rate = Decimal(1.05)

tax = item * rate
total = item + tax

print('\nCorrected data using maths Decimal')

print('Item:\t', '{:.2f}'.format( item ))
print('Tax:\t', '{:.2f}'.format( tax ))
print('Total:\t', '{:.2f}'.format( total ))