# a = b = 1
# while b < 100:
#     print(b)
#     a,b = b, a + b

i = 1
while i < 4 :
    print('Outer Loop Iteration:',i)
    i += 1

    j = 1
    while j < 6 :
        print('\tInner Loop Iteration', j )
        j += 1