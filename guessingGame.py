import random 

num = random.randint( 1, 20 )
flag = True
guess = 0

print('Guess my number 1-20:', end = ' ')

while flag : # while flag remains true
    guess = input()
    if not guess.isdigit() :
        print('Invalid! Enter only digits 1-20')
        continue # book had break which then exits the loop after one guess/ loop
    elif int(guess) < num :
        print('Too low, try again : ', end = ' ')
    elif int( guess ) > num :
        print('Too high try again: ', end = ' ')
    else:
        print('Correct.. My number is ' + guess )
        flag = False