# for i in range( 1, 4 ):
#     for j in range( 1, 4 ):
#         print('Running i=', i, 'j=', j)

# print()


# for i in range(1, 4):
#     for j in range(1, 4):
#         print('Running i =', i, 'j =', j)
#         if i == 2 and j == 3:
#             print('Breaks inner loop at i=1 j=3')
#             break


# print()



for i in range(1, 4):  # Outer loop: i = 1 to 3
    for j in range(1, 4):  # Inner loop: j = 1 to 3
        if i == 1 and j == 2:
            print('\nContinues inner loop at i=1 j=3')
            continue  # Skips the rest of this inner loop iteration
        if i == 3 and j == 2:
            print('\nBreaks inner loop at i=2 j=1')
            break  # Exits the inner loop completely for this i
        print('Running i =', i, 'j =', j)