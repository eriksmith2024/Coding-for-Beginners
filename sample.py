from random import random, sample

num = random()
print ( '\n0.0 to 1.0 Random float ', num)

num = int(num * 10 )
print( '\n0 to 9 Random integer ', num)

nums = [] ; i = 0
while i < 6 :
    nums.append(int(random() * 10 ) + 1)
    i += 1
print( '\n1 to 10 Random sample of integers:', nums)

nums = sample( range( 1, 60 ), 6)
print( '\n1 to 59 Random Integer Sample: ', nums)

print()
